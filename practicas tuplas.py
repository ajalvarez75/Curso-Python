# para hacer una tupla
mitupla=("juan", 1, 2.5, 1995)

# para ejecutar orden anterior
print (mitupla[:])

# para convertir una tupla a una lista
milista=list(mitupla)

# para ejecutar orden anterior
print (milista)

# para convertir una lista en tupla
milista2=[1, 2.5, "alvaro", 1]
mitupla2=tuple(milista2)

#para ejecutar orden anterior
print (mitupla2)

#para buscar un elemento en la tupla
print ("alvaro" in mitupla2)

# para saber el numero de veces que esta un elemento
print (mitupla2.count(1))

# para contar la cantidad de elementos de una tupla
print (len(mitupla2))

# tupla unitaria
mitupla3=("alvaro",)

#para ejecuitar orden anterior
print (len(mitupla3))

# empaquetado de tupla, es una tupla sin parentesis, se recomienda colocar parentesis.
mitupla4="javier", 1, 9.5

# para ejecutar orden anterior
print (mitupla4)

# desempaquetado de dupla o asignacion de variables a una tupla
mitupla5=("alvaro", 1,1,2022)
nombre,dia,mes,agno=mitupla5

# para ejecutar orden anterior
print (nombre)
print (dia)
print (mes)
print (agno)

# en tuplas no se puede usar la funcion append para agregar datos a la tupla.

# el metodo index si se puede aplicar con las duplas.