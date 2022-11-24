import tkinter

raiz = tkinter.Tk()

raiz.title("Mi programa")

#Creamos el componente buttom
def accion():
    print("Hola mundo")

boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.config(fg="green")
boton.pack()


raiz.mainloop()