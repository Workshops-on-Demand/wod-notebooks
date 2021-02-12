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
# Version 0.11

"""
An example of setting the UID light ussing a session key token
"""
DOCUMENTATION = '''
---
module: set_uid_light
short_description: This module sets the UID light on or off
'''

EXAMPLES = '''
- name: set UID light
  become: yes
  set_uid_light:
    name: "Set UID light"
    enabled: True
    uid: True
'''

import sys
import json
import time
from redfish import RedfishClient
from redfish.rest.v1 import ServerDownOrUnreachableError
from ansible.module_utils.basic import *

from get_resource_directory import get_resource_directory

def set_uid_light(_redfishobj):

    body = dict()
    systems_members_uri = None
    systems_members_response = None

    resource_instances = get_resource_directory(_redfishobj)
    if DISABLE_RESOURCE_DIR or not resource_instances:
        #if we do not have a resource directory or want to force it's non use to find the
        #relevant URI
        systems_uri = _redfishobj.root.obj['Systems']['@odata.id']
        systems_response = _redfishobj.get(systems_uri)
        systems_members_uri = next(iter(systems_response.obj['Members']))['@odata.id']
        systems_members_response = _redfishobj.get(systems_members_uri)
    else:
        #Use Resource directory to find the relevant URI
        for instance in resource_instances:
            if '#ComputerSystem.' in instance['@odata.type']:
                systems_members_uri = instance['@odata.id']
                systems_members_response = _redfishobj.get(systems_members_uri)

    if systems_members_response and systems_members_uri:
        print("Current Indicator LED Status: \'%s\'\n" % systems_members_response.dict.\
                                                                            get("IndicatorLED"))
        if "Off" in systems_members_response.dict.get("IndicatorLED"):
            print("Will illuminate indicator LED.\n")
            body["IndicatorLED"] = "Lit"
        else:
            print("Will extinguish indicator LED.\n")
            body["IndicatorLED"] = "Off"

        resp = _redfishobj.patch(systems_members_uri, body)
        #If iLO responds with soemthing outside of 200 or 201 then lets check the iLO extended info
        #error message to see what went wrong
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
            print(json.dumps(resp.dict, indent=4, sort_keys=True))
            time.sleep(10) #going to wait 10 seconds before obtaining the LED indicator state
            sys.stdout.write("\nUpdated Indicator LED Status: \'%s\'\n" % _redfishobj.\
                                                    get(systems_members_uri).dict['IndicatorLED'])

if __name__ == "__main__":
    module = AnsibleModule(
        argument_spec = dict(
            name      = dict(required=True, type='str'),
            enabled   = dict(required=True, type='bool'),
            state     = dict(default='present', choices=['present', 'absent']),
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
        # Create a Redfish client object
        REDFISHOBJ = RedfishClient(base_url=SYSTEM_URL, session_key=SESSION_KEY)
                                                                            
        # Login with the Redfish client
        REDFISHOBJ.login()
    except ServerDownOrUnreachableError as excp:
        sys.stderr.write("ERROR: server not reachable or does not support RedFish.\n")
        sys.exit()

    set_uid_light(REDFISHOBJ)
    REDFISHOBJ.logout()
    module.exit_json(changed=True)
