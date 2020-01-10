#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

# http://python-future.org/quickstart.html
from __future__ import absolute_import, division, print_function

__author__ = "Timothy E Miller, PhD <timmil@cisco.com>"
__contributors__ = [
]
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


# 
# Setup NX-OS switch with required configurations:
# 
#     ! Enable iCAM
#     feature icam
# 
#     ! Set up hourly monitoring for two week
#     icam monitor interval 1 num_intervals 336
# 
#     ! Enable ACL, FIB
#     icam monitor resource acl-tcam module 1 inst 0
#     icam monitor resource fib-tcam module 1 inst 0
#     icam monitor entries acl module 1 inst 0
#     icam monitor scale
#


import requests
import json
import copy
import time

# NX-OS URL and credentials
url='http://127.0.0.1:23456/ins'
switchuser='admin'
switchpassword='admin'

# HTTP Post headers
myheaders={ 'content-type': 'application/json-rpc' }

# Template for the paylod
payload_template = {
    'jsonrpc': '2.0',
    'method': 'cli',
    'params': {
        'cmd': None,
        'version': 1,
    },
    'id': None,
}  

def setup_nxos():
    payload = [] 

    command = copy.deepcopy(payload_template)
    command['params']['cmd'] = 'feature icam'
    command['id'] = 1
    payload.append(command)

    command = copy.deepcopy(payload_template)
    command['params']['cmd'] = 'icam monitor interval 1 num_intervals 336'
    command['id'] = 2
    payload.append(command)

    command = copy.deepcopy(payload_template)
    command['params']['cmd'] = 'icam monitor resource acl-tcam module 1 inst 0'
    command['id'] = 3
    payload.append(command)

    command = copy.deepcopy(payload_template)
    command['params']['cmd'] = 'icam monitor resource fib-tcam module 1 inst 0'
    command['id'] = 4
    payload.append(command)

    command = copy.deepcopy(payload_template)
    command['params']['cmd'] = 'icam monitor entries acl module 1 inst 0'
    command['id'] = 5
    payload.append(command)

    command = copy.deepcopy(payload_template)
    command['params']['cmd'] = 'icam monitor scale'
    command['id'] = 6
    payload.append(command)

    command = copy.deepcopy(payload_template)
    command['params']['cmd'] = 'copy run start'
    command['id'] = 7
    payload.append(command)

    # Post our set of commands (one) to the NXAPI web server
    response_raw = requests.post(url,
                                 data=json.dumps( payload ), 
                                 headers=myheaders,
                                 auth=(switchuser,switchpassword)
                                 )

if __name__ == '__main__':
    setup_nxos()

