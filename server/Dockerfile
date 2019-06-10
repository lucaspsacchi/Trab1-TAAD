FROM ubuntu

COPY . /server

WORKDIR /server

RUN apt install python-pip
RUN pip install -r requirements.txt

CMD [ "python3", "./server.py" ]
