#!/bin/bash
clear
echo "Atualizando repositorios do Linux e seus arquivos"
apt update 
# apt upgrade -y
apt install -y curl lftp lsof mc ncdu nmon nmap net-tools openssl tcpdump telnet tree uuid vim wget

#####
clear
if command -v docker &> /dev/null; then
    echo "Docker está instalado!"
else
    echo "Iniciando a instalacao do docker"
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
fi

# echo "%ubuntu    ALL=(ALL) NOPASSWD:ALL" >>/etc/sudoers
