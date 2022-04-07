#clase con 4 propiedades, un constructor es un metodo especial que le un estado inicial a un objeto
#para establecer un contructor se debe inciar con def __init__(self): nota:init=estado inicial.
class Coche():
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enmarcha=False

#comportamientos del ejercicio POO1 mejorados
	def arrancar(self,arrancamos):
		self.enmarcha=arrancamos

		if(self.enmarcha):
			return "El coche esta en marcha"

		else:
			return "El coche esta parado"

	def estado(self):
		print("el coche tiene: ", self.ruedas, "ruedas. un ancho de: ", self.anchoChasis, "y un largo de: ", self.largoChasis)

miCoche=Coche()

print("El largo del coche es: ", miCoche.largoChasis)
print("El numero de ruedas de mi coche es: ", miCoche.ruedas, " ruedas")
print(miCoche.arrancar(True))

miCoche.estado()

print("-------A continuacion creamos el segundo objeto-------")

miCoche2=Coche()

print("El largo del coche es: ", miCoche.largoChasis)
print("El numero de ruedas de mi coche es: ", miCoche.ruedas, " ruedas")
print(miCoche.arrancar(False))

miCoche2.estado()
