FROM ubuntu:18.04
USER root
RUN apt update
RUN apt-get install nano
RUN apt-get install -y python3-pip
RUN /usr/bin/pip3 install asyncio-nats-client
RUN /usr/bin/pip3 install pymongo
COPY servercli.py /home/
