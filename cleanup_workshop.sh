#!/bin/bash

pushd 00-n9kv
vagrant destroy --force
popd

pushd 02-collect
bash cleanup_module2.sh
popd

pushd 03-visualize
bash cleanup_module3.sh
popd

for i in collect visualize; do
    docker rmi ${i}:latest
    docker rmi ${i}:1
done
