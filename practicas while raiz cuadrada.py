# ejercicio raiz cuadrada
import math

print ("programa raiz cuadrada")
numero=int(input("introduce un numero por favor: "))

intentos=0

while numero<0:
	print ("no se puede hallar raiz cuadrada de u numero negativo")

	if intentos==2:
		print ("demasiados intentos, el programa ha finalizado")
		break;
		
	numero=int(input("introduce un numero por favor: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print ("la raiz cuadrada de " + str(numero) + " es " + str(solucion))