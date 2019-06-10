import docker
from flask import Flask

client = docker.from_env()

app = Flask(__name__)

@app.route('/<int: id_container>', methods=['GET'])
def post(name):
  # container = An object for managing containers on the server.
  # get(id_or_name) = Get a container by name or ID
  # stats = Stream statistics for this container. Similar to the docker stats command.
  x = client.containers.get(id_container).stats()

  # Cria um dicionario chamado aux
  aux = {}
  aux['nome'] = x['name']
  aux['id'] = x['id']

  return json.dumps(aux)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
