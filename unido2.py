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
