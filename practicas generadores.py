# generar numeros pares
def generapares(limite):

	num=1

	milista=[]

	while num<limite:

		milista.append(num*2)

		num=num+1

	return milista

print (generapares(10))

# otra manera
def generapares(limite):

	num=1

	while num<limite:

		yield num*2

		num=num+1

devuelvepares=generapares(10)

for i in devuelvepares:

	print (i)


# devuelve ciudades, con el * puedo indicar los valores a generar

def devuelve_ciudades (*ciudades):

	for elemento in ciudades:
		yield elemento

ciudades_devueltas=devuelve_ciudades("Bogota", "Medellin", "Cartagena", "Barranquilla")

# con la funcion next, se van a devolver los valores 1 a 1
print(next(ciudades_devueltas))
# para ver valor Medellin
print(next(ciudades_devueltas))


# para generar los subelementos

def devuelve_ciudades (*ciudades):
# bucle for aninado
	for elemento in ciudades:
		for subelemento in elemento:
		    yield subelemento

# para abreviar el metodo anterior se podria omitir la linea for subelemento in elemento:
# y se colocaria en la linea de yield, yield from elemento

ciudades_devueltas=devuelve_ciudades("Bogota", "Medellin", "Cartagena", "Barranquilla")

# con la funcion next, se van a devolver los valores 1 a 1
print(next(ciudades_devueltas))
# para ver valor Medellin
print(next(ciudades_devueltas))

