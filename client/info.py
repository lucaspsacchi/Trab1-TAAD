import docker
import socket

client = docker.from_env()

# Funcao auxiliar do post
def post(name):
  # container = An object for managing containers on the server.
  # get(id_or_name) = Get a container by name or ID
  # stats = Stream statistics for this container. Similar to the docker stats command.
  x = client.containers.get(name).stats()

  # Cria um dicionario chamado aux
  aux = {}
  aux['nome'] = x['name']
  aux['id'] = x['id']
  aux['id_container'] = name


  return json.dumps(aux)
