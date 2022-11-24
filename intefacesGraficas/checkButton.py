import tkinter

raiz = tkinter.Tk()

raiz.title("Mi programa")


#creacion de checkbuttom

def verificar():
    valor = check1.get()
    if(valor==1):
        print("El valor esta activo")
    else:
        print("El valor esta desactivado")

check1 = tkinter.IntVar()

checkButtom = tkinter.Checkbutton(raiz, text="Opcion 1", variable=check1, onvalue=1, offvalue=0, command=verificar)
checkButtom.pack()

raiz.mainloop()