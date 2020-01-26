# DEVWKS-2594-CLEUR20

Cisco Live Barcelona 2020 DevNet Workshop 2594 : Leveraging NX-APIs
for Customized Operational Analytics

This repository represents all the example code for the session.

## How to navigate the repository

Each phase of the workshop is laid out in order via the 0n-NAME
directories.  You'll need to enter each directory and follow the
instructions in the respective README.md files.

Prior to beginning the workshop for the very first time, you'll need
to run the following setup steps (on the workshop laptops):

'''bash
cd ${HOME}/Documents/DEVWKS-2594
git pull
bash setup_python.sh
source venv/bin/activate
'''

## Tested Software and Appliance Versions

- Nexus 9000v : The Nexus 9300v "ToR" image, version 9.3(3)
- Python : 3.7.4 (module requirements listed in **requirements.txt**)
- Ansible : 2.9.4
- DevNet Sandbox "Open NX-OS with Nexus 9Kv on VIRL" : 9.2.1
