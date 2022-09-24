from tkinter import *
import tkinter
i=0 

Ventana = tkinter.Tk()
Ventana.title ( "Calculadora" )
Ventana.config ( bg = "lightgrey" )


etiquetN=Entry(Ventana, font = ("Calibri 20"))
etiquetN.grid(row=0,column=0,columnspan=4, padx=5,pady=5)

def click_button(valor):
    global i
    etiquetN.insert(i,valor)
    i +=1

def Delete():
    etiquetN.delete(0, END)
    i= 0 
def Ecuacion():
    ecuacion =etiquetN.get()
    reslutado_ecuacion = eval(ecuacion)
    etiquetN.delete(0, END)
    etiquetN.insert(0, reslutado_ecuacion)
    i=0
#Botones
Boton_Delete = Button(Ventana, text = "DELETE", width =5, height =2, command= lambda:Delete())
Boton1= Button(Ventana, text = "1", width =5, height =2, command= lambda:click_button(1))
Boton2= Button(Ventana, text = "2", width =5, height =2, command= lambda:click_button(2))
Boton3= Button(Ventana, text = "3", width =5, height =2, command= lambda:click_button(3))
Boton4= Button(Ventana, text = "4", width =5, height =2, command= lambda:click_button(4))
Boton5= Button(Ventana, text = "5", width =5, height =2, command= lambda:click_button(5))
Boton6= Button(Ventana, text = "6", width =5, height =2, command= lambda:click_button(6))
Boton7= Button(Ventana, text = "7", width =5, height =2, command= lambda:click_button(7))
Boton8= Button(Ventana, text = "8", width =5, height =2, command= lambda:click_button(8))
Boton9= Button(Ventana, text = "9", width =5, height =2, command= lambda:click_button(9))
Boton0= Button(Ventana, text = "0", width =13, height =2, command= lambda:click_button(0))
Boton_Suma= Button(Ventana, text = "+", width =5, height =2, command= lambda:click_button("+"))
Boton_Resta= Button(Ventana, text = "-", width =5, height =2, command= lambda:click_button("-"))
Boton_Mult= Button(Ventana, text = "x", width =5, height =2, command= lambda:click_button("x"))
Boton_Div= Button(Ventana, text = "/", width =5, height =2, command= lambda:click_button("/"))
Boton_Igual= Button(Ventana, text = "=", width =13, height =2, command= lambda:Ecuacion())
Boton_Delete.grid(row=1, column=0,padx=5, pady= 5)
Boton1.grid(row=4, column=0,padx=5, pady= 5)
Boton2.grid(row=4, column=1,padx=5, pady= 5)
Boton3.grid(row=4, column=2,padx=5, pady= 5)
Boton4.grid(row=3, column=0,padx=5, pady= 5)
Boton5.grid(row=3, column=1,padx=5, pady= 5)
Boton6.grid(row=3, column=2,padx=5, pady= 5)
Boton7.grid(row=2, column=0,padx=5, pady= 5)
Boton8.grid(row=2, column=1,padx=5, pady= 5)
Boton9.grid(row=2, column=2,padx=5, pady= 5)
Boton0.grid(row=5, column=0,columnspan=2,padx=5, pady= 5)
Boton_Suma.grid(row=2, column=3,padx=5, pady= 5)
Boton_Resta.grid(row=1, column=3,padx=5, pady= 5)
Boton_Mult.grid(row=1, column=2,padx=5, pady= 5)
Boton_Div.grid(row=1, column=1,padx=5, pady= 5)
Boton_Igual.grid(row=5, column=2,columnspan=2 ,padx=5, pady= 5)

Ventana.mainloop()