#!/bin/sh

sudo docker run --rm -d \
    --name adblockdns \
    -v "`pwd`/bind:/etc/bind" \
    -p "53:53" -p "53:53/udp" \
    -e "BINDUID=`id -u`" \
    -e "BINDGID=`id -g`" \
    adblock/bind:latest
