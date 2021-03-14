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

# Ansible Module derived from https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/set_uid_light.py

# Version 0.118

# -*- coding: utf-8 -*-
"""
Didactic example of an Ansible Redfish module for getting the UID light of a computer chassis
and its enclosure (if any) using the HPE python-ilorest-library and a session key (i.e. OneView token)
"""

import sys
import json
import time
from redfish import RedfishClient   # RedfishClient is in the HPE's redfish class of the python-ilorest-library
from redfish.rest.v1 import ServerDownOrUnreachableError
from ansible.module_utils.basic import *

# The following get_resource_directory module comes from 
# https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/get_resource_directory.py
# It has been included in your `library` directory to show how to speed up the crawling of 
# HPE iLO Redfish implementation
from get_resource_directory import get_resource_directory 

def get_uid_light(_redfishobj):

    ChassisLEDValues = dict()
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
        for instance in resource_instances:                         # instance = Redfish data type
            if '#Chassis.' in instance['@odata.type']:              # if data type/instance is a Chassis
                chassis_members_uri.append( instance['@odata.id'] ) # Append chassis location to list
                chassis_members_response.append( \
                        _redfishobj.get(chassis_members_uri[-1]) )  # Retrieve/append chassis properties to list

    if chassis_members_response and chassis_members_uri:
        for chassis in chassis_members_response:                     
           ChassisLEDValues[str(chassis.obj['@odata.id'])] = chassis.obj['IndicatorLED']

    if ChassisLEDValues:
        return ChassisLEDValues    

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
