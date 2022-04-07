from io import open
# con W se especifica que se va a escribir, 
Archivo_texto=open("archivo.txt", "w")

frase="estupendo dia para estudiar python\nel miercoles"

Archivo_texto.write(frase)

Archivo_texto.close()
#el archivo text queda creado en la carpeta que asignamos para el editor.


# r para read 
Archivo_texto=open("archivo.txt", "r")

texto=Archivo_texto.read()

Archivo_texto.close()

print(texto)


#se puede usar el readlines en lugar de read

Archivo_texto=open("archivo.txt", "r")

lineas_texto=Archivo_texto.readlines()

Archivo_texto.close()

print(lineas_texto)

# para leer una linea en especifico

print(lineas_texto[0])


# se puede usar el comando append (a) para poder añadir lineas al archivo

Archivo_texto=open("archivo.txt", "a")

Archivo_texto.write("\nsiempre es un buen dia para estudiar")

Archivo_texto.close()


#con el metodo seek podemos modificar la posicion del puntero

Archivo_texto=open("archivo.txt", "r")

#con el numero le especificamos la posicion del puntero a partir de un numero de carateres
Archivo_texto.seek(11)
# hace una lectura hasta la posicion que le hemos indicado
print(Archivo_texto.read())


#lectura y escritura

Archivo_texto=open("archivo.txt", "r+")

#print(Archivo_texto.readlines())

lista_texto=Archivo_texto.readlines();

#con esta linea se puede reeemplazar cualquier linea dentro del archivo
lista_texto[2]="Esta linea ha sido incluida desde el exterior\n"

Archivo_texto.seek(0)

Archivo_texto.writelines(lista_texto)

Archivo_texto.close()