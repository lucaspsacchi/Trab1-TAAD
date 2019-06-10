import json
import docker
import socket
import requests

# Variaveis global
opcao = int(1)
name = socket.gethostname() # Pega o "local host name"
client = docker.from_env()

while (opcao > 0):
  print("Selecione uma opcao:")
  print("0 - Sair")
  print("1 - GET_INFO: Recupera todas as informacoes")
  print("2 - GET_INFO/id_info: Recupera as informacoes do id escolhido")
  print("3 - POST_INFO: Adiciona informacoes no servidor REST")
  opcao = int(input())
  print("")

  if opcao == 0:
    break
  elif opcao == 1:
    response = requests.get("http://192.168.50.2:5000/GET_INFO")
    print(json.dumps(response.json()))
  elif opcao == 2:
    print("Informe o id da informacao")
    info = int(input())
    print("")
    response = requests.get("http://192.168.50.2:5000/GET_INFO/" + str(info))
    print(json.dumps(response.json()))
  elif opcao == 3:
    # Pega as informacoes do docker
    aux = post()
    response = requests.post("http://192.168.50.2:5000/POST_INFO", data={'id': aux['id'], 'nome': aux['nome']})
    if response:
      print("Informacoes inseridas com sucesso!")
  else:
    print("Selecione outra opcao")

  print("")

# Funcao auxiliar do post
def post():
  # container = An object for managing containers on the server.
  # get(id_or_name) = Get a container by name or ID
  aux = {}

  x = client.container.get(name).stats()
  aux['nome'] = x['name']
  aux['id'] = x['id']

  return json.dumps(aux)
