#este Ejercicio nos ayuda a anticipar el error generado al realizar una raiz negativa
import math

def calculaRaiz(num1):

	if num1<0:
		raise ValueError ("el numero no puede ser negativo")

	else:
		return math.sqrt(num1)

op1=int(input("ingrese un numero: "))

try:
	print (calculaRaiz(op1))

except ValueError as ErrorDeNumeroNegativo:
	print (ErrorDeNumeroNegativo)

print ("programa terminado")
