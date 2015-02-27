# -*- coding: utf-8 -*-
from lxml import etree
from datetime import date
tree = etree.parse('becas_premios.xml')
documento = tree.getroot()

#MENU

print "1- Buscar beca o premio por teclado"
print "2- Mostrar becas y enlaces"
print "3- Buscar las becas y premios que su fecha de publicación este entre febrero y abril"
print "4- Contar cuantas becas y premios se han dado."
print "5- Mostrar las id de las becas y añadir cuantos dias ha estado abierta"

opcion= raw_input("Elige una opción: ")

#Ejercicio 1
if opcion == '1':
	encontrado = False
	identificacion = raw_input("Introduce una id: ")
	for i in documento:
		if i[0].text==identificacion:
			encontrado = True
			print "ID: ",i[0].text
			print "Titulo: ",i[1].text
			print "Fecha: ",i[2].text
			print "Descripción: ",i[3].text
			print "Estado: ",i[5].text
	if encontrado == False:
		print "Esa ID no existe"

elif opcion == '2':
	for i in documento:
		print "ID: ",i[0].text,", Enlace: ",i[4].text

elif opcion == '3':
		for i in documento:
			fecha1=i[2].text
			fecha2=fecha1.split("-")
			if fecha2[1] >= "02" and fecha2[1] <= "04":
				print "ID: ",i[0].text,", Fecha: ",i[2].text

elif opcion == '4':
	becas = 0
	premios = 0
	for i in documento:
		titulo = i[1].text
		titulo = titulo.split(" ")
		if titulo[0] == "Becas":
			becas += 1
		elif titulo[0] == "Premios":
			premios += 1

	print "Número de becas concedidas: ",becas
	print "Número de premios concedidos: ",premios 

elif opcion == '5':
	date_format = "%Y/%m/%d"
	for i in documento:
		incial = i.findall("plazopresentacion/plazopresentacion_item/incial")
		final = i.findall("plazopresentacion/plazopresentacion_item/final")
		inicial= str(incial[0].text)
		final= str(final[0].text)
		if inicial != "None" or final != "None":
			inicial = inicial.split("T")
			final = final.split("T")
			inicial = inicial[0].split("-")
			final = final[0].split("-")
			d0 = date(int(inicial[0]),int(inicial[1]),int(inicial[2]))
			d1 = date(int(final[0]),int(final[1]),int(final[2]))
			dias = d1-d0
			print "la beca ",i[0].text," estuvo abierta ",dias.days," dias"

else:
	print "Elige una opción correcta"