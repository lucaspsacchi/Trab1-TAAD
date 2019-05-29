# Variáveis globais
UDP_IP = "127.0.0.1" # IP
port = 0 # Inicialização da variável

# É uma função para receber as mensagens UDP
def server(port):

    # Cria socket UDP
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, port))

    while True:
        # Define o tamanho máximo da mensagem
        info, addr = sock.recvfrom(1024) # Tamanho do buffer é de 1024 bytes

        while info[-1:] == '\0':
            info = info[:-1]

        # Decodifica a mensagem em ASCII
        msg = info.decode('ascii')


