class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

#para hacer salto de linea en pantalla \n
	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha,
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "la furgoneta esta cargada"

		else:
			return "la furgoneta no esta cargada"

#se declara la herencia para moto
class Moto(Vehiculos):
	HacerCaballito=""
	def caballito(self):
		self.HacerCaballito="Estoy haceindo el caballito"

	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha,
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.HacerCaballito)

class VehEletricos():
	def __init__(self):
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True

miMoto=Moto("Honda","CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta=Furgoneta("Ford", "Explorer")

miFurgoneta.arrancar()

miFurgoneta.estado()

print (miFurgoneta.carga(True))

# cuando existen herencias multiples el compilador lee de izq a derecha
class BicicletasElectricas(VehEletricos,Vehiculos):

	pass

miBici=BicicletasElectricas()
