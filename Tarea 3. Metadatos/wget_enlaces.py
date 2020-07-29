#!/usr/bin/python
# -*- coding: utf-8 -*-
#Cerón Rodríguez Lezly Dialid

import os
import re
import sys 

creators = []
applications = []
companies = []
modifiedby = []
modifydate = []
filesname = []

if(len(sys.argv) <2 ):
	print("Se requiere como argumento una lista de enlaces")
else:
	archivo=sys.argv[1]
	arc = open(archivo, "r")
	lines = arc.readlines()
	enlaces=open("enlacesdoc","w+")
	for line in lines:
		enlaces.write(line)
	os.system("mkdir wget")
	os.system("cd wget")
	os.system("for archivo in $(cat ../enlacesdoc); do sudo wget $archivo; done")
	os.system("exiftool . >> salida")
	f = open("salida", "r")
	lines = f.readlines()

	for line in lines:
		if "File Name " in line:
			if "Zip File Name " not in line:
				#print(line)
				filesname.append(line[34:-1])
		if "Creator" in line:
		#print(line[34:-1])
			creators.append(line[34:-1]+" Doc: "+filesname[-1])
		if "Application" in line:
		#print(line[34:-1])
			applications.append(line[34:-1]+" Doc: "+filesname[-1])
		if "Company" in line:
		#print(line[34:-1])
			companies.append(line[34:-1]+" Doc: "+filesname[-1])
		if "Last Modified By" in line:
		#print(line[34:-1])
			modifiedby.append(line[34:-1]+" Doc: "+filesname[-1])
		if "Modify Date" in line:
			if "Zip Modify Date" not in line:
			#print(line[34:-1])
				modifydate.append(line[34:-1]+" Doc: "+filesname[-1])
	reporte= open("reporte","w+")
	reporte.write("Creadores: \n")
	reporte.write("\n")
	for element in creators:
		reporte.write(element)
		reporte.write("\n")
	reporte.write("\n")
	reporte.write("Aplicaciones: \n")
	for element in applications:
		reporte.write(element)
		reporte.write("\n")
	reporte.write("\n")
	reporte.write("Companies: \n")
	for element in companies:
		reporte.write(element)
		reporte.write("\n")
	reporte.write("\n")
	reporte.write("Modificados por: \n")
	for element in modifiedby:
		reporte.write(element)
		reporte.write("\n")
	reporte.write("\n")
	reporte.write("Fecha de modificacion: \n")
	for element in modifydate:
		reporte.write(element)
		reporte.write("\n")

	print("reporte generado. Ejecute : 'cat reporte' para ver")
