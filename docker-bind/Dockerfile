FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y bind9

COPY start.sh /usr/local/bin/start.sh
RUN chmod a+x /usr/local/bin/start.sh

RUN touch /etc/bind/badlist \
    && touch /etc/bind/null.zone.file

EXPOSE 53

CMD ["/usr/local/bin/start.sh"]
