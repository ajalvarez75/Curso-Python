print ("programa dew becas año 2022")

distancia_escuela=int(input("introduce la distancia de la escuela en KM:  "))
print (distancia_escuela)

numero_hermanos=int(input("introduce numero de hermanos:  "))
print (numero_hermanos)

salario_familiar=int(input("introduce salario familiar:  "))
print (salario_familiar)

#el or puede ser interpretado como sino
if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=2000:
    print ("tiene derecho a beca")

else:
    print ("no tiene derecho a beca")


#ejercicio 2
print ("asignaturas optativas 2022")

print ("asignaturas optativas: python - java - c++")
opcion=input("escribe la asignatura escogida:  ")

#con la siguiente opcion se puede pasar el texto introducido a minuscula para que sea compatible con la forma en la cual se programo
asignatura=opcion.lower()

if asignatura in ("python", "java", "c++"):

	print ("asignatura elegida  " + asignatura)

else:
	print ("la asignatura escogida no esta completada")



