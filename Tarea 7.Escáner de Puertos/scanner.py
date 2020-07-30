#!/bin/python3

import sys
import socket
from datetime import datetime

#Definir objetivo
if len(sys.argv) == 3:
    target = socket.gethostbyname(sys.argv[1]) #Hostname to IPV4
    ports=sys.argv[2].split('-')

    #Imprimendo un banner
    print("-" *50)
    print("Escaneando objetivo "+target)   
    print("Hora de inicio: "+str(datetime.now()))
    print("-" *50)

    try: 
        for port in range(int(ports[0]),int(ports[1])+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port)) #error
            #print("Escaneando puerto {}".format(port))
            if result == 0:
                print("El puerto {} esta abierto".format(port))
            s.close()

    except KeyboardInterrupt:
        print("\nSaliendo del programa.")
        sys.exit()

    except socket.gaierror:
        print("El hostname no pudo ser alcanzado.")
        sys.exit()

    except socket.error:
        print("No se pudo conectar al servidor")
        sys.exit()

elif len(sys.argv) == 4:
    if sys.argv[1] == "-l":
        ports=sys.argv[3].split('-')
        archivo=sys.argv[2]
        arc = open(archivo, "r")
        lines = arc.readlines()
        for line in lines:
            target = socket.gethostbyname(line[:-1]) #Hostname to IPV4
            print("-" *50)
            print("Escaneando objetivo " +target)   
            print("Hora de inicio: "+str(datetime.now()))
            print("-" *50)
            try: 
                for port in range(int(ports[0]),int(ports[1])+1):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = s.connect_ex((target,port)) #error
                    #print("Escaneando puerto {}".format(port))
                    if result == 0:
                        print("El puerto {} esta abierto".format(port))
                    s.close()

            except KeyboardInterrupt:
                print("\nSaliendo del programa.")
                sys.exit()

            except socket.gaierror:
                print("El hostname no pudo ser alcanzado.")
                sys.exit()

            except socket.error:
                print("No se pudo conectar al servidor")
                sys.exit()
    else:
        print("Cantidad invalida de argumentos")
        print("Sintaxis: ./scanner.py <ip> <puerto inferior-puerto superior>")
        print("O bien: ./scanner.py -l <lista objetivos> <puerto inferior-puerto superior>")
else:
    print("Cantidad invalida de argumentos")
    print("Sintaxis: ./scanner.py <ip> <puerto inferior-puerto superior>")
    print("O bien: ./scanner.py -l <lista objetivos> <puerto inferior-puerto superior>")