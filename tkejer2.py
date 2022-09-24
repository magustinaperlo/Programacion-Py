from tkinter import *
import tkinter


Ventana = tkinter.Tk()
Ventana.title ( "Contador Decrece" )
Ventana.config ( bg = "lightgrey" )

def Menos():
    num=int(Barra_de_Num ["text"])
    Barra_de_Num ["text"] = f"{num-1}"

etiquet=Label(Ventana,font=("TimesNewRoman 9") ,text = "Contador")
etiquet.grid(row=2,column= 0,padx=5, pady=2)

Barra_de_Num= Label(Ventana,font=("TimesNewRoman 9") ,text = "88" ,)
Barra_de_Num.grid(row=2,column= 1,padx=5, pady=2)

boton1 = tkinter.Button(Ventana,font=("TimesNewRoman 9") , text ="-",command=Menos)
boton1.grid(row=2,column= 2,padx=5, pady=2)




Ventana.mainloop()
