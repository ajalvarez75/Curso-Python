#clase con 4 propiedades
class Coche():
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enmarcha=False

#se establecen 2 comportamientos para nuestra clase, en marcha o parado
	def arrancar(self):
		self.enmarcha=True

	def estado(self):
		if(self.enmarcha):
			return "El coche esta en marcha"

		else:
			return "El coche esta parado"		

miCoche=Coche()

print("El largo del coche es: ", miCoche.largoChasis)
print("El ancho del coche es: ", miCoche.anchoChasis)
print("El numero de ruedas de mi coche es: ", miCoche.ruedas)

miCoche.arrancar()

print(miCoche.estado())
		