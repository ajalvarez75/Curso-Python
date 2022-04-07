# ignora la linea de la letra h y contionua el bucle hasta que termina

for letra in "pyhton":

	if letra=="h":
		continue

	print ("viendo la letra " + letra)

# contar el numero carateres
nombre="pildoras infomaticas"

contador=0

for i in nombre:

	if i==" ":
		continue
	contador+=1
    # forma alternativa para aumentar el conteo 
    # contador=contador=1

print (contador)

#pass, devuelve un null, como si el bucle no se ejecutara, mantiene el programa ocupado hasta que el usuario salga del bucle

# ejercicio else

email=input("introduce tu email, por favor: ")

for i in email:

	if i=="@":

		arroba=True

		break;

else:
	arroba=False

print(arroba)