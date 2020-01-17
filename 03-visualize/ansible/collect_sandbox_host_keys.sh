#!/bin/bash
#
#  Brute force collection of SSH host keys from Sandbox.
#
#  More elegant approach (root level, overwrites entire file):
#  https://blog.ipspace.net/2017/09/collect-ssh-keys-with-ansible.html
#

/usr/bin/sed -i -e 's/172.16.30.*//' ${HOME}/.ssh/known_hosts

for i in 101 102 103 104; do \
   ssh-keyscan 172.16.30.${i} 2>/dev/null >> ${HOME}/.ssh/known_hosts; \
done

