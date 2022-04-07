from tkinter import *
from tkinter import messagebox

root=Tk()

def infoAdicional():
	messagebox.showinfo("Procesador de Juan", "Procesador de textos 2022")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
	#con askquestion se visualizara si o no
	#valor=messagebox.askquestion("salir", "¿Desea salir de la aplicacion?")
	#con askokcancel se visualizara aceptar o cancelar 
	valor=messagebox.askokcancel("salir", "¿Desea salir de la aplicacion?")
	#con askquestion el messagebox devuelve si o no
	#con askokcancel el messagebox devuelve True o False
	if valor==True:
		root.destroy()

def cerrarDocumento():
	valor=messagebox.askretrycancel("reintentar", "No es posible cerrar. Documento bloqueado")
	if valor==False:
		root.destroy()



barraMenu=Menu(root)

root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)


archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")


archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)



barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()