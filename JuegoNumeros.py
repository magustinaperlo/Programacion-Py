from tkinter import *
from tkinter import messagebox
def arranque():
    Ventana_0 = Tk()
    Ventana_0.title("Juego Matematico")
    Ventana_0.config(bg="black")

    def iniciar():
        Ventana_0.withdraw()
        Ventana = Tk()
        Ventana.title("Juego Matematico")
        Ventana.config(bg="black")
        def volver_a_jugar():
            abrir_Ventana2()
        def abrir_Ventana2():
            Ventana.withdraw() 
            Ventana2 = Toplevel() 
            width= Ventana2.winfo_screenwidth()
            Ventana2.config(bg= "black")
            def Ingles():
                Ventana2.withdraw()
                Ventana3 = Toplevel()
                Ventana3.config(bg="black")
                def ordenar():
                    Ventana3.withdraw()
                    Ventana4 = Toplevel()   
                    Ventana4.config(bg="black")
                    def mayor():
                        Ventana4.withdraw()
                        Ventana5 = Toplevel()
                        Ventana5.config(bg="black")
                        def Validar_Resta():
                                try:
                                    valor2 = resto_de_resta.get()
                                    if valor2!="0" and valor2!= "" and valor2.isnumeric():
                                        return True
                                    else:
                                        messagebox.showwarning("Error","You must enter a numeric value")
                                        return False
                                except:
                                    messagebox.showwarning("Error","You must enter a numeric value")
                        def seguir():
                            if Validar_Resta():
                                Ventana5.withdraw()
                                Ventana6 = Toplevel()
                                Ventana6.config(bg="black")
                                def Validar_Suma():
                                    try:
                                        valor1 = resto_de_suma.get()
                                        if valor1!="0" and valor1!= ""and valor1.isnumeric():
                                            return True
                                        else:
                                            messagebox.showwarning("Error","You must enter a numeric value")
                                            return False
                                    except:
                                        messagebox.showwarning("Error","You must enter a numeric value")
                                def adivinar():
                                    if Validar_Suma():
                                        Ventana6.withdraw()
                                        Ventana7 = Toplevel()
                                        Ventana7.config(bg="black") 

                                        def salir():
                                            Ventana7.withdraw()
                                            Ventana8 = Toplevel()
                                            Ventana8.config(bg="black")
                                            Etiqueta_saludo = Label(Ventana8, text = "thanks for playing!",font=("TimesNewRoman 9",), bg ="lime" )
                                            Etiqueta_saludo.grid(row=0,column=0,padx=5,pady=2)
                                            boton_inicio = Button(Ventana8, command = arranque, text = "RESTART", font = ("TimesNewRoman 9"),  bg = "lime")
                                            boton_inicio.grid(row=4,column=1,padx=5,pady=2)
                                            Ventana8.mainloop()
                                        def numero_oculto():    
                                            k = int(resto_de_resta.get())/9
                                            digito1 = (int(resto_de_suma.get()) - k)/2
                                            digito2 = (int(resto_de_suma.get()) + k)/ 2
                                            var = str(int(digito1))+str(int(digito2))
                                            return numero.set(var)
                                        Etiqueta11 = Label(Ventana7,text = "The number is",font= ("TimesNewRoman 9"), bg ="lime" )
                                        Etiqueta11.grid(row=0,column=0,padx=5,pady=2)
                                        numero = IntVar(value="")
                                        Etiqueta12 = Entry(Ventana7, textvariable= numero ,justify= "center",font= ("TimesNewRoman 9",), bg ="lime", fg ="lime" , state= "readonly" )
                                        Etiqueta12.grid(row=2,column=0,padx=5,pady=2)
                                        boton_ver = Button(Ventana7, command = numero_oculto, text = "Press to see it!!! ", font = ("TimesNewRoman 9"),  bg = "lime")
                                        boton_ver.grid(row=4,column=1,padx=5,pady=2)
                                        boton_jugar_nuevo = Button(Ventana7, command = volver_a_jugar, text = "Play again", font = ("TimesNewRoman 9"),  bg = "lime")
                                        boton_jugar_nuevo.grid(row=4,column=2,columnspan=2,padx=5,pady=2)
                                        boton_salir = Button(Ventana7, command = salir, text = "Exit", font = ("TimesNewRoman 9"),  bg = "lime")
                                        boton_salir.grid(row=4,column=3,padx=5,pady=2)
                                        Ventana7.mainloop()

                                Etiqueta8 = Label(Ventana6,text = "Now add the numbers of the number \n you thought at the beginning. .",font= ("TimesNewRoman 9"), bg ="lime" )
                                Etiqueta8.grid(row=0,column=0,padx=5,pady=2)
                                Etiqueta9 = Label(Ventana6,text = "Write the result here:",font= ("TimesNewRoman 9"), bg ="lime" )
                                Etiqueta9.grid(row=2,column=0,padx=5,pady=2)
                                resto_de_suma = Entry(Ventana6, font= ("TimesNewRoman 9"),bg = "lime")
                                resto_de_suma.grid(row=3,column=1,padx=5,pady=2)
                                boton_adivinar = Button(Ventana6, command = adivinar, text = "If you press here\n I tell you what number you thought!!! ", font = ("TimesNewRoman 9"),  bg = "lime")
                                boton_adivinar.grid(row=4,column=1,columnspan=2,padx=5,pady=2)
                                Ventana6.mainloop()

                        Etiqueta6 = Label(Ventana5,text ="So, subtract from the new \n number the one you thought of.",font= ("TimesNewRoman 9"), bg ="lime" )
                        Etiqueta6.grid(row=0,column=0,padx=5,pady=2)
                        Etiqueta7 = Label(Ventana5,text = "Write the result here:",font= ("TimesNewRoman 9"), bg ="lime" )
                        Etiqueta7.grid(row=2,column=0,padx=5,pady=2)
                        resto_de_resta = Entry(Ventana5, font= ("TimesNewRoman 9"),bg = "lime")
                        resto_de_resta.grid(row=3,column=1,columnspan=2,padx=5,pady=2)
                        boton_siguiente = Button(Ventana5, command = seguir, text = " CONTINUE ",font = ("TimesNewRoman 9"),  bg = "lime")
                        boton_siguiente.grid(row=4,column=1,columnspan=2,padx=5,pady=2)
                        Ventana5.mainloop()

                    def menor():
                        Ventana4.withdraw()
                        Ventana8 = Toplevel()
                        Ventana8.config(bg="black")
                        def Validar_Resta():
                                try:
                                    valor2 = resto_de_resta.get()
                                    if valor2!="0" and valor2!= ""and valor2.isnumeric():
                                        return True
                                    elif valor2 == "0":
                                            messagebox.showwarning("Error","You must enter a number other than zero")    
                                    else:    
                                        messagebox.showwarning("Error","You must enter a numeric value")
                                        return False
                                except:
                                    messagebox.showwarning("Error","You must enter a numeric value")
                        def seguir():
                            if Validar_Resta():
                                Ventana8.withdraw()
                                Ventana9 = Toplevel()
                                Ventana9.config(bg="black")
                                def Validar_Suma():
                                        try:
                                            valor1 = resto_de_suma.get()
                                            if valor1!="0" and valor1!= ""and valor1.isnumeric():
                                                return True
                                            elif valor1 == "0":
                                                messagebox.showwarning("Error","You must enter a number other than zero")    
                                            else:    
                                                messagebox.showwarning("Error","You must enter a numeric value")
                                                return False
                                        except:
                                            messagebox.showwarning("Error","You must enter a numeric value")
                                def adivinar():
                                    if Validar_Suma():
                                        Ventana9.withdraw()
                                        Ventana10 = Toplevel()
                                        Ventana10.config(bg="black")
                                        def salir():
                                            Ventana10.withdraw()
                                            Ventana11 = Toplevel()
                                            Ventana11.config(bg="black")
                                            Etiqueta_saludo = Label(Ventana11, text = "thanks for playing",font=("TimesNewRoman 9",), bg ="lime" )
                                            Etiqueta_saludo.grid(row=0,column=0,padx=5,pady=2)
                                            boton_inicio = Button(Ventana11, command = arranque, text = "Restart", font = ("TimesNewRoman 9"),  bg = "lime")
                                            boton_inicio.grid(row=4,column=1,padx=5,pady=2)
                                            Ventana11.mainloop()
                                        def numero_oculto():
                                            k = int(resto_de_resta.get())/9
                                            digito1 = (int(resto_de_suma.get()) + k)/2
                                            digito2 = (int(resto_de_suma.get()) - k)/ 2
                                            var = str(int(digito1))+str(int(digito2))
                                            return numero.set(var)
                                        Etiqueta_11 = Label(Ventana10,text = "The number is",font= ("TimesNewRoman 9"), bg ="lime" )
                                        Etiqueta_11.grid(row=0,column=0,padx=5,pady=2)
                                        numero = IntVar(value="")
                                        Etiqueta_12 = Entry(Ventana10, textvariable= numero ,justify= "center",font= ("TimesNewRoman 9",), bg ="lime", fg ="lime" )
                                        Etiqueta_12.grid(row=2,column=0,padx=5,pady=2)
                                        boton_ver = Button(Ventana10, command = numero_oculto, text = "Press to see it ", font = ("TimesNewRoman 9"),  bg = "lime")
                                        boton_ver.grid(row=4,column=1,padx=5,pady=2)
                                        boton_jugar_nuevo = Button(Ventana10, command = volver_a_jugar, text = "Play again", font = ("TimesNewRoman 9"),  bg = "lime")
                                        boton_jugar_nuevo.grid(row=4,column=2,columnspan=2,padx=5,pady=2)
                                        boton_salir = Button(Ventana10, command = salir, text = "Exit", font = ("TimesNewRoman 9"),  bg = "lime")
                                        boton_salir.grid(row=4,column=3,padx=5,pady=2)
                                        Ventana10.mainloop()
                                Etiqueta_8 = Label(Ventana9,text = "Now, add up the digits of the number \n you thought of at first.",font= ("TimesNewRoman 9"), bg ="lime" )
                                Etiqueta_8.grid(row=0,column=0,padx=5,pady=2)
                                Etiqueta_9 = Label(Ventana9,text = "Write the result here:",font= ("TimesNewRoman 9"), bg ="lime" )
                                Etiqueta_9.grid(row=1,column=0,padx=5,pady=2)
                                resto_de_suma = Entry(Ventana9, font= ("TimesNewRoman 9"),bg = "lime")
                                resto_de_suma.grid(row=3,column=1,padx=5,pady=2)
                                boton_adivinar = Button(Ventana9, command = adivinar, text = "If you press here\n I tell you what number you thought!!! ", font = ("TimesNewRoman 9"),  bg = "lime")
                                boton_adivinar.grid(x=250, y= 450)
                                Ventana9.mainloop()

                        Etiqueta_6 = Label(Ventana8,text = "So, subtract the number you \n thought first from the new number",font= ("TimesNewRoman 9"), bg ="lime" )
                        Etiqueta_6.grid(row=4,column=1,padx=5,pady=2)
                        Etiqueta_7 = Label(Ventana8,text = "Write the result here:",font= ("TimesNewRoman 9"), bg ="lime" )
                        Etiqueta_7.grid(row=4,column=1,padx=5,pady=2)
                        resto_de_resta = Entry(Ventana8, font= ("TimesNewRoman 9"),bg = "lime")
                        resto_de_resta.grid(row=4,column=1,padx=5,pady=2)
                        boton_siguiente = Button(Ventana8, command = seguir, text = " Continue ",font = ("TimesNewRoman 9"),  bg = "lime")
                        boton_siguiente.grid(row=4,column=1,padx=5,pady=2)
                        Ventana8.mainloop()

                    Etiqueta_5 = Label(Ventana4,text = "Now reverse the order of the figures",font= ("TimesNewRoman 9"), bg ="lime" )
                    Etiqueta_5.grid(row=0,column=1,padx=5,pady=2)            
                    Etiqueta5a = Label(Ventana4,text = "Is the new number higher or lower than the first?",font= ("TimesNewRoman 9"), bg ="lime" )
                    Etiqueta5a.grid(row=2,column=1,padx=5,pady=2)
                    boton_mayor = Button(Ventana4, command = mayor, text = " Higher ",font = ("TimesNewRoman 9"),  bg = "lime")
                    boton_mayor.grid(row=4,column=1,padx=5,pady=2)
                    boton_menor = Button(Ventana4, command = menor, text = " Lower ",font = ("TimesNewRoman 9"),  bg = "lime")
                    boton_menor.grid(row=4,column=3,padx=5,pady=2)
                    Ventana4.mainloop()

                Etiqueta3 = Label(Ventana3, text = "Think of a two-digit number (not equal). ",font= ("TimesNewRoman 9"), bg ="lime" )
                Etiqueta3.grid(row=0,column=1,padx=5,pady=2)
                Etiqueta4 = Label(Ventana3, text = "Ready, Press continue",font= ("TimesNewRoman 9"), bg ="lime" )
                Etiqueta4.grid(row=2,column=1,padx=5,pady=2)
                boton_siguiente = Button(Ventana3, command = ordenar, text = " Continue ",font = ("TimesNewRoman 9"),  bg = "lime")
                boton_siguiente.grid(row=4,column=1,padx=5,pady=2)
                Ventana3.mainloop()    
            def Español():
                Ventana2.withdraw()
                Ventana3 = Toplevel()
                Ventana3.config(bg="black")
                def ordenar():
                    Ventana3.withdraw()
                    Ventana4 = Toplevel()
                    Ventana4.config(bg="black")
                    def mayor():
                        Ventana4.withdraw()
                        Ventana5 = Toplevel()
                        Ventana5.config(bg="black")
                        def Validar_Resta():
                                try:
                                    valor2 = resto_de_resta.get()
                                    if valor2!="0" and valor2!= ""and valor2.isnumeric():
                                        return True
                                    elif valor2 =="0":
                                        messagebox.showwarning("Error","Debe ingresar un número distinto de cero")
                                    else:
                                        messagebox.showwarning("Error","Debe ingresar un valor numérico")
                                        return False
                                except:
                                    messagebox.showwarning("Error","Debe ingresar un valor numérico")
                        def seguir():
                            if Validar_Resta():
                                Ventana5.withdraw()
                                Ventana6 = Toplevel()
                                Ventana6.config(bg="black")
                                def Validar_Suma():
                                    try:
                                        valor1 = resto_de_suma.get()
                                        if valor1!="0" and valor1!= ""and valor1.isnumeric():
                                            return True
                                        elif valor1 =="0":
                                            messagebox.showwarning("Error","Debe ingresar un número distinto de cero")
                                        else:
                                            messagebox.showwarning("Error","Debe ingresar un valor numérico")
                                            return False
                                    except:
                                        messagebox.showwarning("Error","Debe ingresar un valor numérico")
                                def adivinar():
                                    if Validar_Suma():
                                        Ventana6.withdraw()
                                        Ventana7 = Toplevel()
                                        Ventana7.config(bg="black") 
                                        def salir():
                                            Ventana7.withdraw()
                                            Ventana8 = Toplevel()
                                            Ventana8.config(bg="black")
                                            Etiqueta_saludo = Label(Ventana8, text = "Gracias por jugar!!!",font=("TimesNewRoman 9",), bg ="lime" )
                                            Etiqueta_saludo.grid(row=0,column=0,padx=5,pady=2)
                                            boton_inicio = Button(Ventana8, command = arranque, text = "Reiniciar", font = ("TimesNewRoman 9"),  bg = "lime")
                                            boton_inicio.grid(row=4,column=1,padx=5,pady=2)
                                            Ventana8.mainloop()

                                        def numero_oculto():    
                                            k = int(resto_de_resta.get())/9
                                            digito1 = (int(resto_de_suma.get()) - k)/2
                                            digito2 = (int(resto_de_suma.get()) + k)/ 2
                                            var = str(int(digito1))+str(int(digito2))
                                            return numero.set(var)
                                        Etiqueta11 = Label(Ventana7,text = "El número es",font= ("TimesNewRoman 9"), bg ="lime" )
                                        Etiqueta11.grid(row=0,column=0,padx=5,pady=2)
                                        numero = IntVar(value="")
                                        Etiqueta12 = Entry(Ventana7, textvariable= numero ,justify= "center",font= ("TimesNewRoman 9"), bg ="lime", fg ="lime" , state= "readonly" )
                                        Etiqueta12.grid(row=0,column=0,padx=5,pady=2)
                                        boton_ver = Button(Ventana7, command = numero_oculto, text = "Presiona para ver el numero", font = ("TimesNewRoman 9"),  bg = "lime")
                                        boton_ver.grid(row=4,column=1,padx=5,pady=2)
                                        boton_jugar_nuevo = Button(Ventana7, command = volver_a_jugar, text = "Volver a jugar", font = ("TimesNewRoman 9"),  bg = "lime")
                                        boton_jugar_nuevo.grid(row=4,column=2,padx=5,pady=2)
                                        boton_salir = Button(Ventana7, command = salir, text = "salir", font = ("TimesNewRoman 9"),  bg = "lime")
                                        boton_salir.grid(row=4,column=3,padx=5,pady=2)
                                        Ventana7.mainloop()

                                Etiqueta8 = Label(Ventana6,text = "Ahora, sumá las cifras del número \n que pensaste al principio.",font= ("TimesNewRoman 9"), bg ="lime" )
                                Etiqueta8.grid(row=0,column=0,padx=5,pady=2)
                                Etiqueta9 = Label(Ventana6,text = "Escribí el resultado aquí",font= ("TimesNewRoman 9"), bg ="lime" )
                                Etiqueta9.grid(row=2,column=0,padx=5,pady=2)
                                resto_de_suma = Entry(Ventana6, font= ("TimesNewRoman 9"),bg = "lime")
                                resto_de_suma.grid(row=3,column=1,columnspan=2,padx=5,pady=2)
                                boton_adivinar = Button(Ventana6, command = adivinar, text = "Si presionas aquí\n te digo qué número pensaste!!! ", font = ("TimesNewRoman 9"),  bg = "lime")
                                boton_adivinar.grid(row=4,column=1,columnspan=2,padx=5,pady=2)
                                Ventana6.mainloop()

                        Etiqueta6 = Label(Ventana5,text = "Entonces, restale al nuevo número el que pensaste.",font= ("TimesNewRoman 9"), bg ="lime" )
                        Etiqueta6.grid(row=0,column=0,padx=5,pady=2)
                        Etiqueta7 = Label(Ventana5,text = "Escribí el resultado aquí:",font= ("TimesNewRoman 9"), bg ="lime" )
                        Etiqueta7.grid(row=2,column=0,padx=5,pady=2)
                        resto_de_resta = Entry(Ventana5, font= ("TimesNewRoman 9"),bg = "lime")
                        resto_de_resta.grid(row=3,column=1,columnspan=2,padx=5,pady=2)
                        boton_siguiente = Button(Ventana5, command = seguir, text = " Siguiente ",font = ("TimesNewRoman 9"),  bg = "lime")
                        boton_siguiente.grid(row=4,column=1,columnspan=2,padx=5,pady=2)
                        Ventana5.mainloop()

                    def menor():
                        Ventana4.withdraw()
                        Ventana8 = Toplevel()
                        Ventana8.config(bg="black")
                        def Validar_Resta():
                                try:
                                    valor2 = resto_de_resta.get()
                                    if valor2!="0" and valor2!= ""and valor2.isnumeric():
                                        return True
                                    elif valor2 =="0":
                                        messagebox.showwarning("Error","Debe ingresar un número distinto de cero")
                                    else:
                                        messagebox.showwarning("Error","Debe ingresar un valor numérico")
                                        return False
                                except:
                                    messagebox.showwarning("Error","Debe ingresar un valor numérico")
                        def seguir():
                            if Validar_Resta():
                                Ventana8.withdraw()
                                Ventana9 = Toplevel()
                                Ventana9.config(bg="black")
                                def Validar_Suma():
                                        try:
                                            valor1 = resto_de_suma.get()
                                            if valor1!="0" and valor1!= ""and valor1.isnumeric():
                                                return True
                                            elif valor1 =="0":
                                                messagebox.showwarning("Error","Debe ingresar un número distinto de cero")
                                            else:
                                                messagebox.showwarning("Error","Debe ingresar un valor numérico")
                                                return False
                                        except:
                                            messagebox.showwarning("Error","Debe ingresar un valor numérico")
                                def adivinar():
                                    if Validar_Suma():
                                        Ventana9.withdraw()
                                        Ventana10 = Toplevel()
                                        Ventana10.config(bg="black")
                                        def salir():
                                            Ventana10.withdraw()
                                            Ventana11 = Toplevel()
                                            Ventana11.config(bg="black")
                                            Etiqueta_saludo = Label(Ventana11, text = "Gracias por jugar!!!",font=("TimesNewRoman 9",), bg ="lime" )
                                            Etiqueta_saludo.grid(row=0,column=0,padx=5,pady=2)
                                            boton_inicio = Button(Ventana11, command = arranque, text = "Reiniciar", font = ("TimesNewRoman 9"),  bg = "lime")
                                            boton_inicio.grid(row=4,column=1,padx=5,pady=2)
                                            Ventana11.mainloop()
                                        def numero_oculto():
                                            k = int(resto_de_resta.get())/9
                                            digito1 = (int(resto_de_suma.get()) + k)/2
                                            digito2 = (int(resto_de_suma.get()) - k)/ 2
                                            var = str(int(digito1))+str(int(digito2))
                                            return numero.set(var)
                                        Etiqueta_11 = Label(Ventana10,text = "El número es",font= ("TimesNewRoman 9"), bg ="lime" )
                                        Etiqueta_11.grid(row=0,column=0,padx=5,pady=2)
                                        numero = IntVar(value="")
                                        Etiqueta_12 = Entry(Ventana10, textvariable= numero ,justify= "center",font= ("TimesNewRoman 9",), bg ="lime", fg ="lime" , state= "readonly" )
                                        Etiqueta_12.grid(row=2,column=0,padx=5,pady=2)
                                        boton_ver = Button(Ventana10, command = numero_oculto, text = "Presioná para ver el numero ", font = ("TimesNewRoman 9"),  bg = "lime")
                                        boton_ver.grid(row=4,column=1,padx=5,pady=2)
                                        boton_jugar_nuevo = Button(Ventana10, command = volver_a_jugar, text = "Volver a jugar", font = ("TimesNewRoman 9"),  bg = "lime")
                                        boton_jugar_nuevo.grid(row=4,column=2,columnspan=2,padx=5,pady=2)
                                        boton_salir = Button(Ventana10, command = salir, text = "salir", font = ("TimesNewRoman 9"),  bg = "lime")
                                        boton_salir.grid(row=4,column=3,padx=5,pady=2)
                                        Ventana10.mainloop()
                                Etiqueta_8 = Label(Ventana9,text = "Ahora, sumá las cifras del número \n que pensaste al principio.",font= ("TimesNewRoman 9"), bg ="lime" )
                                Etiqueta_8.grid(row=0,column=0,padx=5,pady=2)
                                Etiqueta_9 = Label(Ventana9,text = "Escribí el resultado aquí",font= ("TimesNewRoman 9"), bg ="lime" )
                                Etiqueta_9.grid(row=1,column=0,padx=5,pady=2)
                                resto_de_suma = Entry(Ventana9, font= ("TimesNewRoman 9"),bg = "lime")
                                resto_de_suma.grid(row=3,column=1,columnspan=2,padx=5,pady=2)
                                boton_adivinar = Button(Ventana9, command = adivinar, text = "Si presionas aquí\n adivino tu numero ", font = ("TimesNewRoman 9"),  bg = "lime")
                                boton_adivinar.grid(row=4,column=1,columnspan=2,padx=5,pady=2)
                                Ventana9.mainloop()

                        Etiqueta_6 = Label(Ventana8,text = "Entonces, restale al número que pensaste el nuevo número.",font= ("TimesNewRoman 9"), bg ="lime" )
                        Etiqueta_6.grid(row=0,column=0,padx=5,pady=2)
                        Etiqueta_7 = Label(Ventana8,text = "Escribí el resultado aquí",font= ("TimesNewRoman 9"), bg ="lime" )
                        Etiqueta_7.grid(row=2,column=0,padx=5,pady=2)
                        resto_de_resta = Entry(Ventana8, font= ("TimesNewRoman 9"),bg = "lime")
                        resto_de_resta.grid(row=3,column=1,columnspan=2,padx=5,pady=2)
                        boton_siguiente = Button(Ventana8, command = seguir, text = " Seguir",font = ("TimesNewRoman 9"),  bg = "lime")
                        boton_siguiente.grid(row=4,column=1,columnspan=2,padx=5,pady=2)
                        Ventana8.mainloop()

                    Etiqueta_5 = Label(Ventana4,text = "Invertí el orden de las cifras",font= ("TimesNewRoman 9"), bg ="lime" )
                    Etiqueta_5.grid(row=0,column=0,padx=5,pady=2)            
                    Etiqueta5a = Label(Ventana4,text = "El nuevo número es mayor o menor que el primero?",font= ("TimesNewRoman 9"), bg ="lime" )
                    Etiqueta5a.grid(row=2,column=0,padx=5,pady=2)
                    boton_mayor = Button(Ventana4, command = mayor, text = " Mayor ",font = ("TimesNewRoman 9"),  bg = "lime")
                    boton_mayor.grid(row=4,column=1,padx=5,pady=2)
                    boton_menor = Button(Ventana4, command = menor, text = " Menor ",font = ("TimesNewRoman 9"),  bg = "lime")
                    boton_menor.grid(row=4,column=3,padx=5,pady=2)
                    Ventana4.mainloop()

                Etiqueta3 = Label(Ventana3, text = "Pensá un número de dos cifras (que no sean iguales)",font= ("TimesNewRoman 9"), bg ="lime" )
                Etiqueta3.grid(row=0,column=1,padx=5,pady=2)
                Etiqueta4 = Label(Ventana3, text = "Presiona seguiente",font= ("TimesNewRoman 9"), bg ="lime" )
                Etiqueta4.grid(row=2,column=1,padx=5,pady=2)
                boton_siguiente = Button(Ventana3, command = ordenar, text = " Seguiente ",font = ("TimesNewRoman 9"),  bg = "lime")
                boton_siguiente.grid(row=4,column=1,columnspan=2,padx=5,pady=2)
                Ventana3.mainloop()

            Etiqueta2 = Label(Ventana2,text = "Elegi el idioma",font= ("TimesNewRoman 9"), bg ="lime" )
            Etiqueta2.grid(row=0,column=1,padx=5,pady=2)
            boton_Ingles = Button(Ventana2, command = Ingles, text = " Ingles ",font = ("TimesNewRoman 9"),  bg = "lime")
            boton_Ingles.grid(row=4,column=1,padx=5,pady=2)
            boton_Español = Button(Ventana2, command = Español, text = " Español ",font = ("TimesNewRoman 9"),  bg = "lime")
            boton_Español.grid(row=3,column=1,padx=5,pady=2)
            Ventana2.mainloop()

        Etiqueta = Label(Ventana,text = "Se en que numero piensas",font= ("TimesNewRoman 9"), bg ="lime" )
        Etiqueta.grid(row=2,column=1,padx=5,pady=2)
        Etiqueta1 = Label(Ventana,text = "Si querés jugar, presioná el boton",font= ("TimesNewRoman 9"), bg ="lime" )
        Etiqueta1.grid(row=3,column=1,padx=5,pady=2)
        boton_jugar = Button(Ventana, command = abrir_Ventana2, text = " JUGAR ",font = ("TimesNewRoman 9"),  bg = "lime")
        boton_jugar.grid(row=4,column=1,columnspan=2,padx=5,pady=2)
        Ventana.mainloop()
    Etiqueta_bienvenido = Label(Ventana_0, text = "Quieres jugar un juego matematico\n Presiona Comenzar",font=("TimesNewRoman 9",), bg ="lime" )
    Etiqueta_bienvenido.grid(row=0,column=0,columnspan=4,padx=2,pady=2)
    boton_jugar_nuevo = Button(Ventana_0, command = iniciar, text = "Comenzar",font = ("TimesNewRoman 9"),  bg = "lime")
    boton_jugar_nuevo.grid(row=4,column=1,columnspan=2,padx=5,pady=2)

    Ventana_0.mainloop()
arranque()