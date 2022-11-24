import tkinter
from tkinter import filedialog

raiz = tkinter.Tk()

raiz.title("Mi programa")


#Creamos ventana para abrir un fichero para
def abrirArchivo():
    rutaFichero = filedialog.askopenfile(title="Abrir archivo")
    print(rutaFichero)



boton = tkinter.Button(raiz, text="Pulsar para abrir un archivo", command=abrirArchivo)
boton.pack()

raiz.mainloop()


