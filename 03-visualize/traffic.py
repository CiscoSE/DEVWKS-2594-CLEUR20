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


# Core Python Modules
from multiprocessing import Process

# Local modules
import connection


def traffic(switch, source, destination, size):
    nxapi = connection.nxapi(
        host=switch, port=80,
        username='cisco', password='cisco'
    )

    command = 'ping {0} source {1} count unlimited interval 1 packet-size {2}'
    command = command.format(destination, source, size)

    # Call the ping, NXAPI will timeout the connection, simply restart
    while(True):
        payload = nxapi.payload(command)

        try:
            response = nxapi.post(payload)
        except Exception:
            pass

    return response


if __name__ == '__main__':
    flows = [
        ('172.16.30.101', '192.168.0.1', '192.168.12.2', '100'),
        ('172.16.30.102', '192.168.0.2', '192.168.22.2', '200'),
        ('172.16.30.103', '192.168.1.1', '192.168.11.1', '300'),
        ('172.16.30.104', '192.168.1.2', '192.168.22.1', '400'),
    ]
    switch = []
    for i, flow in enumerate(flows):
        switch.append(
            Process(target=traffic, args=flow).start()
        )
