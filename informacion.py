from tkinter import *

#Creando vent2 Información
vent2=Tk()
vent2.title("Pinball Andrea Timaran")
canv2=Canvas(vent2, width=1000, height=600)
fondo = PhotoImage(file="1.gif")
canv2.create_image(450,300,image=fondo)
infol=canv2.create_text(140,90,text="Objetivo",font=("Barbieri-Book",20),fill="yellow")
info=canv2.create_text(400,150,text="El juego consiste en que el jugador no debe dejar \ncaer la pelota y lograr la máxima puntución posible \n ",font=("Barbieri-Book",20),fill="white")
canv2.pack()
boton = PhotoImage(file="boton4.gif")

def quitar(vent2):
    vent2.destroy()

def menu():
    quitar(vent2)
    import Principio

botonMenu=Button(vent2, text="Regresar al menú",font=("Baribieri-Book",22),width=170,command=menu,bg="#A9E2F3",image=boton).place(x=210,y=470)
vent2.mainloop()
