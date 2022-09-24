from tkinter import *
import tkinter


Ventana = tkinter.Tk()
Ventana.title ( "Contador Crece" )
Ventana.config ( bg = "lightgrey" )

def Mas():
    num=int(Barra_de_Num ["text"])
    Barra_de_Num ["text"] = f"{num+1}"

def Menos():
    num=int(Barra_de_Num ["text"])
    Barra_de_Num ["text"] = f"{num-1}"

def Reiniciar():
    num=int(Barra_de_Num ["text"])
    Barra_de_Num ["text"] = f"0"

etiquet=Label(Ventana, text = "Contador")
etiquet.grid(row=1,column= 0,padx=5, pady=2)

Barra_de_Num= Label(Ventana,text = "0" ,)
Barra_de_Num.grid(row=1,column= 1,padx=5, pady=2)

boton1 = tkinter.Button(Ventana, text ="+",command=Mas )
boton1.grid(row=0,column= 2,padx=5, pady=2)
boton2 = tkinter.Button(Ventana, text ="-",command=Menos )
boton2.grid(row=1,column= 2,padx=5, pady=2)
boton3 = tkinter.Button(Ventana, text ="Reset",command=Reiniciar )
boton3.grid(row=2,column= 2,padx=5, pady=2)


Ventana.mainloop()
