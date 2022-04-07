from tkinter import *

root=Tk()

root.title("ejemplo")

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesViajes():

	opcionEscogida=""

	if(playa.get()==1):
		opcionEscogida+="playa "

	if(montagna.get()==1):
		opcionEscogida+="montaña "

	if(turismoRural.get()==1):
		opcionEscogida+="turismoRural "

	textoFinal.config(text=opcionEscogida)			


foto=PhotoImage(file="")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="elige destinos", width=50).pack()

Checkbutton(frame, text="playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViajes).pack()
Checkbutton(frame, text="montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViajes).pack()
Checkbutton(frame, text="rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViajes).pack()

textoFinal=Label(frame)
textoFinal.pack()



root.mainloop()
