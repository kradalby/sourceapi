FROM alpine:3.4

MAINTAINER Kristoffer Dalby

EXPOSE 8080

ENV DIR=/srv/app

RUN apk update
RUN apk add postgresql-dev \
        mailcap \
        build-base \
        python3-dev \
        jpeg-dev \
        zlib-dev \
        python3 \
        linux-headers \
        git \
        pcre-dev

ENV LIBRARY_PATH=/lib:/usr/lib

WORKDIR $DIR

COPY . $DIR

RUN python3 -m pip install pip -U

RUN pip3 install -r requirements/production.txt --upgrade

RUN apk del postgresql-dev \
        build-base \
        python3-dev \
        jpeg-dev \
        zlib-dev \
        linux-headers \
        pcre-dev

ENTRYPOINT ["/srv/app/docker-entrypoint.sh"]
