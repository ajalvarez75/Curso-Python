print ("verificacion de acceso")

edad_usuario=int(input("introduce tu edad, por favor"))

#considerar en en caso de que existan varios IF el ELSE funcionara con el IF mas cercano

if edad_usuario<18:
	print ("no puedes pasar")

else:	
     print ("puedes pasar")

print ("el programa ha finalizado")

# ejercicio 2, multiples IF para un Else, recordar la primera nota, ya que el programa generara error.

print ("verificacion de acceso")

nota_alumno=int(input("introduce tu nota, por favor:  "))

if nota_alumno<5:
    print ("insuficiente")

if nota_alumno<6:
	print ("suficiente")

if nota_alumno<7:
	print ("bien")

if nota_alumno<9
    print ("notable")

else:
	print("sobresaliente")
