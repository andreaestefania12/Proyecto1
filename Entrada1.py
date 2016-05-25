#Creando vent1 Entrada
vent1=Tk()
vent1.title("Pinball Andrea Timaran")
canv1=canv1(vent1, width=1000, height=600)
fondo = PhotoImage(file="1.gif")
canv1.create_image(450,300,image=fondo)
foto = PhotoImage(file="final.gif")
canv1.create_image(500,280,image=foto)
canv1.pack()

def quitar(vent1):
    vent1.destroy()

def juego():
    quitar(vent1)
    import Proyecto1
  

def regresar():
    quitar(vent1)
    import Principio

    

#Creando campo de Texto
texto=canv1.create_text(190,350,fill="#088A85",font=("Barbieri-Book",20),text="Nombre Jugador : ")
txtUsuario = Entry(vent1,textvariable=" ",width=30,font=("Barbieri-Book",17),bg="white")
txtUsuario.place(x=310,y=340)
nom=txtUsuario.get()

#Boton seguir
botonSeguir=Button(vent1, text='Continuar',font=("Barbieri-Book",22), width=12,command=juego,bg="#A9E2F3").place(x=400,y=415)

#Boton menú principal
botonSalir=Button(vent1, text='Menú principal',font=("Barbieri-Book",22), width=12,command=regresar,bg="#A9E2F3").place(x=400,y=505)


vent1.mainloop()

