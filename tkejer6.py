from tkinter import *
import tkinter


Ventana = tkinter.Tk()
Ventana.title ( "Peliculas" )
Ventana.config ( bg = "lightgrey" )

def limpiar():
    pelicula.set("")

def enviar():   
    lista_peliculas.insert(END,pelicula.get())
    limpiar()

pelicula = StringVar()

Añadir=Label(Ventana,font=("TimesNewRoman 9") , text = "Titulos de peliculas para ver")
Añadir.grid(row=1,column= 1,columnspan=2,padx=5, pady=2)

etiquetN=Entry(Ventana,textvariable=pelicula, font = ("TimesNewRoman 9 "))
etiquetN.grid(row=2,column=1,columnspan=2, padx=5,pady=5)



Boton=Button(Ventana,font=("TimesNewRoman 9") , text = "Añadir",command= enviar)
Boton.grid(row=3, column=1,padx=5, pady=2)

Lista=Label(Ventana,font=("TimesNewRoman 9") , text = "Peliculas")
Lista.grid(row=1,column= 3,columnspan=2 ,padx=5, pady=2)

lista_peliculas = Listbox(Ventana,width = 30 )
lista_peliculas.grid (row=3,column = 3, padx=5,pady=5)

Ventana.mainloop()