# bucle determinado-con final
i=1

while i<=10:
	print("Ejecucion " + str(i))
	i=i+1

print("termino la ejecucion")


# bucle indeterminado
edad=int(input("introduce tu edad, pora favor: "))

# segun la condicion establecida en el while puede ser interminado o no
while edad<0:
	print("has introducido una edad negativa. Vuelve a intentarlo")
	edad=int(input("introduce tu edad, pora favor: "))

print("Gracias por colaborar. Puedes pasar")
print("edad del aspirante " + str(edad))

	
# while con rango
edad=int(input("introduce tu edad, pora favor: "))

while edad<5 or edad>100:
	print("has introducido una edad incorrecta. Vuelve a intentarlo")
	edad=int(input("introduce tu edad, pora favor: "))

print("Gracias por colaborar. Puedes pasar")
print("edad del aspirante " + str(edad))