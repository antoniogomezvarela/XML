# -*- coding: utf-8 -*-
from lxml import etree

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

	#buscar = etree.Element("%s" % (identificacion))
	'''for i in buscar:
		if i.text == identificacion:
			print "SI"
		else:
			print "NO"'''

elif opcion == '2':
	print "sdads"
elif opcion == '3':
	print "sdads"
elif opcion == '4':
	print "sdads"
elif opcion == '5':
	print "sdads"
else:
	print "Elige una opción correcta"