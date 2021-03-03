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
 
 # Version 0.1

# -*- coding: utf-8 -*-
"""
An example of modifying the Ignore property of a security parameter.
This modification will appear in the Security Dashboard of the 
iLO Graphical User Interface.
"""
DOCUMENTATION = '''
---
module: set_ignore_security_param
short_description: This module sets the Ignore property of the supplied security parameter.
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

# Supply exact Security Parameter Name
- name: Ignore 'Password Complexity'
  set_ignore_security_param:
      ilo_ip: "{{ inventory_hostname }}:{{ ansible_port }}"
      session_key: "{{ token }}"
      security_param_name: "Password Complexity"
      ignore_security_param: True

# Supply only a part of the Security Parameter Name. Respect case!
- name: Ignore 'Secure Boot'
  set_ignore_security_param:
      ilo_ip: "{{ inventory_hostname }}:{{ ansible_port }}"
      session_key: "{{ token }}"
      security_param_name: "Secure"
      ignore_security_param: True


'''

import os
import sys
import json
from redfish import RedfishClient
from redfish.rest.v1 import ServerDownOrUnreachableError
from get_resource_directory import get_resource_directory
# Instantiating module class
from ansible.module_utils.basic import *


def set_ignore_security_param(_redfishobj, ParamName, IGNORE, DISABLE_RESOURCE_DIR):
    security_params_data = {}
    body = { "Ignore": IGNORE } 

    resource_instances = get_resource_directory(_redfishobj)
    if DISABLE_RESOURCE_DIR or not resource_instances:
        print ("\tNot using Resource directory\n")
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
        print ("\tUsing Resource directory\n")
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
        for security_params in security_params_data:
            if ParamName in security_params_data[security_params]['Name']:
                    resp = _redfishobj.patch(security_params_data[security_params]['@odata.id'], body)
                    if resp.status == 400:
                        try:
                            print(json.dumps(resp.obj['error']['@Message.ExtendedInfo'], indent=4, \
                                                                                sort_keys=True))
                        except Exception as excp:
                            sys.stderr.write("A response error occurred, unable to access iLO Extended "\
                                 "Message Info...")
                    elif resp.status != 200:
                        sys.stderr.write("An http response of \'%s\' was returned.\n" % resp.status)
                    else:
                        print("Success!\n")
                    break


if __name__ == "__main__":

    module = AnsibleModule(
            argument_spec = dict(
                state     = dict(default='present', choices=['present', 'absent']),
                ilo_ip    = dict(required=True, type='str'),
                session_key = dict(required=True, stype='str'),
                security_param_name      = dict(required=True, type='str'),
                ignore_security_param    = dict(required=True, type='bool')))
    SYSTEM_URL = "https://" + module.params['ilo_ip']
    SESSION_KEY = module.params['session_key']
    PARAM_NAME = module.params['security_param_name']
    IGNORE = module.params['ignore_security_param']

    # flag to force disable resource directory. Resource directory and associated operations are
    # intended for HPE servers.
    DISABLE_RESOURCE_DIR = False

    try:
        # Create a Redfish client object
        REDFISHOBJ = RedfishClient(base_url=SYSTEM_URL, session_key=SESSION_KEY)                             
        # Login with the Redfish client
        REDFISHOBJ.login()
    except ServerDownOrUnreachableError as excp:
        sys.stderr.write("ERROR: server not reachable or does not support RedFish.\n")
        sys.exit()

    set_ignore_security_param(REDFISHOBJ, PARAM_NAME, IGNORE, DISABLE_RESOURCE_DIR)
    REDFISHOBJ.logout()
    module.exit_json(changed=True)
