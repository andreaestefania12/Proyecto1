from tkinter import *
import random
import time

#Crear ventana Principal
ventana=Tk()
ventana.title("Pinball Andrea Timaran")
canvas=Canvas(ventana, width=1000, height=600)
fondo = PhotoImage(file="1.gif")
canvas.create_image(450,300,image=fondo)
foto = PhotoImage(file="final.gif")
canvas.create_image(500,300,image=foto)
canvas.pack()


def quitar(ventana):
    ventana.destroy()

def funcion():
    quitar(ventana)
    import Entrada

def esc_vent():
    ventana.withdraw()
    vent2.deiconify()

#Creando vent2 Información
vent2=Toplevel(ventana)
vent2.title("Pinball Andrea Timaran")
canv2=Canvas(vent2, width=1000, height=600)
fondo = PhotoImage(file="1.gif")
canv2.create_image(450,300,image=fondo, anchor="center")
infol=canv2.create_text(140,100,text="Objetivo",font=("Barbieri-Book",20),fill="yellow")
info=canv2.create_text(400,150,text="El juego consiste en que el jugador no debe dejar \ncaer la pelota y lograr la máxima puntución posible",font=("Barbieri-Book",20),fill="white")
canv2.pack(fill='none')


#Crear botones ventana principal
botonJugar=Button(ventana, text=' Jugar',font=("Barbieri-Book",22), width=12,command=funcion,bg="#FFFF00").place(x=150,y=380)
botonSalir=Button(ventana, text='Salir del Juego',font=("Barbieri-Book",22), width=12,command=ventana.destroy,bg="#A9E2F3").place(x=400,y=380)
botonInfo=Button(ventana, text="Información del juego",font=("Baribieri-Book",22),width=19,command= esc_vent,bg="#A9E2F3").place(x=210,y=470)
vent2.withdraw()
ventana.mainloop()

