 # Copyright 2020 Hewlett Packard Enterprise Development LP
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

 # Original python file used to create the companion Ansible Module am_set_uid_light.py
 # Source: https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/set_uid_light.py   
    
 # Version 0.11
    
# -*- coding: utf-8 -*-
"""
Example of an Ansible Redfish module for retrieving the UID light status for iLO 5 fw >= 2.10
(prior to iLO 5 fw 2.10, the IndicatorLED is only in the Systems data type.)
"""

import sys
import json
import time
from redfish import RedfishClient # RedfishClient is in the HPE's redfish class of the python-ilorest-library
from redfish.rest.v1 import ServerDownOrUnreachableError
from ansible.module_utils.basic import *

# The following get_resource_directory module comes from https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/get_resource_directory.py
# It has been included in this infrastructure to show how you can speed up the crawling of 
# HPE iLO Redfish implementation
from get_resource_directory import get_resource_directory

def get_uid_light(_redfishobj):

    ChassisLEDValues = dict()
    chassis_members_uri = None
    chassis_members_response = None

    resource_instances = get_resource_directory(_redfishobj)
    if DISABLE_RESOURCE_DIR or not resource_instances:
        #if we do not have a resource directory or want to force it's non use to find the
        #relevant URI
        
        # Starting at iLO 5 fw 2.10, IndicatorLEDs are in the Chassis data type (as well as in the Systems data type)
        chassis_uri = _redfishobj.root.obj['Chassis']['@odata.id']
        chassis_response = _redfishobj.get(chassis_uri)
        iterator = iter(chassis_response.obj['Members'])
        
        # TBD: the following is Work in Progress
        chassis_toto_uri = next(iterator)['@odata.id']
        print("Chassis toto URIs: \'%s\'\n" % str(chassis_toto_uri))
        
        chassis_members_uri = next(iter(chassis_response.obj['Members']))['@odata.id']
        #print ("Chassis members URIs: \'%s\'\n" % str(chassis_members_uri))
        chassis_members_response = _redfishobj.get(chassis_members_uri)
        
    else:
        #Use Resource directory to find the relevant URI
        for instance in resource_instances:
            if '#Chassis.' in instance['@odata.type']:
                chassis_members_uri = instance['@odata.id']
                #print("Chassis Member URI: \'%s\'" % str(chassis_members_uri))
                chassis_members_response = _redfishobj.get(chassis_members_uri)
                if chassis_members_response and chassis_members_uri:
                    ChassisLEDValues[str(chassis_members_uri)] = chassis_members_response.dict.get("IndicatorLED")
                    #print("\tCurrent Indicator LED Status: \'%s\'\n" % ChassisLEDValues[str(chassis_members_uri)])
                                            

    if ChassisLEDValues:
        return ChassisLEDValues    
        
    

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
    DISABLE_RESOURCE_DIR = True

    try:
        # Create a Redfish client object using a Session Authentication Token
        REDFISHOBJ = RedfishClient(base_url=SYSTEM_URL, session_key=SESSION_KEY)
        
        # Login with the Redfish client
        REDFISHOBJ.login()
    except ServerDownOrUnreachableError as excp:
        sys.stderr.write("ERROR: server not reachable or does not support RedFish.\n")
        sys.exit()

    ChassisLEDValues=get_uid_light(REDFISHOBJ)
    REDFISHOBJ.logout()
    module.exit_json(changed=False, ChassisLEDValues=ChassisLEDValues )
