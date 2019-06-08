#!/bin/bash

# Código
opcao=1

  while [ $opcao > "0" ];
  do
    echo "Selecione uma opção:"
    echo "0 - Sair"
    echo "1 - GET_INFO: Recupera todas as informações"
    echo "2 - GET_INFO/id_info: Recupera as informações do id escolhido"
    echo "3 - POST_INFO: Adiciona informações no servidor REST"
    read opcao;
    echo ""

    case $opcao in
      "0")
        break
      ;;
      "1")
        # código do curl do get
        curl -i 172.17.0.1:5000/GET_INFO
      ;;
      "2")
        # ...
        echo "Informe o id da informação"
        read id
        curl -i 172.17.0.1:5000/GET_INFO/$id
      ;;
      "3")
        gnome-terminal -- bash -c 'sudo docker stats > saida.txt'
        cat saida.txt
        curl -i -H "Content-Type: application/json" -X POST -d '{}' 172.17.0.1:5000/POST_INFO
      ;;
    esac
    echo ""
done
