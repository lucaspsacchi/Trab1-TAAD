# Atualização padrão
sudo apt update
sudo apt -y upgrade

# Clona a pasta do git que tem os script de client/server
git clone https://github.com/lucaspsacchi/Trab1-TAAD.git

# Baixando o docker e docker swarn
sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt -y install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker

# Adiciona a vm como worker no cluster
# chmod +x worker.sh
# sh worker.sh

# Builda a imagem do docker
cd Trab1-TAAD/client
sudo docker build -t client:latest .
