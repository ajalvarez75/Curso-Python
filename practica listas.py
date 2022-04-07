#la lista comienza desde 0, siente este elemento asignado a Maria.
# 0=Maria, 1=Pepe, 2=Martha, 3=Antonio
milista=["Maria","Pepe","Martha","Antonio"]

# para llamar a la lista
print (milista[:])

# para llamar/mostrar un elemento determinado de la lista
print (milista[3])

# para llamar un rango de la lista,
print (milista[1:3])
# nota: para que se incluya el ultimo dato deseado de la lista se debe colocar el numero siguiente.

# para colocar desde el dato deseado hasta el ultimo.
print (milista[1:])

# para agregar un elemento al final de la lista
milista.append("Alvaro")

# para leer la instruccion previa
print (milista[:])

# para insertar un dato a partir de una posicion especifica en la lista.
milista.insert(2,"Javier")

# para leer la instruccion previa
print (milista[:])

# para concatenar o expandir nuetra lista con un numero indeterminado de elementos.
milista.extend(["noviembre", "diciembre", "Enero", "bogota", "Medellin", 6, 7.5, True])

# para leer la instruccion previa
print (milista[:])

# para saber una posicion expecifica
# en caso de existir dos valores/datos iguales, nos va a mostrar la posicion del primer valor/dato.
print (milista.index("Enero"))

# para saber si un dato existe en la lista
# el dato debe ser exacto. de otra forma mostrara False.
print("Pepe" in milista)

# para remover elementos de la lista
milista.remove("bogota")

# para leer la instruccion previa
print (milista[:])

# para remover cualquier elemento de la lista
milista.remove(True)

# para leer la instruccion previa
print (milista[:])

# eliminar el ultimo elemento de una lista
milista.pop()

# para leer la instruccion previa
print (milista[:])

# para sumar dos listas
milista2=["adios", "UPS"]

milista3=milista+milista2

print (milista3[:])

# para multiplicar o repetir una lista
milista4=["a","b","c"] * 2

print (milista4[:])