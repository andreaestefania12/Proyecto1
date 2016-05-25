from tkinter import *
import time

#Crear ventana Principal
vent=Tk()
vent.title("Pinball Andrea Timaran")
canv=Canvas(vent, width=1000, height=600)
fondo = PhotoImage(file="1.gif")
canv.create_image(450,300,image=fondo)
foto = PhotoImage(file="final.gif")
canv.create_image(500,300,image=foto)
canv.pack()

def vent1():
    vent.withdraw()
    #Ventana hija donde va a estar el juego
    ventana=Toplevel(vent)
    fondo = PhotoImage(file="1.gif")
    canvas=Canvas(ventana,width=1000,height=600)
    fondo = PhotoImage(file="1.gif")
    canvas.create_image(450,300,image=fondo)
   


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
    linea_der_3=canvas.create_rectangle(460,200,470,400,fill="#088A85")
    linea_der_4=canvas.create_line(468,399,380,445,width=10,fill="#088A85")
    linea_der_5=canvas.create_line(560,0,560,440,width=8,fill="#088A85")
    linea_der_6=canvas.create_line(510,437,561,437,width=8,fill="#088A85")


    #Paletas
    global pale_izq,pale_der
    pale_izq=canvas.create_polygon(200,480,200,520,280,520,outline="black",fill="#A9F5F2")
    pale_der=canvas.create_polygon(310,520,390,480,390,520,outline="black",fill="#A9F5F2")

    #Obstaculos
    global obs0,obs1,obs2,obs3,obs4
    obs0=canvas.create_oval(150,50,180,80, fill="#81F7F3")
    obs1=canvas.create_oval(220,90,250,120, fill="#FE2E64")
    obs2=canvas.create_oval(280,50,310,80, fill="#81F7F3")
    obs3=canvas.create_oval(340,90,370,120, fill="#FE2E64")
    obs4=canvas.create_oval(400,50,430,80, fill="#81F7F3")



    #vidas
    vida=1
    global vid_text
    vid_text=canvas.create_text(800,300,font=("Barbieri-Book",34),text=("Vidas:",vida),fill="white")
    

    #Puntaje
    punt=canvas.create_text(790,40,font=("Barbieri-Book",34),text="Puntuación:",fill="white")
    global puntuacion
    puntuacion = 0
    punt_text=canvas.create_text(800,100,font=("Barbieri-Book",34),text=puntuacion,fill="white")
    canvas.itemconfig(punt_text,text=puntuacion)  

    #Usuario
    nom=txtUsuario.get()
    usuario=canvas.create_text(800,190,font=("Barbieri-Book",28),text=("Jugador:",nom),fill="white")
      

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
        vid_text=canvas.create_text(800,300,font=("Barbieri-Book",34),text=("Vidas:",vida),fill="white")
        canvas.update()
        canvas.delete(vid_text)
        time.sleep(0.004)
        vid_text=canvas.create_text(800,300,font=("Barbieri-Book",34),text=("Vidas:",vida),fill="white")
        

    #######################################################
    ###################### COLISIONES #####################
    #######################################################

        
    def iniciar_juego():


        texto_fin_de_juego= canvas.create_text(290,240,font=("Barbieri-Book",34),text="FIN JUEGO",fill="white",state='hidden')
        
        pos=canvas.coords(ball["obj"])
        
        x = (pos[0]+pos[2])//2
        y = (pos[1]+pos[3])//2
      
        #Cordenadas de los obstaculos
        p1= canvas.coords(obs0)
        p2= canvas.coords(obs1)
        p3= canvas.coords(obs2)
        p4= canvas.coords(obs3)
        p5= canvas.coords(obs4)



        #Colisiones de los filos

        if y<=10:
            ball["dy"]*=-1
            
        if  x>=535 or x<=84:
            ball["dx"]*=-1

        if y>=540:
            if 270<=x<320:
               vidas(vida)
               canvas.itemconfig(texto_fin_de_juego,state="normal")
               
        if y>=500:
            ball["dy"]*=-1


        #Colisiones con los obstaculos


        #Obstaculo 1
        if ( p1[0]<= x <= p1[2]) and  ((p1[1]-20) <= y <= (p1[3]+10 )):
            ball["dy"]*=-1
            puntuacion=puntuacion+30
            
        if ((p1[1]-20) < y < (p1[3]+10 )) and (( (p1[0]-10)<= x <= (p1[2]+10) )):
            ball["dx"]*=-1
            puntuacion=puntuacion+30

        #Obstaculo 2
        if ( p2[0]<= x <= p2[2]) and  ((p2[1]-20) <= y <= (p2[3]+10 )):
            ball["dy"]*=-1
            puntuacion = puntuacion + 40
        if ((p2[1]-20) < y < (p2[3]+10 )) and (( (p2[0]-10)<= x <= (p2[2]+10) )):
            ball["dx"]*=-1
            puntuacion = puntuacion + 40 
        #Obstaculo 3
        if ( p3[0]<= x <= p3[2]) and  ((p3[1]-20) <= y <= (p3[3]+10 )):
            ball["dy"]*=-1
            puntuacion = puntuacion + 40
        if ((p3[1]-20) < y < (p3[3]+10 )) and (( (p3[0]-5)<= x <= (p3[2]+5) )):
            ball["dx"]*=-1
            puntuacion = puntuacion + 40
        #Obstaculo 4
        if ( p4[0]<= x <= p4[2]) and  ((p4[1]-20) <= y <= (p4[3]+10 )):
            ball["dy"]*=-1
            puntuacion = puntuacion + 40
        if ((p4[1]-20) < y < (p4[3]+10 )) and (( (p4[0]-5)<= x <= (p4[2]+10) )):
            ball["dx"]*=-1
            #puntuacion = puntuacion + 40
        #Obstaculo 5
        if ( p5[0]<= x <= p5[2]) and  ((p5[1]-20) <= y <= (p5[3]+10 )):
            ball["dy"]*=-1
