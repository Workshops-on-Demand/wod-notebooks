 # Copyright 2019 Hewlett Packard Enterprise Development LP
 #
 # Licensed under the Apache License, Version 2.0 (the "License"); you may
 # not use this file except in compliance with the License. You may obtain
 # a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 # License for the specific language governing permissions and limitations
 # under the License.

# Ansible Module derived from https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/set_uid_light.py

# Version 0.118

# -*- coding: utf-8 -*-
"""
Didactic example of an Ansible Redfish module for setting the UID light of a computer chassis
and its enclosure (if any) using the HPE python-ilorest-library and a session key (i.e. OneView token)
"""
DOCUMENTATION = '''
---
module: set_uid_light
short_description: Ansible Redfish module to modify the UID light status of a chassis and its enclosure (if any) using a session authentication method.
'''

EXAMPLES = '''
- name: set UID light
  become: yes
  set_uid_light:
    url: "https://<ip>:<port>"
    session_key: "<Token/Session key>"
'''

import sys
import json
import time
from redfish import RedfishClient   # RedfishClient is in the HPE's redfish class of the python-ilorest-library
from redfish.rest.v1 import ServerDownOrUnreachableError
from ansible.module_utils.basic import *

# The following get_resource_directory module comes from https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/get_resource_directory.py
# It has been included in this infrastructure to show how to speed up the crawling of 
# HPE iLO Redfish implementation
from get_resource_directory import get_resource_directory # HPE proprietarty 

def set_uid_light(_redfishobj):

    body = dict()
    chassis_members_uri = []
    chassis_members_response = []

    # Retrieve all data types/instances and associated data (i.e. location) 
    # from the resource directory (if any)
    resource_instances = get_resource_directory(_redfishobj)

    if DISABLE_RESOURCE_DIR or not resource_instances:
        #if we do not have a resource directory or want to force it's non use to find the
        #relevant URI
        chassis_uri = _redfishobj.root.obj['Chassis']['@odata.id']  # Retrieve location of Chassis data type
        chassis_response = _redfishobj.get(chassis_uri)             # Retrieve content of Chassis data type
        for chassis in chassis_response.obj['Members']:             # For each Member of the Chassis collection...
            chassis_members_uri.append( chassis['@odata.id'] )      # Append chassis location to list
            #print("Chassis list: " + str(chassis_members_uri))
            chassis_members_response.append(  \
                    _redfishobj.get(chassis['@odata.id']) )         # Retrieve/append chassis properties to list

    else:
        # Use resource directory to fast find the relevant URIs
        for instance in resource_instances:     # instance = Redfish data type
            if '#Chassis.' in instance['@odata.type']:              # if data type/instance is a Chassis
                chassis_members_uri.append( instance['@odata.id'] ) # Append chassis location to list
                chassis_members_response.append( \
                        _redfishobj.get(chassis_members_uri[-1]) )  # Retrieve/append chassis properties to list

    if chassis_members_response and chassis_members_uri:
        for chassis in chassis_members_response:
            #print("Current Indicator LED Status for chassis \'%s\': \'%s\'" % \
            #        (chassis.obj['Id'], chassis.obj['IndicatorLED']))
            if "Off" in chassis.obj['IndicatorLED']:
                #print("Will illuminate indicator LED for chassis \'%s\' \n" % chassis.obj['Id'])
                body["IndicatorLED"] = "Lit"
            else:
                #print("Will extinguish indicator LED for chassis \'%s\' \n" % chassis.obj['Id'])
                body["IndicatorLED"] = "Off"

            # Send PATCH request with new IndicatorLED value
            resp = _redfishobj.patch(chassis.obj['@odata.id'], body)   
            #If iLO responds with soemthing outside of 200, 201 and 204 (to work with DMTF Redfish simulaor),
            #check the iLO extended info error message to see what went wrong
            if resp.status == 400:
                try:
                    print(json.dumps(resp.obj['error']['@Message.ExtendedInfo'], indent=4, \
                                                                                sort_keys=True))
                except Exception as excp:
                    sys.stderr.write("A response error occurred, unable to access iLO Extended "\
                                 "Message Info...")
            elif resp.status != 200 and resp.status != 204:  # 204 is returned by DMTF Redfish simulator
                sys.stderr.write("An http response of \'%s\' was returned.\n" % resp.status)
            else:
                print("Success!")
                #print(json.dumps(resp.dict, indent=4, sort_keys=True))
                # Uncomment the following line if you test against a real physical server
                #time.sleep(10) #going to wait 10 seconds before obtaining the LED indicator state

                # ToDo: Better error handling
                sys.stdout.write("Updated Indicator LED Status for chassis \'%s\': \'%s\'\n\n\n" % \
                        ( _redfishobj.get(chassis.obj['@odata.id']).dict['Id'], \
                        _redfishobj.get(chassis.obj['@odata.id']).dict['IndicatorLED']))

if __name__ == "__main__":
    module = AnsibleModule(
        argument_spec = dict(
            url      = dict(required=True, type='str'),
            session_key   = dict(required=True, type='str')
        )
    )
    # Set variables based on vars fed from .yml
    SYSTEM_URL = module.params['url']
    SESSION_KEY = module.params['session_key']

    # flag to force disable resource directory. Resource directory and associated operations are
    # intended for HPE servers.
    DISABLE_RESOURCE_DIR = False
    
    # Starting with version 3.2.2 of the HPE python-redfish-library,
    # RedfishClient requires a ca_cert_data parameter
    ca_cert_data = {}
    #ca_cert_data["cert_file"] = "c:\\test\\ppcacuser.crt"
    #ca_cert_data["key_file"] = "c:\\test\\ppcacuserpriv.key"
    #ca_cert_data["key_password"] = "password"

    try:
        # Create a Redfish client object using a Session Authentication Token
        REDFISHOBJ = RedfishClient(base_url=SYSTEM_URL, session_key=SESSION_KEY, ca_cert_data=ca_cert_data)
                                                                            
        # Login with the Redfish client
        if not ca_cert_data:
            REDFISHOBJ.login()
        else:
            REDFISHOBJ.login(auth='certificate')
    except ServerDownOrUnreachableError as excp:
        sys.stderr.write("ERROR: server not reachable or does not support RedFish.\n")
        sys.exit()

    set_uid_light(REDFISHOBJ)   # ToDo: better error handling 
    REDFISHOBJ.logout()
    module.exit_json(changed=True)
