FROM ubuntu

COPY . /client

WORKDIR /client

RUN apt install python3-pip

CMD [ "python3", "./interface.py" ]
