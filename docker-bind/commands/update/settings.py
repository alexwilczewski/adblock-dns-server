import os
import socket
import sys, shutil


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BLACKLIST_FILEPATH = '/etc/bind/badlist'
NULLZONE_FILEPATH = '/etc/bind/null.zone.file'
WHITELIST_FILEPATH = os.path.abspath('whitelist')

ADBLOCK_SOURCES = [
    'http://adaway.org/hosts.txt',
    'http://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext',
    'http://winhelp2002.mvps.org/hosts.txt',
    'http://hosts-file.net/ad_servers.txt',
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',

    # porn sites to block
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts',
    '/usr/local/lib/update/local_sources/porn_custom.txt',
    '/usr/local/lib/update/local_sources/porn_reddit.txt',
]

HOST = 'dns1'
DOMAIN = 'example.org'
IPV4 = '0.0.0.0'
IPV6 = None