##            puntuacion = puntuacion + 40
            
        if ((p5[1]-20) < y < (p5[3]+10 )) and (( (p5[0]-10)<= x <= (p5[2]+10) )):
            ball["dx"]*=-1



        #Colisiones lineas

        if (118<=x<=130) and (200<=y<=410):
            ball["dx"]*=-1
            
        if (70<=x<=78) and (150<=y<=440):
            ball["dx"]*=-1
        
        if (450<=x<=460) and (200<=y<=400):
            ball["dx"]*=-1

        if (510<=x<=518) and (150<=y<=440):
            ball["dx"]*=-1
            
        ball["dy"] = ball["dy"] + 0.3
        canvas.move(ball["obj"],ball["dx"],ball["dy"]) 
        ventana.after(20,iniciar_juego)
##        contador_puntuacion.config(text=" "+str(puntuacion))



    def inicio(event):
        iniciar_juego()
            


    ball = {"dx": 9, "dy":-15, "obj":canvas.create_oval(525,390,545,410, fill="yellow")}
##    contador_puntuacion=Label(canvas,text=" ",fg="white",bg="black")
##    contador_puntuacion.pack()
##    canvas.create_window( 600, 100, window = contador_puntuacion )
    

    ventana.bind("a",mover_izq)
    ventana.bind("<Up>",mover_der)
    ventana.bind('<space>', inicio)
    canvas.pack()

    ventana.mainloop()
        
#Creando campo de Texto
texto=canv.create_text(190,350,fill="#088A85",font=("Barbieri-Book",20),text="Nombre Jugador : ")
usuario=StringVar()
txtUsuario = Entry(vent,textvariable=usuario,width=30,font=("Barbieri-Book",17),bg="white")
txtUsuario.place(x=310,y=340)



#Boton seguir
boton=PhotoImage(file="continuar.png")
botonSeguir=Button(vent,width=170,command=vent1,bg="#A9E2F3",image=boton).place(x=400,y=415)

#Boton menú principal
menu=PhotoImage(file="menu.png")
botonSalir=Button(vent, width=170,command=vent1,bg="#A9E2F3",image=menu).place(x=400,y=505)


