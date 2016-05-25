from tkinter import *

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
  
def 


#Ventana de juego 
vent2=Toplevel(ventana)
vent2.title("Pinball Andrea Timaran")
canva= Canvas(vent2,width=1000,height=600)
fondo = PhotoImage(file="1.gif")
