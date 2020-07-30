#!/bin/bash
#Ceron Rodriguez Lezly Dialid
#Script para instalar OpenVas en KAli 2020

echo "Instalacion de OpenVas"
echo "Actualizando sistema"
sudo apt-get update
echo "Instalando OpenVas"
sudo apt-get install openvas -y
echo "Actualizando OpenVas"
sudo openvas-setup
echo "Es necesario guardar la password generada en un lugar seguro"
echo "Iniciando OpenVas"
sudo openvas-start
echo "Para continuar ingrese en el navegador a https://127.0.0.1:9392"