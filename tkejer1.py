from tkinter import *
import tkinter

Ventana = tkinter.Tk()
Ventana.geometry("300x200")
Ventana.title ( "Contador" )
Ventana.config ( bg = "lightgrey" )

def mas():
    num=int(Barra_de_Num ["text"])
    Barra_de_Num ["text"] = f"{num+1}"

etiquet=Label(Ventana, text = "Contador")
etiquet.place(x=15,y=80)

Barra_de_Num= Label(Ventana,text = "0" ,)
Barra_de_Num.place( x = 120, y = 80)

boton1 = tkinter.Button(Ventana, text ="+",command=mas)
boton1.place(x=225, y=80)

Ventana.mainloop()