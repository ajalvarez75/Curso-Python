import re
#considerar buscar patrones de busqueda python
nombre1="Sandra Lopez"

nombre2="Antonio Gomez"

nombre3="Maria Lopez"


if re.match("Sandra", nombre1):

	print("Hemos encontrado el nombre")

else:

	print("No lo hemos encontrado")

#---------------------------------------------------


nombre1="Jara Lopez"

nombre2="Antonio Gomez"

nombre3="Lara Lopez"

#el punto representa una letra sin determinar
if re.match(".ara", nombre3, re.IGNORECASE):

	print("Hemos encontrado el nombre")

else:

	print("No lo hemos encontrado")

#---------------------------------------------------


cadena1="Jara Lopez"

cadena2="1234568"

cadena3="a1561641616"

#encontrar un dato solo numero
if re.match("\d", cadena2):

	print("Hemos encontrado el nombre")

else:

	print("No lo hemos encontrado")