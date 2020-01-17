# DEVWKS-2594: 01-generate

Simple Python script to query the NXAPI and generate metrics
that will be collected by another phase.

## Outcomes

- Demonstrate use of the requests module
- Examples of navigating returned data structure

## Pre-requisites

- [Vagrant Box Instructions](../../n9kv/README.md)
  - Must have Nexus 9000v Vagrant box running
  - Must have iCAM enabled via *setup_nxos.py* script

## Network Communication Diagram

![Network Diagram](images/Step01-Network-Communication.png)

## How to use

    python generate.py

