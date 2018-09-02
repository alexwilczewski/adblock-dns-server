FROM alpine:3.8

RUN apk add --no-cache bind
RUN apk add --no-cache shadow

COPY start.sh /usr/local/bin/start.sh
RUN chmod a+x /usr/local/bin/start.sh

EXPOSE 53

CMD ["/usr/local/bin/start.sh"]
