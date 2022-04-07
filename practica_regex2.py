import re

lista_nombres=['Ana Gomez',
				'Maria Martinez',
				'Sandra Lopez',
				'Santiago Martinez']


for elemento in lista_nombres:
#se pueden usar simbolos para encontrar relacionados antes o despues del valor a encontrar como ^ o $
#^ los que comienza y $ los que terminan
	if re.findall('^Sandra', elemento):

		print(elemento)

#-------------------------------------------------------------

lista_nombres1=['Ana Gomez',
				'Maria Martinez',
				'Sandra Lopez',
				'Santiago Martinez']


for elemento1 in lista_nombres1:
#apellidos
	if re.findall('Martinez$', elemento1):

		print(elemento1)

#--------------------------------------------------------------


lista_nombres2=['Ana GoÑez',
				'Maria Martinez',
				'Sandra Lopez',
				'Santiago Martinez']


for elemento2 in lista_nombres2:
#carateres
	if re.findall('[Ñ]', elemento2):

		print(elemento2)


#--------------------------------------------------------------

lista_nombres3=['hombres',
				'mujeres',
				'niños',
				'niñas']


for elemento3 in lista_nombres3:
#elemento masculinos y femeninos
	if re.findall('niñ[oa]s', elemento3):

		print(elemento3)

#--------------------------------------------------------------

lista_nombres4=['Alvaro',
				'Javier',
				'Tomas',
				'Ricardo']


for elemento4 in lista_nombres4:
#rango de elementos, si no se especifica si los elementos a buscar comienzan ^ o terminan $ pyhton asumira que comienzan 
	if re.findall('[J-T]', elemento4):

		print(elemento4)

#--------------------------------------------------------------


lista_nombres4=['Alvaro',
				'Javier',
				'Tomas',
				'Ricardo']


for elemento4 in lista_nombres4:
#rango de elementos, si no se especifica si los elementos a buscar comienzan ^ o terminan $ pyhton asumira que comienzan 
	if re.findall('[J-T]', elemento4):

		print(elemento4)

#--------------------------------------------------------------


lista_nombres5=['ma1',
				'ma5',
				'ma3',
				'ma6',
				'maA',
				'maC',
				'maD',
				'maE']


for elemento5 in lista_nombres5:
#doble rango de elementos
	if re.findall('ma[3-5C-D]', elemento5):

		print(elemento5)



