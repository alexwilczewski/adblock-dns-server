FROM alpine:3.8

RUN apk add --no-cache bind shadow python3
RUN pip3 install requests

COPY commands /usr/local/lib
RUN chmod a+x /usr/local/lib/update/update.sh \
    && ln -s /usr/local/lib/update/update.sh /usr/local/bin/update

COPY start.sh /usr/local/bin/start.sh
RUN chmod a+x /usr/local/bin/start.sh

EXPOSE 53

CMD ["/usr/local/bin/start.sh"]
