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
import time

# Add NX-API connection
import connection

# Add Prometheus Client
import prometheus_client

# How often to poll switch in seconds (should match collection frequency)
sleep_interval = 5

ipv4_host_routes = prometheus_client.Gauge(
                    'icam_fib_tcam_ipv4_host_routes',
                    'FIB TCAM for IPv4 Host Routes'
                    )
ipv4_routes = prometheus_client.Gauge(
                    'icam_fib_tcam_ipv4_routes',
                    'FIB TCAM for IPv4 Routes'
                    )
ipv4_lpm_routes = prometheus_client.Gauge(
                    'icam_fib_tcam_ipv4_lpm_routes',
                    'FIB TCAM for IPv4 LPM Routes'
                    )


# Python function to generate the metric
def generate(switch):
    payload = switch.payload('show icam resource fib-tcam module 1 inst 0')
    response = switch.post(payload)

    # Pointer reference to "top of tree" for our relevant info (PEP8 2-steps)
    nxapi_result = response['result']['body']
    table_data = nxapi_result['TABLE_fib_resource']['ROW_fib_resource']

    # List element 0 = ipv4 host routes
    ipv4_host_routes.set(
       float(table_data[0]['TABLE_fib_stats']['ROW_fib_stats']['Used_Entries'])
    )

    # List element 1 = ipv4 routes
    ipv4_routes.set(
       float(table_data[1]['TABLE_fib_stats']['ROW_fib_stats']['Used_Entries'])
    )

    # List element 2 = ipv4 LPM routes
    ipv4_lpm_routes.set(
       float(table_data[2]['TABLE_fib_stats']['ROW_fib_stats']['Used_Entries'])
    )


# The Python section executed when run as the "main" script (i.e. via CLI)
if __name__ == '__main__':

    # For this module, abstract out all the connection, post, and response
    # processing related to nxapi into a 'connection' class
    switch = connection.nxapi(
        host='host.docker.internal', port='23456',
        username='admin', password='admin'
    )

    # Start the Prometheus client listening on port 8888
    prometheus_client.start_http_server(8888)

    # For 02-collect module, this is an infinite loop
    while True:
        # Trigger generation and collection preparation
        generate(switch)

        # Sleep until the next interval
        time.sleep(sleep_interval)
