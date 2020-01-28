# Ansible Playbook to Initialize Sandbox

## Initial Sandbox Setup

For Ansible to work properly, you must have the SSH host keys
for the switches saved in your known_hosts file.  Run the
following script to clear out the old ones and save the new
ones:

```bash
    bash collect_sandbox_host_keys.sh
```

Run the Ansible playbook (don't forget to have your Python 3
environment activated) that will enable http for NX-API and
set the boot variables for us.

```bash
    ansible-playbook setup_sandbox.yaml
```

## Sandbox VXLAN EVPN Setup

There is nothing in these modules that require VLXAN EVPN. It just happens to
be a specialty of mine and I have Ansible for it. Now, you have Ansible for most
of the setup/configuration.

The commands we are converting to metrics are not VXLAN specific either so you
can use them for traditional ethernet designs.

## Usage

To build the VXLAN EVPN fabric in the DevNet Sandbox, first establish the VPN
to the sandbox.  Then run this command:

```bash
ansible-playbook vxlan.yml
```

## Repo Notes

This module was developed and tested with Ansible 2.9, leveraging the *network_cli*
connection methodology.

The Ansible configuration file changes the default inventory file to be the
included **sandbox.yaml** file. If you have errors indicating no hosts found
or issues that seem like it doesn't know about the sandbox inventory, you can
manually specify the inventory file via:

```bash
ansible-playbook -i sandbox.yaml playbook.yaml
```

## Requirements

- Python 3.6 : Python modules [requirements](../../requirements.txt)
- Ansible 2.9
