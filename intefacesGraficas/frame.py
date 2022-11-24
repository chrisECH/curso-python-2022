import tkinter

raiz = tkinter.Tk()

raiz.title("Mi programa")

# Crear un frame 
frame = tkinter.Frame(raiz)
frame.config(bg="blue", width=600, height=300)
frame.pack()

raiz.mainloop()