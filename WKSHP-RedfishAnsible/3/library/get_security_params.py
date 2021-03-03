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
 
 # Version 0.11

# -*- coding: utf-8 -*-
"""
An example for retrieving the iLO security parameters and associated values.
These security parameters are part of the iLO security dashboard.
"""
DOCUMENTATION = '''
---
module: get_security_params
short_description: This module retrieves the security properties of the iLO security dashboard.
'''


EXAMPLES = '''

# List of Security Parameters:
    # "Require Login for iLO RBSU"
    # "Secure Boot"
    # "Password Complexity"
    # "Security Override Switch"
    # "IPMI/DCMI Over LAN"
    # "Minimum Password Length"
    # "Authentication Failure Logging"
    # "Require Host Authentication"
    # "Last Firmware Scan Result"

# 
- name: Get security parameters
  get_security_params:
         ilo_ip: "{{ inventory_hostname }}:{{ ansible_port }}"
         session_key: "{{ token }}"

'''

import os
import sys
import json
from redfish import RedfishClient
from redfish.rest.v1 import ServerDownOrUnreachableError
from get_resource_directory import get_resource_directory
# Instantiating module class
from ansible.module_utils.basic import *


def get_security_params(_redfishobj, DISABLE_RESOURCE_DIR):
    security_params_data = {} 

    resource_instances = get_resource_directory(_redfishobj)
    if DISABLE_RESOURCE_DIR or not resource_instances:
        #if we do not have a resource directory or want to force it's non use to find the
        #relevant URI
        # Retrieve the URIs of all Managers
        managers_uri = _redfishobj.root.obj['Managers']['@odata.id']
        # Retrieve the data of all managers URIs
        managers_response = _redfishobj.get(managers_uri)
        # Retrieve the URIs of all Members of all managers
        managers_members_uri = next(iter(managers_response.obj['Members']))['@odata.id']
        # Retrieve the data of all members of all Managers
        managers_members_response = _redfishobj.get(managers_members_uri)

        # Retrieve the URIs of all the SecurityServices from all Managers Members
        securityservices_uri = managers_members_response.obj.Oem.Hpe.Links\
                ['SecurityService']['@odata.id']

        # Retrieve the data of all SecurityServices URIs
        securityservices_response = _redfishobj.get(securityservices_uri)
        
        # Retrieve the URIs of all the SecurityDashboards
        securitydashboards_uri = securityservices_response.obj.Links\
                ['SecurityDashboard']['@odata.id']
        
        # Retrieve the data of all SecurityDashboard URIs
        securitydashboard_response = _redfishobj.get(securitydashboards_uri)

        # Retrieve the Security Params URIs
        securityparams_uri = securitydashboard_response.obj\
                ['SecurityParameters']['@odata.id']

        # Retrieve the data of all Security Params
        securityparams_response = _redfishobj.get(securityparams_uri)

        # Retrieve the Security Params Members
        SecurityParams = securityparams_response.obj['Members']
        for _security_params in SecurityParams:
            security_params_data[_security_params['@odata.id']] = _redfishobj.\
                                               get(_security_params['@odata.id']).dict

    else:
        for instance in resource_instances:
            #Use Resource directory to find the relevant URI
            if '#HpeiLOSecurityParamCollection.' in instance['@odata.type'] and 'Managers' in \
                                                                        instance['@odata.id']:
                SecurityParams_uri = instance['@odata.id']
                SecurityParams = _redfishobj.get(SecurityParams_uri).obj['Members']
                for _security_params in SecurityParams:
                     security_params_data[_security_params['@odata.id']] = _redfishobj.\
                                                        get(_security_params['@odata.id']).dict
                break

    if security_params_data:
        return security_params_data
        

if __name__ == "__main__":

    module = AnsibleModule(
            argument_spec = dict(
                state     = dict(default='present', choices=['present', 'absent']),
                ilo_ip    = dict(required=True, type='str'),
                session_key = dict(required=True, stype='str')))
    SYSTEM_URL = "https://" + module.params['ilo_ip']
    SESSION_KEY = module.params['session_key']

    # flag to force disable resource directory. Resource directory and associated operations are
    # intended for HPE servers.
    DISABLE_RESOURCE_DIR = True

    try:
        # Create a Redfish client object
        REDFISHOBJ = RedfishClient(base_url=SYSTEM_URL, session_key=SESSION_KEY)                             
        # Login with the Redfish client
        REDFISHOBJ.login()
    except ServerDownOrUnreachableError as excp:
        sys.stderr.write("ERROR: server not reachable or does not support RedFish.\n")
        sys.exit()

    SecurityParams=get_security_params(REDFISHOBJ, DISABLE_RESOURCE_DIR)
    REDFISHOBJ.logout()
    
    module.exit_json(changed=True, SecurityParams=SecurityParams)
