FROM ubuntu

COPY . /server

WORKDIR /server

RUN apt-get update && apt-get install -y \
    python-pip
RUN pip install -r requirements.txt

CMD [ "python", "./server.py" ]
