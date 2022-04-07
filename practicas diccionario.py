# ejemplo con variables strim, pero tambien se puede con numeros.
midiccionario={"alemania":"berlin","francia":"paris","españa":"madrid"}

# para ejecutar una busqueda especifica
print (midiccionario["españa"])

# para mostrar todo el diccionario
print (midiccionario)

# como agregar mas elementos al diccionario
midiccionario["italia"]="lisboa"

# para ejecutar orden anterior
print (midiccionario)

# para modificar un dato en el diccionario
midiccionario["italia"]="roma"

# para modificar orden anterior
print (midiccionario)

# para eliminar un elemento del diccionario
del midiccionario["españa"]

# para modificar la orden anterior
print (midiccionario) 

# para dar valores a un diccionario usando una lista
milista=["españa", "francia", "reino unido", "alemania"]
midiccionario1={milista[0]:"madrid", milista[1]:"paris", milista[2]:"londres", milista[3]:"berlin"}

# para ejecutar orden anterior
print (midiccionario1)

# para buscar valor especifico
print (midiccionario1["francia"])

# asignar un grupo de valores a un elemento del diccionario
midiccionario2={23:"jordan", "nombre": 23877, "anillos":[1991,1992,1993,1996,1997,1998]}

# para ejecutar orden anterior
print (midiccionario2["anillos"])

# para imprimir las claves
print (midiccionario2.keys())

# para imprimir los valores de un dicionario
print (midiccionario2.values())

# para saber la cantidad de valores de un diccionario
print (len(midiccionario2))