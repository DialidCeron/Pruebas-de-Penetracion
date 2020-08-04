#!/bin/bash

if [ "$1" == "" ]
then
	echo "Sintaxis invalida. Es necesario pasar como argumento un archivo que contenga un nombre de dominio por linea"
        echo "Sintaxis: ./transferencias.sh archivo_dominios"
else
	echo "Lista de dominios con transferencia habilitada: " > transferencias
	while read line; do 
		whois $line | grep 'DNS:\|Name Server:' | tr -s " " | cut -d ":" -f 2 | cut -d " " -f 2 > temp
			while read dom; do
				check=$(dig axfr @$dom $line | grep -c 'Transfer failed.')
				if [[ $check == "0" ]]; then
					echo $line >> transferencias
				fi
			done < temp 
		done < $1
fi
echo "Creado archivo transferencias con lista de dominios cuyo DNS tiene zona de transferencia habilitada"
rm temp


