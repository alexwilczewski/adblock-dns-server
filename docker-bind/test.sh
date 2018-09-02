#!/bin/sh

sudo docker run --rm -it \
    -v "`pwd`/../bind:/etc/bind" \
    -p "53:53" -p "53:53/udp" \
    -e "BINDUID=`id -u`" \
    -e "BINDGID=`id -g`" \
    adblock/bind:latest \
    /bin/sh
