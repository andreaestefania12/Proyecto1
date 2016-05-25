from tkinter import *
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

def informacion():
    quitar(ventana)
    import informacion

#Crear botones ventana principal
botonJugar=Button(ventana, text=' Jugar',font=("Barbieri-Book",22), width=12,command=funcion,bg="#FFFF00").place(x=150,y=380)
botonSalir=Button(ventana, text='Salir del Juego',font=("Barbieri-Book",22), width=12,command=ventana.destroy,bg="#A9E2F3").place(x=400,y=380)
botonInfo=Button(ventana, text="Información del juego",font=("Baribieri-Book",22),width=19,command=informacion,bg="#A9E2F3").place(x=210,y=470)
ventana.mainloop()


    

    
