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


import copy

# Declare list of supported messaging types and command types
supported_messages = ('json-rpc')
supported_command_types = {
    'json-rpc': ['cli', 'cli_ascii'],
    }

supported_headers = {
    'post': {
        'json-rpc': {'content-type': 'application/json-rpc'},
    },
}

valid_rollbacks = ['stop-on-error', 'rollback-on-error', 'continue-on-error']


class invalidType(Exception):
    """
    Generic exception to throw when an invalid message or command type is used.
    """
    pass


class json_rpc:
    """
    Class for the JSON-RPC 2.0 standard for Remote Procedure Calls that
    are encoded within JSON formatting.

    JSON-RPC Standard - http://www.jsonrpc.org/specification
    Server implementation - https://github.com/pavlov99/json-rpc

    """

    def __init__(self, method=None, cmd=None):
        self._messages = 'json-rpc'
        self._version = '2.0'
        self._method = None
        self._commands = []
        self._error = 'stop-on-error'
        self._rollback = []

        self._set_method(method=method)
        self.add_command(command=cmd)

    def _set_method(self, method=None):
        if method not in supported_command_types[self._messages]:
            message = 'Unsupported command type {0}'.format(method)
            message = '{0} for {1}'.format(message, self._messages)
            raise invalidType(message)

        self._method = method

    def add_command(self, command=None, rollback=None):
        if not command:
            return

        self._commands.append(command)

        if not rollback:
            self._rollback.append(self._error)
        else:
            if rollback not in valid_rollbacks:
                raise invalidType('Rollback: {0}'.format(rollback))
            self._rollback.append(rollback)

    def _get_template(self):
        """
        Template generator
        """

        return {
            'jsonrpc': '2.0',
            'method': self._method,
            'params': {
                'cmd': None,
                'version': 1,
            },
            'id': None,
        }

    def post_input(self):
        template = self._get_template()
        commands = []

        for id, cmd in enumerate(self._commands):
            template['params']['cmd'] = cmd
            template['id'] = id + 1
            template['rollback'] = self._rollback[id]

            commands.append(copy.deepcopy(template))

        return commands

    def post_header(self):
        return supported_headers['post']['json-rpc']

    # Change default behavior for errors
    def skip_errors(self):
        self._error = 'continue-on-error'

    # Change default behavior for errors
    def rollback_errors(self):
        self._error = 'rollback-on-error'

    def halt_errors(self):
        self._error = 'stop-on-error'
