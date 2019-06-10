FROM ubuntu

COPY . /server

WORKDIR /server

RUN apt install python3-pip
RUN pip3 install -r requirements.txt

CMD [ "python3", "./server.py" ]
