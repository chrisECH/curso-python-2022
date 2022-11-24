import tkinter

raiz = tkinter.Tk()

raiz.title("Mi programa")

#Creamos el componente entry

entrada = tkinter.Entry(raiz)
entrada.config(justify="center")
entrada.pack()

raiz.mainloop()