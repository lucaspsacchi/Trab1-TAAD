FROM ubuntu

COPY . /client

WORKDIR /client

RUN apt-get update && apt-get install -y \
    python-pip
RUN pip install docker

CMD [ "python", "./interface.py" ]
