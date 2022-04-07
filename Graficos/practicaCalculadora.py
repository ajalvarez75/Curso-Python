from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)

miFrame.pack()

operacion=""

resultado=0


#---------------------Pantalla-----------------------------
#con columnspan se abarcan todas las columanas que queramos

numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#---------------------Pulsaciones teclado------------------
# se usa mas para concatenar
# se usa get para almacenar la informacion pulsada
# se usa set para mostrar en pantalla el numero presionado
#funcion para que cuando se realice la operacion nos permita ingresar un nuevo valor
def numeroPulsado(num):
	global operacion
	
	if operacion!="":
		numeroPantalla.set(num)

		operacion=""
	
	else:
		numeroPantalla.set(numeroPantalla.get() + num)

#---------------------Funcion Suma-------------------------
# al usar += se incrementa
# con la funcion int python interpretara las letras como numeros enteros
def suma(num):
	global operacion

	global resultado
#resultado=resultado+int(num)
	resultado+=int(num)

	operacion="suma"

	numeroPantalla.set(resultado)

#---------------------Funcion el resultado-------------------------------	

def el_resultado():

	global resultado

	numeroPantalla.set(resultado+int(numeroPantalla.get()))

	resultado=0

#---------------------Fila 1-------------------------------

button7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
button7.grid(row=2, column=1)
button8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
button8.grid(row=2, column=2)
button9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
button9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)

#---------------------Fila 2-------------------------------

# lambda hace que el programa no almacene el numero 4 predeterminadamente

button4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
button4.grid(row=3, column=1)
button5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
button5.grid(row=3, column=2)
button6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
button6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width=3)
botonMult.grid(row=3, column=4)

#---------------------Fila 3-------------------------------

button1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
button1.grid(row=4, column=1)
button2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
button2.grid(row=4, column=2)
button3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
button3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3)
botonRest.grid(row=4, column=4)

#---------------------Fila 4-------------------------------

button0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
button0.grid(row=5, column=1)
buttonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
buttonComa.grid(row=5, column=2)
buttonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
buttonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)

raiz.mainloop()