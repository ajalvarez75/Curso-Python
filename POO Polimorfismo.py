class Coche():

	def desplazamiento(self):
		print("Me desplazo en 4 ruedas")

class Moto():

	def desplazamiento(self):
		print("Me desplazo en 2 ruedas")

class Camion():

	def desplazamiento(self):
		print("Me desplazo en 6 ruedas")

#camino largo
Vehiculo1=Coche()
Vehiculo1.desplazamiento()

Vehiculo2=Moto()
Vehiculo2.desplazamiento()

Vehiculo3=Camion()
Vehiculo3.desplazamiento()

#con polimorfismo
def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()
#reemplazando la variable puede adoptar el valor de su reespetiva funcion de desplazamiento
miVehiculo=Camion()

desplazamientoVehiculo(miVehiculo)
