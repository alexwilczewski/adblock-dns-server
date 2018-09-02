#!/bin/sh

sudo docker run --rm -it \
    -v "`pwd`/../files/named.conf.local:/etc/bind/named.conf.local" \
    -v "`pwd`/../files/named.conf.options:/etc/bind/named.conf.options" \
    -v "`pwd`/../files/badlist:/etc/bind/badlist" \
    -v "`pwd`/../files/null.zone.file:/etc/bind/null.zone.file" \
    -p "53:53" -p "53:53/udp" \
    -e "BINDUID=`id -u`" \
    -e "BINDGID=`id -g`" \
    adblock/bind:latest \
    /bin/bash
