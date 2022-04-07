# uso de rangos con la funcion for
for i in range(5):
	print ("adios")

for i in range(5):
	print (i)

# funcion de tipo f, para concatenar el nombre de la variable con su valor
for i in range(5):	
	print (f"valor de la variable {i}")

# conteo de un rango de datos desde un numero espefico
# primer valor(5), desde se debe comenzar el rango
# segundo valor(10), hasta donde iria el conteo (9)
# tercer valor(2), determina como se hara el conteo, para este ejemplo tiene que ser de 2 en 2.
for i in range(5,100,20):	
	print (f"valor de la variable {i}")

#ejercicio de validacion para correo eletronico
valido=False
email=input("introduce tu email:  ")

for i in range(len(email)):
	if email[i]=="@":
         valido=True

if valido:
	print ("correo valido")

else:
	print ("correo invalido")