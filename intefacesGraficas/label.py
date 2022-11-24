import tkinter

raiz = tkinter.Tk()

raiz.title("Mi programa")

#Creamos el componente label

texto = "Hola mundo"
etiqueta= tkinter.Label(raiz, text=texto)
etiqueta.config(fg="green", bg="lightgrey", font=("Cortana", 30))
etiqueta.pack()

raiz.mainloop()