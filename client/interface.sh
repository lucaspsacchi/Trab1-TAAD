#!/bin/bash
  opcao=-1

  while [ $opcao != "0" ];
  do
    echo "Selecione uma opção:"
    echo "0 - Sair"
    echo "1 - GET_INFO: Recupera todas as informações"
    echo "2 - GET_INFO/id_info: Recupera as informações do id escolhido"
    echo "3 - POST_INFO: Adiciona informações no servidor REST"
    read opcao;
    echo ""

    case $opcao in
      "1")
        # código do curl do get
        echo "Escolheu o 1"
      ;;
      "2")
        # ...
        echo "Escolheu o 2"
      ;;
      "3")
        echo "Escolheu o 3"
      ;;
    esac
    echo ""
done
