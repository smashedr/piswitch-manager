#!/usr/bin/env bash

set -x

if [[ $(id -u) -ne 0 ]];then
    echo "Please run as root."
    exit 1
fi

apt install -y python3 python3-pip python3-dev
/usr/bin/env python3 -m pip install -r requirements.txt
[[ "$?" != "0" ]] && echo "Fatal error installing requirements.txt" && exit 1

if [[ ! -d /websites/piswitch-manager ]];then
    mkdir -p /websites/piswitch-manager
fi

cp -r ./ /websites/piswitch-manager

# TODO: need to generate a unique settings.env file
if [[ ! -f /websites/piswitch-manager/settings.env ]];then
    cp ./settings.env.example /websites/piswitch-manager/settings.env
fi

if [[ ! -f /etc/systemd/system/piswitch-manager.service ]];then
    cp ./piswitch-manager.service /etc/systemd/system/piswitch-manager.service
    /usr/bin/env systemctl daemon-reload
fi

/usr/bin/env systemctl is-enabled piswitch-manager.service >/dev/null 2>&1
if [[ "$?" != "0" ]];then
    /usr/bin/env systemctl enable piswitch-manager.service
fi

/usr/bin/env python3 /websites/piswitch-manager/manage.py makemigrations
[[ "$?" != "0" ]] && echo "Fatal error running makemigrations" && exit 1
/usr/bin/env python3 /websites/piswitch-manager/manage.py migrate
[[ "$?" != "0" ]] && echo "Fatal error running migrate" && exit 1
/usr/bin/env python3 /websites/piswitch-manager/manage.py clearsessions
[[ "$?" != "0" ]] && echo "Fatal error running clearsessions" && exit 1

echo "Setup was successful. The service will start on reboot."
