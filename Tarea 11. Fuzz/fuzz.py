#!/usr/bin/python
#Ceron Rodriguez Lezly Dialid

import requests
import sys

header = {'User-Agent':'Mozilla/5.0'} 
#fuzz_url = "http://truerandom.bid/tienda" 
caracteres = {'\'', '_', '..', '/', '1', '2', '3', '4', '5','6','7','8','9','0','%','*','UNION'}
archivo=sys.argv[1]
arc = open(archivo, "r")
urls = arc.readlines()
for url in urls:
	response = requests.get(url,headers=header) 
	status = response.status_code 
	if (status == "200"):
		print("URL potencialmente inyectable:" + url)
	if "Error" in response.text or "Syntax" in response.text:
		print("URL potencialmente inyectable:" + url)
	for c in caracteres:
		response = requests.get(url+c,headers=header) 
		status = response.status_code 
		if (status == "200"):
			print("URL potencialmente inyectable:" + url)
		if "Error" in response.text or "Syntax" in response.text:
			print("URL potencialmente inyectable:" + url)