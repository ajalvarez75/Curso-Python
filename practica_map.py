class Empleado:

	def __init__(self, nombre, cargo, salario):

		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):

		return"{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)


listaEmpleados=[

Empleado("Juan", "director", 6700),

Empleado("Ana", "presidenta", 7500),

Empleado("Antonio", "administrativo", 2100),

Empleado("juan", "secretaria", 2150),

Empleado("juan", "botones", 1800),

]

def calculo_comision(empleado):

	empleado.salario=empleado.salario*1.03

	return empleado

listaEmpleadoscomision=map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadoscomision:

	print(empleado)