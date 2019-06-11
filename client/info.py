import docker
import json
from flask import Flask

client = docker.from_env()

app = Flask(__name__)

@app.route('/<string:id_container>', methods=['GET'])
def post(id_container):
  # container = An object for managing containers on the server.
  # get(id_or_name) = Get a container by name or ID
  # stats = Stream statistics for this container. Similar to the docker stats command.
  x = client.containers.get(id_container).stats(stream=False)
  # Cria um dicionario chamado aux
  aux = {}
  aux['nome'] = x['name']
  aux['id'] = x['id']
  aux['id_container'] = id_container

  return str(aux)

if __name__ == '__main__':
    app.run(host='192.168.50.3', port=5000) # IP DO WORKER
