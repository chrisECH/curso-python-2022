import tkinter

raiz = tkinter.Tk()

raiz.title("Mi programa")

#Creacion de radiobuttom

def seleccionar():
    print("La opcion seleccionada es {}".format(opcion.get()))

opcion = tkinter.IntVar()

radiobuttom1 = tkinter.Radiobutton(raiz, text="Opcion 1", variable=opcion, value=1, command=seleccionar)
radiobuttom1.pack()

radiobuttom2 = tkinter.Radiobutton(raiz, text="Opcion 2", variable=opcion, value=2, command=seleccionar)
radiobuttom2.pack()

radiobuttom3 = tkinter.Radiobutton(raiz, text="Opcion 3", variable=opcion, value=3, command=seleccionar)
radiobuttom3.pack()

raiz.mainloop()