from ast import Num
import math
from tkinter import *
import tkinter


Ventana = tkinter.Tk()

Ventana.title ( "Factorial" )
Ventana.config ( bg = "lightgrey" )

def Calcular():
    Cal=int(num.get())+1
    Barra_de_Num_Fac.config(text= math.factorial(Cal))
    for i in range(Cal):
        num.set(Cal)

etiquet=Label(Ventana, font=("TimesNewRoman 9") ,text = "n: ")
etiquet.grid(row=2,column= 0,padx=5, pady=2)

num=IntVar(value=0)
Barra_de_Num= Entry(Ventana,font=("TimesNewRoman 9") ,text = "0" ,textvariable=num,state= "readonly")
Barra_de_Num.grid(row=2,column= 1,padx=5, pady=2)

etiquet=Label(Ventana,font=("TimesNewRoman 9") , text = "Factorial de n: ")
etiquet.grid(row=4,column= 0,padx=5, pady=2)

Barra_de_Num_Fac= Label(Ventana,font=("TimesNewRoman 9") ,text = "0" ,)
Barra_de_Num_Fac.grid(row=4,column=1,padx=5, pady=2)

boton1 = tkinter.Button(Ventana,font=("TimesNewRoman 9") , text ="siguiente",command=Calcular )
boton1.grid(row=3,column= 0,padx=5, pady=2)

Ventana.mainloop()
