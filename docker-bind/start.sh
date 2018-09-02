#!/bin/sh

groupmod --gid $BINDGID bind
usermod --uid $BINDUID bind

chown bind:bind /etc/bind/*
chmod 644 /etc/bind/*

exec named -g
