#!/bin/sh

for i in prometheus nx-osv9000-1 nx-osv9000-2 nx-osv9000-3 nx-osv9000-4; do
    docker ps -a | grep -q ${i}
    if [ "$?" == "0" ]; then
        echo -n "Stopping "; docker stop ${i}
        echo -n "Removing "; docker rm ${i}
    fi
done
