class Persona():

	def __init__(self, nombre, edad, Lugar_residencia):

		self.nombre=nombre
		self.edad=edad
		self.Lugar_residencia=Lugar_residencia

	def descripcion(self):

		print("nombre: ", self.nombre, "edad: ", self.edad, "lugar_residencia: ", self.Lugar_residencia)

class Empleado(Persona):

	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

		#funcion super sirve para heredar carateristicas de una clase anterior
		super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):

		super().descripcion()

		print("salario: ", self.salario, "antiguedad: ", self.antiguedad)

Antonio=Empleado(1500, 15, "Manuel", 55, "Colombia")

Antonio.descripcion()

# para saber si un objeto pertenece a una clase o no

print(isinstance(Antonio, Persona))



