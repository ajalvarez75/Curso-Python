import pickle

class Vehiculo():

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

	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha,
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

coche1=Vehiculo("mazda","mx5")

coche2=Vehiculo("mazda","mx10")

coche3=Vehiculo("mazda","mx15")

coches=[coche1, coche2, coche3]

fichero=open("loscoches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)


#para recuperar el archivo binario

ficheroApertura=open("loscoches", "rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
	print(c.estado())