FROM alpine:3.4

MAINTAINER Kristoffer Dalby

ENV DIR=/srv/app
ENV LIBRARY_PATH=/lib:/usr/lib

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


WORKDIR $DIR

# Install requirements
COPY ./requirements $DIR/requirements
RUN python3 -m pip install pip -U && \
    pip3 install -r requirements/production.txt --upgrade

# Delete unneeded files.
RUN apk del build-base \
        python-dev \
        linux-headers

# Copy project files
COPY . $DIR


EXPOSE 8080

ENTRYPOINT ["/srv/app/docker-entrypoint.sh"]
