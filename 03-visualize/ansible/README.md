# Ansible Playbook to Initialize Sandbox

## Instructions

For Ansible to work properly, you must have the SSH host keys
for the switches saved in your known_hosts file.  Run the
following script to clear out the old ones and save the new
ones:

    bash collect_sandbox_host_keys.sh

Run the Ansible playbook (don't forget to have your Python 3
environment activated) that will enable http for NX-API and
set the boot variables for us.

    ansible-playbook -i sandbox.yaml setup_sandbox.yaml
