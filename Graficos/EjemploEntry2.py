#con grid.
from tkinter import *
raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

miNombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg="red", justify="right")

#en caso de querer hacer un cuadro de contraseña se puede usar/añadir la siguiente opcion
#el * puede ser reemplazado por cualquier simmbolo que queramos que se visualice.

cuadropassword=Entry(miFrame)
cuadropassword.grid(row=1, column=1, padx=10, pady=10)
cuadropassword.config(fg="red", justify="right")
cuadropassword.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroApellido.config(fg="red", justify="right")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)
cuadroDireccion.config(fg="red", justify="right")

textoComentario=Text(miFrame, width=15, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)

#para construir el scroll
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
#con la funcion sticky="nsew" para que se adapte al cuadro de texto de los comentarios
scrollVert.grid(row=4, column=2, sticky="nsew")
#para agregar un posicionador al scroll
textoComentario.config(yscrollcommand=scrollVert.set)


#con la opcion sticky podemos modificar la posicion de los nombres de los marcos
#w=weste n=north s=south e=este tambien se pueden usar las opciones intermedias
#wn, ne, se, sw

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

passwordLabel=Label(miFrame, text="contraseña: ")
passwordLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)


def codigoBoton():
	miNombre.set("Alvaro")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)

botonEnvio.pack()

#para poder visualizar nuestra interfaz grafica/ventana
raiz.mainloop()