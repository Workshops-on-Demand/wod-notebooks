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

# -*- coding: utf-8 -*-


# Ansible Module derived from https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/set_uid_light.py
# Version 0.114

"""
Didactic example of an Ansible Redfish module for setting the UID light of a computer chassis
and its enclosure (if any) using the HPE python-ilorest-library and
a session key (i.e. OneView token)
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
    chassis_members_uri = None
    chassis_members_response = None

    resource_instances = get_resource_directory(_redfishobj)
    if DISABLE_RESOURCE_DIR or not resource_instances:
        #if we do not have a resource directory or want to force it's non use to find the
        #relevant URI
        # ********* TBD/Work in progress **************
        chassis_uri = _redfishobj.root.obj['Chassis']['@odata.id']
        chassis_response = _redfishobj.get(chassis_uri)
        chassis_members_uri = next(iter(chassis_response.obj['Members']))['@odata.id']
        chassis_members_response = _redfishobj.get(chassis_members_uri)
    else:
        #Use Resource directory to find the relevant URI
        for instance in resource_instances:
            if '#Chassis.' in instance['@odata.type']:
                chassis_members_uri = instance['@odata.id']
                chassis_members_response = _redfishobj.get(chassis_members_uri)
                if chassis_members_response and chassis_members_uri:
                    if "Off" in chassis_members_response.dict.get("IndicatorLED"):
                        body["IndicatorLED"] = "Lit"
                    else:
                        body["IndicatorLED"] = "Off"

                resp = _redfishobj.patch(chassis_members_uri, body)
                #If iLO responds with soemthing outside of 200 or 201 then lets check the iLO extended info
                #error message to see what went wrong
                if resp.status == 400:
                    try:
                        sys.stderr.write(json.dumps(resp.obj['error']['@Message.ExtendedInfo'], indent=4, \
                                                                                sort_keys=True))
                    except Exception as excp:
                        sys.stderr.write("A response error occurred, unable to access iLO Extended "\
                                 "Message Info...")
                elif resp.status != 200:
                        sys.stderr.write("An http response of \'%s\' was returned.\n" % resp.status)
                else:
                    sys.stdout.write("Success!\n")
                    sys.stdout.write(json.dumps(resp.dict, indent=4, sort_keys=True))
                    time.sleep(10) #going to wait 10 seconds before obtaining the LED indicator state
                    sys.stdout.write("\nUpdated Indicator LED Status: \'%s\'\n" % _redfishobj.\
                                                    get(chassis_members_uri).dict['IndicatorLED'])

if __name__ == "__main__":
    module = AnsibleModule(
        argument_spec = dict(
            url      = dict(required=True, type='str'),
            session_key   = dict(required=True, stype='str')
        )
    )
    # Set variables based on vars fed from .yml
    SYSTEM_URL = module.params['url']
    SESSION_KEY = module.params['session_key']

    # flag to force disable resource directory. Resource directory and associated operations are
    # intended for HPE servers.
    DISABLE_RESOURCE_DIR = False

    try:
        # Create a Redfish client object using a Session Authentication Token
        REDFISHOBJ = RedfishClient(base_url=SYSTEM_URL, session_key=SESSION_KEY)
                                                                            
        # Login with the Redfish client
        REDFISHOBJ.login()
    except ServerDownOrUnreachableError as excp:
        sys.stderr.write("ERROR: server not reachable or does not support RedFish.\n")
        sys.exit()

    set_uid_light(REDFISHOBJ)
    REDFISHOBJ.logout()
    module.exit_json(changed=True)
