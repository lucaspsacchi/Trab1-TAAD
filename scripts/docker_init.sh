# Atualização padrão
sudo apt update
sudo apt -y upgrade

# Clona a pasta do git que tem os script de client/server
git clone https://github.com/lucaspsacchi/Trab1-TAAD.git


# Baixando o docker e docker swarn
apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
apt-key fingerprint 0EBFCD88
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt update
apt -y install docker-ce docker-ce-cli containerd.io
systemctl start docker
systemctl enable docker

# gpasswd -a "${USER}" docker
