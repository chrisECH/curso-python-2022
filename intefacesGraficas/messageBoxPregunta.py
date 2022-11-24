import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()

raiz.title("Mi programa")

#Creamos ventana emergente con pregunta

def preguntar():
    resultado = tkinter.messagebox.askquestion("Titulo", "¿Quieres borrar este fichero?")
    if(resultado == "yes"):
        print("Ha seleccionado que si")
    else:
        print("Ha seleccionado que no")
    



boton1 = tkinter.Button(raiz, text="Pulsa para preguntar", command=preguntar)
boton1.pack()

raiz.mainloop()