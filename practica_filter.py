'''def numero_par(num):

	if num % 2==0

	return True'''

numeros=[17,24,7,39,8,51,92]

print(list(filter(lambda numero_par: numero_par%2==0, numeros)))


#Ejercicio 2

class Empleado:

	def __init__(self, nombre, cargo, salario):

		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):

		return"{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)


listaEmpleados=[

Empleado("Juan", "director", 75000),

Empleado("Ana", "presidenta", 85000),

Empleado("Antonio", "administrativo", 25000),

Empleado("juan", "secretaria", 27000),

Empleado("juan", "botones", 21000),

]

salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado_salario in salarios_altos:

	print(empleado_salario)