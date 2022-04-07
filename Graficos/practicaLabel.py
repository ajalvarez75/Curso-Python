from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

Label(miFrame, text="Hola Gente de Python", fg="red", font=("comic sans MS", 18)).place(x=100, y=200)

root.mainloop()

#solo imagen
root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="image1.png")

Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()

