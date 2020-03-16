#! /bin/bash

mount -o remount,rw /

cp dataserver /etc/init.d/

chmod +x /etc/init.d/dataserver

update-rc.d dataserver defaults

if [ -f /etc/rc2.d/S20dataserver ]; then
        echo "Rename file in rc2.d"
        mv /etc/rc2.d/S20dataserver /etc/rc2.d/S99dataserver
fi
