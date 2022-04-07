from tkinter import *

raiz=Tk()

raiz.title("ventana de pruebas")

#para poder cambiarle el tamaño a la ventana. solo horizontalmente
#raiz.resizable(True,False)

#la imagen tiene que ser en formato .ico, se deja vacia.
raiz.iconbitmap("")

#tamaño de la foto
raiz.geometry("650x350")

#fondo del ventana bg=background
raiz.config(bg="blue")

raiz.config(bd=45)

raiz.config(relief="groove")

#we can use other options like "pirate"
raiz.config(cursor="pirate")

miFrame=Frame()

miFrame.pack()

#n = north
miFrame.pack(side="left", anchor="n")

# is poisble to use X or both instead Y.
miFrame.pack(fill="y", expand="True")

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd=35)

miFrame.config(relief="sunken")

#we can use other options like "pirate"
miFrame.config(cursor="hand2")

raiz.mainloop()
#en el archivo se agrega una W a la extension .PY para que abra directamente en windows.