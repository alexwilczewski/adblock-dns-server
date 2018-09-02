#!/bin/sh

groupmod --gid $BINDGID named
usermod --uid $BINDUID named

chown named:named /etc/bind/*
chmod 644 /etc/bind/*

exec named -g
