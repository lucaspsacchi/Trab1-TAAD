import docker
import socket

name = socket.gethostname() # Pega o "local host name"

client = docker.from_env()

def post():
  # container = An object for managing containers on the server.
  # get(id_or_name) = Get a container by name or ID
  aux = {}

  x = client.container.get(name).stats()
  aux['nome'] = x['name']
  aux['id'] = x['id']

  return json.dumps(aux)

