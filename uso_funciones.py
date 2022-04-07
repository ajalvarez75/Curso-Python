#import practicas modulos
#El * funciona para importar todas las clases u objetos que se han creado en el modulo

from practicas_modulos import *

sumar(7,5)

restar(8,2)

multiplicar(2,2)

#si se cambia el archivo practicas_modulos de carpeta el interprete de python generara error, si...
#el modulo no encuentra el archivo en la misma carpeta de uso_funciones pasara a buscarlo en syspath
# para configurar la ubicacion de los modulos y usarlos desde cualquier ubicacion se deben usar paquetes