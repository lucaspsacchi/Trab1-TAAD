FROM ubuntu

COPY . /client

WORKDIR /client

RUN apt-get update && apt-get install -y \
    python-pip
RUN pip install docker
RUN pip install Flask

CMD [ "python", "./interface.py" ]
