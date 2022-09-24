from tkinter import *
import tkinter
import random
from tkinter import messagebox

def Generar_Numero():
    a = Num1.get()
    b = Num2.get()
    if a<b:
        numero_aleatorio = random.randint(a+1,b-1)
        return NumGen.set(numero_aleatorio)
    else:
        numero_aleatorio=0
        return messagebox.showwarning("Error","El primer número debe ser menor que el segundo")

Ventana = tkinter.Tk()
Ventana.title ( "Generador de Numeros" )
Ventana.config ( bg = "lightgrey" )
Num1=IntVar()
Num2=IntVar()
NumGen=IntVar()

etiquet1=Label(Ventana, font=("TimesNewRoman 9") , text ="Número 1")
etiquet1.grid(row=1, column=0,padx=5,pady=5)
etiquet2=Label(Ventana, font=("TimesNewRoman 9") , text ="Número 2")
etiquet2.grid(row=2, column=0,padx=5,pady=5)
etiquet_gen=Label(Ventana, font=("TimesNewRoman 9") , text ="Número Generado")
etiquet_gen.grid(row=3, column=0,padx=5,pady=5)

spinbox1=Spinbox(from_= -1000, to= 1000,textvariable= Num1)
spinbox1.grid(row=1, column=1,padx=5,pady=5)
spinbox2=Spinbox(from_= -1000, to= 1000,textvariable= Num2)
spinbox2.grid(row=2, column=1,padx=5,pady=5)

Generado=Entry(Ventana,textvariable=NumGen,font=("TimesNewRoman 9"))
Generado.grid(row=3,column=1,padx=5,pady=5)

Boton=Button(Ventana,text="Generar",font=("TimesNewRoman 9"),command=Generar_Numero)
Boton.grid(row=4,column=0,columnspan=2,padx=5,pady=2)
Ventana.mainloop()