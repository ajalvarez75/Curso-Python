#ejemplo de funcion tradicional
'''def area_triangulo(base, altura):

	return (base*altura)/2

triangulo1=area_triangulo(5,7)

triangulo2=area_triangulo(9,6)

print(triangulo1)

print(triangulo2)'''

#con funcion lambda, funciones complejas no pueden ser resumidas con esta forma ya que no tiene condicionales o bucles
area_triangulo=lambda base, altura:(base*altura)/2

#una vez establecida la formula lambda se puede:
print(area_triangulo(7,5))

#otra forma
triangulo1=area_triangulo(7,5)

print(triangulo1)


# ejercicio 2
al_cubo=lambda numero:pow(numero,3)

#al_cubo=lambda numero:numero**3

print(al_cubo(13))


#ejercicio 3
destacar_valor=lambda comision:"¡{}!€".format(comision)

comision_Ana=15585

print(destacar_valor(comision_Ana))