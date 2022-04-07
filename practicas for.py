for i in [1,2,3]:
	print ("hola")

for i in ["primavera", "verano", "octoño", "invierno"]:
	print (i)

for i in ["pildoras", "informaticas"]:
# imprime tan veces como palabras hay
# con el end se puede determinar el espacio entre el numero de impresiones
	print ("hola", end=" ")

# si se deja una sola palabra se imprimira el numero de carateres que tenga la palabra
for i in "abcdfg":
    print ("gracias", end=" ")

# evaluar si es un correo electronico
email=False

for i in "Alvaro@alvarez":
	if (i=="@"):
		email=True

if email:
	print ("email es correcto")
else:
	print ("email es incorrecto")	

# evaluar si un conjunto de datos puede llegar a ser correo eletronico
email=False
miemail=input ("introduce tu correo electronico:  ")
for i in miemail:
	if (i=="@"):
		email=True

if email:
	print ("email es correcto")
else:
	print ("email es incorrecto")


