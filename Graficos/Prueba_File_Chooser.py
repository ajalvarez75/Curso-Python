from tkinter import *
from tkinter import filedialog

root=Tk()

def abreFichero():
	fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("ficheros de excel","*.xlsx"),
		("Ficheros de texto","*.txt"),("todos los ficheros","*.*")))

	print(fichero)

Button (root, text="Abrir Fichero", command=abreFichero).pack()

root.mainloop()