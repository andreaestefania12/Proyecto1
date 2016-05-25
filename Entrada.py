from tkinter import *

#Creando ventana
ventana=Tk()
ventana.title("Pinball Andrea Timaran")
canvas=Canvas(ventana, width=1000, height=600)
fondo = PhotoImage(file="1.gif")
canvas.create_image(450,300,image=fondo)
foto = PhotoImage(file="final.gif")
canvas.create_image(500,280,image=foto)
canvas.pack()

def quitar(ventana):
    ventana.destroy()

def juego():
    quitar(ventana)
    import Proyecto1
    

def regresar():
    quitar(ventana)
    import Principio

    

#Creando campo de Texto
texto=canvas.create_text(190,350,fill="#088A85",font=("Barbieri-Book",20),text="Nombre Jugador : ")
txtUsuario = Entry(ventana,textvariable=" ",width=30,font=("Barbieri-Book",17),bg="white")
txtUsuario.place(x=310,y=340)
nom=txtUsuario.get()

#Boton seguir
botonSeguir=Button(ventana, text='Continuar',font=("Barbieri-Book",22), width=12,command=juego,bg="#A9E2F3").place(x=400,y=415)

#Boton menú principal
botonSalir=Button(ventana, text='Menú principal',font=("Barbieri-Book",22), width=12,command=regresar,bg="#A9E2F3").place(x=400,y=505)


ventana.mainloop()
