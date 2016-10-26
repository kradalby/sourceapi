FROM python:3.5.2

MAINTAINER Kristoffer Dalby


ENV NAME=sourceapi

ENV DIR=/srv/app

RUN mkdir $DIR
WORKDIR $DIR

# Install requirements
COPY ./requirements $DIR/requirements
RUN pip install -r requirements/production.txt --upgrade

# Copy project files
COPY . $DIR

EXPOSE 8080
EXPOSE 8081

CMD ["sh", "docker-entrypoint.sh"]
