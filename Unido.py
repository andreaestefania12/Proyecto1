from tkinter import *
import random
import time

#Creando ventana
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
    
    #Creando ventana
    vent1=Tk()
    vent1.title("Pinball Andrea Timaran")
    canvas=Canvas(vent1, width=1000, height=600)
    fondo = PhotoImage(file="1.gif")
    canvas.create_image(450,300,image=fondo)
    foto = PhotoImage(file="final.gif")
    canvas.create_image(500,280,image=foto)
    canvas.pack()

    def quitar(vent1):
        vent1.destroy()

    def juego():
        quitar(vent1)
        #Creando ventana
        vent2=Tk()
        vent2.title("Pinball Andrea Timaran")
        canvas=Canvas(vent2, width=1000, height=600)
        fondo = PhotoImage(file="1.gif")
        canvas.create_image(450,300,image=fondo)

        canvas.pack()

        #######################################################
        ################## Tablero del juego ##################
        #######################################################

        #Bordes del juego
        linea_izq_1=canvas.create_line(70,0,70,440,width=8,fill="#088A85")
        linea_izq_2=canvas.create_line(68,437,210,500,width=9,fill="#088A85")
        linea_izq_3=canvas.create_rectangle(120,200,130,410,fill="#088A85")
        linea_izq_4=canvas.create_line(122,407,210,446,width=10,fill="#088A85")
        linea_der_1=canvas.create_line(510,150,510,440,width=8,fill="#088A85")
        linea_der_2=canvas.create_line(512,435,370,510,width=8,fill="#088A85")
        linea_der_3=canvas.create_rectangle(470,200,460,400,fill="#088A85")
        linea_der_4=canvas.create_line(468,399,380,445,width=10,fill="#088A85")
        linea_der_5=canvas.create_line(560,0,560,440,width=8,fill="#088A85")
        linea_der_6=canvas.create_line(510,437,561,437,width=8,fill="#088A85")
        linea_der_7=canvas.create_line(560,0,560,440,width=8,fill="#088A85")

        #Paletas

        pale_izq=canvas.create_polygon(200,480,200,520,280,520,outline="black",fill="#A9F5F2")
        pale_der=canvas.create_polygon(310,520,390,480,390,520,outline="black",fill="#A9F5F2")

        #Obstaculos
        global obs0,obs1,obs2,obs3,obs4
        obs0=canvas.create_oval(150,50,180,80, fill="#81F7F3")
        obs1=canvas.create_oval(220,90,250,120, fill="#FE2E64")
        obs2=canvas.create_oval(280,50,310,80, fill="#81F7F3")
        obs3=canvas.create_oval(340,90,370,120, fill="#FE2E64")
        obs4=canvas.create_oval(400,50,430,80, fill="#81F7F3")
        obstaculos={obs0:20,obs1:50,obs2:100,obs3:50,obs4:20}

        pos=canvas.coords(obstaculos)

        #vidas
        vida=3
        vid_text=canvas.create_text(800,190,font=("Barbieri-Book",34),text=("Vidas:",vida),fill="white")




        #Puntaje
        punt=canvas.create_text(790,40,font=("Barbieri-Book",34),text="Puntuación:",fill="white")
        puntuacion=0
        punt_text=canvas.create_text(800,100,font=("Barbieri-Book",34),text=puntuacion,fill="white")
        nombre = Label(vent2, text=nom)
        nombre.place(x= 500, y= 300)
        #canvas.itemconfig(punt_text,text=puntuacion)        

        #######################################################
        ###################### COLISIONES #####################
        #######################################################


        #Movimiento palancas

        def mover_izq(event):

            global pale_izq
            canvas.delete(pale_izq)
            pale_izq = canvas.create_polygon(200,480,200,520,280,500,outline="black",fill="#A9F5F2")
            canvas.update()
            canvas.delete(pale_izq)
            time.sleep(0.04)
            pale_izq = canvas.create_polygon(200,480,200,520,280,520,outline="black",fill="#A9F5F2")

        def mover_der(event):
            
            global pale_der
            canvas.delete(pale_der)
            pale_der = canvas.create_polygon(310,490,390,480,390,520,outline="black",fill="#A9F5F2")
            canvas.update()
            canvas.delete(pale_der)
            time.sleep(0.04)
            pale_der = canvas.create_polygon(310,520,390,480,390,520,outline="black",fill="#A9F5F2")

        def vidas(vida):

            vida=vida-1

            global vid_text
            canvas.delete(vid_text)
            vid_text=canvas.create_text(800,190,font=("Barbieri-Book",34),text=("Vidas:",vida),fill="white")
            canvas.update()
            canvas.delete(vid_text)
            time.sleep(0.004)
            vid_text=canvas.create_text(800,190,font=("Barbieri-Book",34),text=("Vidas:",vida),fill="white")
            


            
        def iniciar_juego():


            texto_fin_de_juego= canvas.create_text(300,240,font=("Barbieri-Book",36),text="FIN JUEGO",fill="white",state='hidden')
                
            
            x1,y1,x2,y2 = canvas.coords(ball["obj"])
            x = (x1+x2)//2
            y = (y1+y2)//2
            x3,y3,x4,y4= x2,y1,x1,y2

            xb1,yb1,xb2,yb2=canvas.coords(obs0)
            xb3,yb3,xb4,yb4= xb2,yb1,xb1,yb2
            
            #Colision el los filos
            if y<=10:
                ball["dy"]*=-1
                
            if  x>=535 or x<=84:
                ball["dx"]*=-1

            if y>=500:
                vidas(vida)

            #Colision obstaculos

            if x1<=182 and x1>=152 and y1<=82  and y1>=52 :
                ball["dx"]*=-1
                ball["dy"]*=-1
                
                
            canvas.move(ball["obj"], ball["dx"], ball["dy"])
            canvas.after(50, iniciar_juego)
            
                   
            #if x2<=xb1 and y2<=yb1 and x1<=xb2 :
                #ball["dx"]*=-1
             #   ball["dy"]*=-1
            #if x3<=xb4 and y3<=yb4:
             #   ball["dx"]*=-1
              #  ball["dy"]*=-1
           # if x1<=200:
            #    ball["dx"]*=-1
             #   ball["dy"]*=-1
          #  if y>=521:
           #     canvas.itemconfig(texto_fin_de_juego,state="normal")
            
             
            canvas.move(ball["obj"],ball["dx"],ball["dy"]) 
            #ventana.after(50,moverball)
        """
            x = (x1+x2)//2
            y = (y1+y2)//2
            
           xb=(xb1+xb2)//2
            yb=(yb1+yb2)//2
            
            if x<70 or x>490:
                ball["dball["dx"]*=-1
                ball["dy"]*=-1x"]*=-1
            if x==140 or x==450 and y>=200 and y<=450:
                ball["dx"]*=-1    
            if y<10:
                ball["dy"]*=-1
            if y>=521 and x>=280 and x<=310:
                 ball["dy"]*=1
                 canvas.itemconfig(texto_fin_de_juego,state="normal")
        """
            
           # if y==yb:
            #    ball["dy"]*=-1        




        def inicio(event):
            iniciar_juego()
                


        ball = {"dx": 6, "dy":3, "obj":canvas.create_oval(230,190,250,210, fill="yellow")}


        vent2.bind("a",mover_izq)
        vent2.bind("<Up>",mover_der)
        vent2.bind('<space>', inicio)

        vent2.mainloop()




        

    def regresar():
        quitar(vent1)
        import Principio

        

    #Creando campo de Texto
    texto=canvas.create_text(190,350,fill="#088A85",font=("Barbieri-Book",20),text="Nombre Jugador : ")
    txtUsuario = Entry(vent1,textvariable=" ",width=30,font=("Barbieri-Book",17),bg="white")
    txtUsuario.place(x=310,y=340)
    nom=txtUsuario.get()

    #Boton seguir
    botonSeguir=Button(vent1, text='Continuar',font=( "Barbieri-Book",22), width=12,command=juego,bg="#A9E2F3").place(x=400,y=415)

    #Boton menú principal
    botonSalir=Button(vent1, text='Menú principal',font=("Barbieri-Book",22), width=12,command=regresar,bg="#A9E2F3").place(x=400,y=505)


    ventana.mainloop()



def informacion():
    quitar(ventana)
    #Creando ventana
    vent3=Tk()
    vent3.title("Pinball Andrea Timaran")
    canvas3=Canvas(vent3, width=1000, height=600)
    fondo = PhotoImage(file="1.gif")
    canvas3.create_image(450,300,image=fondo)
    infol=canvas3.create_text(140,100,text="Objetivo",font=("Barbieri-Book",20),fill="yellow")
    info=canvas3.create_text(400,150,text="El juego consiste en que el jugador no debe dejar \ncaer la pelota y lograr la máxima puntución posible",font=("Barbieri-Book",20),fill="white")
    canvas3.pack()


#Creando botones
botonJugar=Button(ventana, text=' Jugar',font=("Barbieri-Book",22), width=12,command=funcion,bg="#FFFF00").place(x=150,y=380)
botonSalir=Button(ventana, text='Salir del Juego',font=("Barbieri-Book",22), width=12,command=ventana.destroy,bg="#A9E2F3").place(x=400,y=380)
botonInfo=Button(ventana, text="Información del juego",font=("Baribieri-Book",22),width=19,command=informacion,bg="#A9E2F3").place(x=210,y=470)
ventana.mainloop()
