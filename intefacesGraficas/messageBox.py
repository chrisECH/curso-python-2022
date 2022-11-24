import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()

raiz.title("Mi programa")


#Creacion de message box
def avisar():
    ventana1 = tkinter.messagebox.showinfo("Titulo", "Mensaje informativo" )


boton1 = tkinter.Button(raiz, text="Aviso", command=avisar)
boton1.pack()


raiz.mainloop()