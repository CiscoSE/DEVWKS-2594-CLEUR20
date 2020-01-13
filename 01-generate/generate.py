#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python Template for Cisco Sample Code.

Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""


__author__ = "Timothy E Miller, PhD <timmil@cisco.com>"
__contributors__ = [
]
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


# Import relevant Python modules
import requests
import json
import copy
import time


# Vagrant Nexus 9300v Connection and Credentials
url = 'http://127.0.0.1:23456/ins'
switchuser = 'admin'
switchpassword = 'admin'

# HTTP Post headers
myheaders = {'content-type': 'application/json-rpc'}

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

# How often to poll switch in seconds (should match collection frequency)
sleep_interval = 15


# Python function to generate the metric
def generate():
    # Clone the template
    command = copy.deepcopy(payload_template)

    # Add the required command to the clone
    command['params']['cmd'] = 'show icam resource fib-tcam module 1 inst 0'
    command['id'] = 1

    # Send our commands to the switch (as a list)
    payload = [command]
    response_raw = requests.post(url,
                                 data=json.dumps(payload),
                                 headers=myheaders,
                                 auth=(switchuser, switchpassword)
                                 )

    # Convert response to Python friendly format
    response = response_raw.json()

    # Pointer reference to "top of tree" for our relevant info (PEP8 2-steps)
    nxapi_result = response['result']['body']
    table_data = nxapi_result['TABLE_fib_resource']['ROW_fib_resource']

    return (
        table_data[1]['Class'],
        table_data[1]['TABLE_fib_stats']['ROW_fib_stats']['Used_Entries']
    )


# The Python section executed when run as the "main" script (i.e. via CLI)
if __name__ == '__main__':

    # For the 01-generate section, only loop a few times
    loop = 3
    while loop > 0:
        metric_name, metric_value = generate()

        print(int(time.time()))
        print('{0},{1}'.format(metric_name, metric_value))

        time.sleep(sleep_interval)
        loop = loop - 1
