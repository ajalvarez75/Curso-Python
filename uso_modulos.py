#Calculos = nombre de la carpeta donde tenemos nuestro modulo
#calculos_generales = nombre de nuestro archivo con los modulos
#se usa * para usar la funcion que queramos

#from Calculos.calculos_generales import potencia
from Calculos.calculos_generales import *

sumar(4,6)

#para hacer que las carpetas funcionen como paquetes y sean reconocidas por el editor de python
#debemos colocar dentro de cada carpeta el archivo __init__.py

#ejercicio 2
from Calculos.basicos_mas.OperacionesBasicas import *

dividir(4,6)

#ejercicio 3
from Calculos.redondeo_potencia.redondearYpotenciar import *

redondear(4.8)