#!/usr/bin/env python3
from datetime import datetime

import settings
from domain_utils.host_crawler import HostCrawler
from domain_utils.blacklist_writer import BlacklistWriter
from domain_utils.nullzone_writer import NullzoneWriter


def create_null_zone():
    output_path = settings.NULLZONE_FILEPATH
    host = settings.HOST
    domain = settings.DOMAIN
    ipv4 = settings.IPV4
    ipv6 = settings.IPV6

    nullzone_writer = NullzoneWriter(output_path, ipv4, ipv6, domain, host)
    nullzone_writer.export_to_file()


def update_badlist():
    redirect_ip = settings.IPV4
    output_path = settings.BLACKLIST_FILEPATH
    sources = settings.ADBLOCK_SOURCES

    ad_domain_list = []
    for source in sources :
        crawler = HostCrawler(source)
        ad_domain_list.extend(crawler.get_domains())
    ad_domain_list = HostCrawler.remove_duplicates(ad_domain_list)

    ad_domain_list = get_filter_out_whitelist(ad_domain_list)

    blacklist_writer = BlacklistWriter(ad_domain_list, redirect_ip, output_path)
    blacklist_writer.export_to_file()

def get_filter_out_whitelist(ad_domain_list):
    whitelist_path = settings.WHITELIST_FILEPATH

    openfile = open(whitelist_path)
    whitelist_content = openfile.read()
    openfile.close()

    whitelist_domains = whitelist_content.split('\n')

    return list(set(ad_domain_list) - set(whitelist_domains))


if __name__ == '__main__':
    create_null_zone()
    update_badlist()
