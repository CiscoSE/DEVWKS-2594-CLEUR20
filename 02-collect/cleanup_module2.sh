#!/bin/sh

for i in collector prometheus; do
    docker ps -a | grep -q ${i}
    if [ "$?" == "0" ]; then
        echo -n "Stopping "; docker stop ${i}
        echo -n "Removing "; docker rm ${i}
    fi
done
