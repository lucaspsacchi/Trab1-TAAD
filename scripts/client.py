# Variáveis globais
UDP_IP = "127.0.0.1" # IP
port = 0 # Inicialização da variável

# É uma função para enviar as mensagens UDP
def client(msg, port):

    # Codifica a mensagem em ASCII e inclui um \0 no final da string
    info = msg.encode('ascii') + b'\0'

    # Cria o socket UDP
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

   # Envia a mensagem pelo socket para um ip e uma porta destino
    sock.sendto(info, (UDP_IP, port))

