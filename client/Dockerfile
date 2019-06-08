FROM ubuntu

COPY . /client

WORKDIR /client

RUN apt-get update && apt-get install -y \
curl

CMD [ "bash", "./interface.sh" ]
