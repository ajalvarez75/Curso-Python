class Coche():

	def __init__(self):

		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	def arrancar(self,arrancamos):
		self.enmarcha=arrancamos

		if(self.__enmarcha):
			chequeo=self.__chequeo_interno()

		if(self.__enmarcha and chequeo):
			return "El coche esta en marcha"

		elif(self.__enmarcha and chequeo==False):
			return "algo ha ido mal en el chequeo. no podemos arrancar"	

		else:
			return "El coche esta parado"

	def estado(self):
		print("el coche tiene: ", self.__ruedas, "ruedas. un ancho de: ", self.__anchoChasis, "y un largo de: ", self.__largoChasis)

#metodo normal y corriente, metodo no encapsulado
	def chequeo_interno(self):
		print("reaalizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.gasolina=="ok" and self.puertas=="cerradas"):
			return True

		else:
			return False

miCoche=Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("-------A continuacion creamos el segundo objeto-------")

miCoche2=Coche()

print(miCoche.arrancar(False))

miCoche2.estado()
