def funcion_decoradora(funcion_parametro):
#*args=numero indeterminado de parametros
#**kwargs= argumentos con clave
	def funcion_interior(*args, **kwargs):

		#acciones adicionales que decoran

		print("vamos a realizar un calculo: ")

		funcion_parametro(*args, **kwargs)

		#acciones adicionales que decoran

		print("hemos terminado el calculo")

	return funcion_interior
	
@funcion_decoradora
def suma(num1, num2, num3):

	print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):

	print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):

	print(pow(base, exponente))


suma(8,10,2)

resta(10,2)

potencia(base=5, exponente=3)				