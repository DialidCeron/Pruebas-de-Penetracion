#!/bin/bash

if [ "$5" == "" ]
then
	echo "Sintaxis invalida."
    echo "Sintaxis: ./serveremail.sh objetivo puerto --VRFY --file lista_usuarios"
    echo "Sintaxis: ./serveremail.sh objetivo puerto --RCPT --file lista_usuarios"
else 
	if [ "$3" == "--VRFY" ]
	then
		cp $5 vrfy
		sed -i -e 's/^/VRFY /' vrfy 
		cat vrfy | nc -w 1 $1 $2 > salida
		cat salida | grep 252 | cut -d " " -f 3 > usuarios_encontrados
		echo "Se genero el archivo usuarios_encontrados"
	else
		if [ "$3" == "--RCPT" ]
		then
			cp $5 rcpt
			sed -i -e 's/^/RCPT TO:/' rcpt 
			sed -i -e '1s/^/MAIL FROM: dialid@cert.unam.mx\n/' rcpt
			cat rcpt | nc -w 1 $1 $2 > salida
			cat salida | tail +3 > tmp
			paste usuarios tmp | grep 250 | tr -s " " | cut -d " " -f 1 | sed 's/250/ /' > usuarios_encontrados
			echo "Se genero el archivo usuarios_encontrados"
		else
			echo "Sintaxis invalida."
    		echo "Sintaxis: ./serveremail.sh objetivo puerto --VRFY --file lista_usuarios"
    		echo "Sintaxis: ./serveremail.sh objetivo puerto --RCPT --file lista_usuarios"
    	fi
	fi
fi