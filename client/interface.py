# -*- coding: utf-8 -*-

import json
import socket
import requests

# Variaveis global
opcao = int(1)
id_container = socket.gethostname() # Pega o "local host name" que eh o id do container


# Interface
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
    response = requests.get("http://192.168.50.3:5001/" + str(id_container))
    # Passa os dados obtidos para o metodo post do server
    print("response: " + str(response.content))
    response = requests.post("http://192.168.50.2:5000/POST_INFO", json=response.content)
    if response:
      print("Informacoes inseridas com sucesso!")
  else:
    print("Selecione outra opcao")

  print("")
