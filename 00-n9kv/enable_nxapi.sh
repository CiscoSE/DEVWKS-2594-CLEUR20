#!/usr/bin/env bash

vagrant status > /dev/null
if [ "$?" -ne 0 ]; then
   echo "Vagrant status not clean"
   exit 1
fi

printf "conf t\nfeature nxapi\nend" | vagrant ssh
printf "conf t\nnxapi http port 80\nend" | vagrant ssh
printf "conf t\nboot nxos bootflash:nxos.9.3.3.bin\nend" | vagrant ssh
printf "conf t\ncopy run start\nexit" | vagrant ssh

