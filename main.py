#!python3
from datetime import datetime

import settings
from domain_utils.crawler import Crawler
from domain_utils.blacklist_writer import BlacklistWriter
from domain_utils.nullzone_writer import NullzoneWriter


def create_null_zone():
    output_path = settings.NULLZONE_FILEPATH
    fqdn = settings.FQDN
    ipv4 = settings.IPV4
    ipv6 = settings.IPV6
    domain_parts = fqdn.split('.')

    # set blacklist server ip
    host = domain_parts[0]
    del domain_parts[0]
    if len(domain_parts) == 0:
        domain = 'example.com'
    else:
        domain = '.'.join(domain_parts)

    nullzone_writer = NullzoneWriter(output_path, ipv4, ipv6, domain, host)
    nullzone_writer.export_to_file()


def get_extra_badlist():
    f = open('extra/extra.txt')
    extra_lines = f.read().split('\n')
    f.close()
    return extra_lines


def update_badlist():
    redirect_ip = settings.IPV4
    output_path = settings.BLACKLIST_FILEPATH
    sources = settings.ADBLOCK_SOURCES

    ad_domain_list = []
    ad_domain_list.extend(get_extra_badlist())

    print(ad_domain_list)
    for source in sources :
        crawler = Crawler(source)
        ad_domain_list.extend(crawler.get_domains())
    ad_domain_list = Crawler.remove_duplicates(ad_domain_list)

    blacklist_writer = BlacklistWriter(ad_domain_list, redirect_ip, output_path)
    blacklist_writer.export_to_file()


if __name__ == '__main__':
    create_null_zone()
    update_badlist()
