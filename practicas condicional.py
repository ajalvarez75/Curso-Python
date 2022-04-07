edad=145

#python leera el if the izquierda a derecha

if 0<edad<100:
   print ("edad es correcta")

else:
	print ("edad incorrecta")

# para python no es posible concatenar un valor de tipo string con un valor de tipo entero
# para funcione una concatenacion se deben manejar los mismos tipos de valores o datos

salario_presidente=int(input("introduce salario presidente "))
print ("salario_presidente: " + str(salario_presidente))

salario_director=int(input("introduce salario director "))
print ("salario_director: " + str(salario_director))

salario_jefe_de_area=int(input("introduce salario jefe de area "))
print ("salario_jefe_de_area: " + str(salario_jefe_de_area))

salario_administrativo=int(input("introduce salario administrativo "))
print ("salario_administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_de_area<salario_director<salario_presidente:
	print ("todo funciona correctamente")
else: 
	print ("algo huele mal")