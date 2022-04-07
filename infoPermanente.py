import pickle

class Persona:

	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("se ha creado una persona nueva con el nombre de: ", self.nombre)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

	personas=[]

	def __init__(self):

		ListaDePersonas=open("FicheroExterno", "ab+")
		ListaDePersonas.seek(0)

		try:
			self.personas=pickle.load(ListaDePersonas)
			print("se cargaron {} personas del fichero externo".format(len(self.personas)))

		except:
			print("el fichero esta vacio")

		finally:
			ListaDePersonas.close()
			del(ListaDePersonas)		

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		ListaDePersonas=open("FicheroExterno", "wb")
		pickle.dump(self.personas, ListaDePersonas)
		ListaDePersonas.close()
		del(ListaDePersonas)

	def mostrarInfoFicheroExterno(self):
		print("la informacion del fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)

miLista=ListaPersonas()
persona=Persona("Ana", "Femenino", 19)
miLista.agregarPersonas(persona)
#p=Persona("Antonio", "Masculino", 39)
#miLista.agregarPersonas(p)
#p=Persona("Ana", "Femenino", 19)
#miLista.agregarPersonas(p)
miLista.mostrarInfoFicheroExterno()
#miLista.mostrarPersonas()