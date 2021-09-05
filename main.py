"""

Morpion by Maxence.R

Développers and Designer
Informaticiens indépendants

"""



#
#Importation des modules
#

import time
from tkinter import *
from tkinter.messagebox import *
import pygame
from random import *

def Clic(event):
    global a,C1,C2,C3,C1RC,C1R,C2RC,C2R,C3RC,C3R,L1RC,L1R,L2RC,L2R,L3RC,L3R,L1,L2,L3
    
    #
    # position du pointeur de la souris
    #
    
    X = event.x
    Y = event.y

    #   
    #Si a=1 on met une croix
    #

    if a==1:
        if X < 100:
            if Y < 100:
                if C1[0]==2:
                    a=0
                    C1[0]=1
                    L1[0]=1
                    Croix(50,50)
                else :
                        showinfo(title='Non',message='Tu ne peux pas !')
            else :
                if Y < 200:
                    if C1[1]==2:
                        a=0
                        C1[1]=1
                        L2[0]=1
                        Croix(50,150)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')
                else :
                    if C1[2]==2:
                        a=0
                        C1[2]=1
                        L3[0]=1
                        Croix(50,250)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')
               
        if X < 200 and X > 100:
            if Y < 100:
                if C2[0]==3:
                    a=0
                    C2[0]=1
                    L1[1]=1
                    Croix(150,50)
                else :
                        showinfo(title='Non',message='Tu ne peux pas !')
            else :
                if Y < 200:
                    if C2[1]==3:
                        a=0
                        C2[1]=1
                        L2[1]=1
                        Croix(150,150)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')
                else :
                    if C2[2]==3:
                        a=0
                        C2[2]=1
                        L3[1]=1
                        Croix(150,250)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')
               
        if X < 300 and X > 200:
            if Y < 100:
                if C3[0]==4:
                    a=0
                    C3[0]=1
                    L1[2]=1
                    Croix(250,50)
                else :
                        showinfo(title='Non',message='Tu ne peux pas !')
               
            else :
                if Y < 200:
                    if C3[1]==4:
                        a=0
                        C3[1]=1
                        L2[2]=1
                        Croix(250,150)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')
                   
                else :
                    if C3[2]==4:
                        a=0
                        C3[2]=1
                        L3[2]=1
                        Croix(250,250)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')
    
    #               
    #Ici a=0 et on met un rond
    #

    else:
        if X < 100:
            if Y < 100:
                if C1[0]==2:
                    a=1
                    C1[0]=0
                    L1[0]=0
                    Rond(50,50)
                else :
                        showinfo(title='Non',message='Tu ne peux pas !')
                       
            else :
                if Y < 200:
                    if C1[1]==2:
                        a=1
                        C1[1]=0
                        L2[0]=0
                        Rond(50,150)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')
                   
                else :
                    if C1[2]==2:
                        a=1
                        C1[2]=0
                        L3[0]=0
                        Rond(50,250)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')
                   
        if X < 200 and X > 100:
            if Y < 100:
                if C2[0]==3:
                    a=1
                    C2[0]=0
                    L1[1]=0
                    Rond(150,50)
                else :
                        showinfo(title='Non',message='Tu ne peux pas !')
               
            else :
                if Y < 200:
                    if C2[1]==3:
                        a=1
                        C2[1]=0
                        L2[1]=0
                        Rond(150,150)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')
                   
                else :
                    if C2[2]==3:
                        a=1
                        C2[2]=0
                        L3[1]=0
                        Rond(150,250)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')
                   
        if X < 300 and X > 200:
            if Y < 100:
                if C3[0]==4:
                    a=1
                    C3[0]=0
                    L1[2]=0
                    Rond(250,50)
                else :
                        showinfo(title='Non',message='Tu ne peux pas !')
            else :
                if Y < 200:
                    if C3[1]==4:
                        a=1
                        C3[1]=0
                        L2[2]=0
                        Rond(250,150)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')
                   
                else :
                    if C3[2]==4:
                        a=1
                        C3[2]=0
                        L3[2]=0
                        Rond(250,250)
                    else :
                        showinfo(title='Non',message='Tu ne peux pas !')

#
#ici on créer la fonction pour afficher les ronds
#

def Rond(x1,y1):
    global C1,C2,C3
    morpion.create_oval(x1-45,y1-45,x1+45,y1+45, fill="#FFFFFF")
    Verif()

#
#ici on créer la fonction pour afficher les croix
#

def Croix(x1,y1):
    global C1,C2,C3
    morpion.create_line(x1-45,y1-45,x1+45,y1+45, fill="#FFFFFF")
    morpion.create_line(x1+45,y1-45,x1-45,y1+45, fill="#FFFFFF")
    Verif()

def player_info():
    pseudo=pseudonyme.get()
    pseudo2=pseudonyme_two.get()
      
    print("Joueur 1 : " + pseudo)
    print("Joueur 2 : " + pseudo2)

score = 0

def replay_game_if_win():
    global score
    replay_game()
    score = 0
    #
    # Ici on remet les score a 0
    #

    ascore1 = Canvas(root, width=120, height=30, bg='#443F42', highlightthickness=0)
    ascore1.create_rectangle(0, 0, score, 45, fill='#595558', width=0)
    ascore1.place(x=128, y=30)

    ascore2 = Canvas(root, width=120, height=30, bg='#443F42', highlightthickness=0)
    ascore2.create_rectangle(0, 0, score, 45, fill='#595558', width=0)
    ascore2.place(x=250, y=30)

def add_point_score():
    global score
    global pseudonyme
    score +=25
    ascore1 = Canvas(root, width=120, height=30, bg='#443F42', highlightthickness=0)
    ascore1.create_rectangle(0, 0, score, 45, fill='#595558', width=0)
    ascore1.place(x=128, y=30)
    if score >= 120:
        pseudo2=pseudonyme.get()
        showinfo(title='Gagne',message=f'{pseudo2} a Gagner !')
        time.sleep(2)
        replay_game_if_win()
    else:
        ascore1 = Canvas(root, width=120, height=30, bg='#443F42', highlightthickness=0)
        ascore1.create_rectangle(0, 0, score, 45, fill='#595558', width=0)
        ascore1.place(x=128, y=30)

score2 = 0

def add_point_score2():
    global score2
    global pseudonyme_two
    score2 +=25
    ascore1 = Canvas(root, width=120, height=30, bg='#443F42', highlightthickness=0)
    ascore1.create_rectangle(0, 0, score, 45, fill='#595558', width=0)
    ascore1.place(x=128, y=30)
    if score2 >= 121:
        pseudo=pseudonyme_two.get()
        showinfo(title='Gagne',message=f'{pseudo} a Gagner !')
        time.sleep(2)
        replay_game_if_win()
    else:
        ascore2 = Canvas(root, width=120, height=30, bg='#443F42', highlightthickness=0)
        ascore2.create_rectangle(0, 0, score2, 45, fill='#595558', width=0)
        ascore2.place(x=250, y=30)

def replay_game():
    global morpion
    global C1RC,C1R,C2RC,C2R,C3RC,C3R,L1RC,L1R,L2RC,L2R,L3RC,L3R
    global C1, C2,C3,C1RC,C1R,C2RC,C2R,C3RC,C3R,L1RC,L1R,L2RC,L2R,L3RC,L3R,L1,L2,L3
    global C1, L1, C2, L2, C3, L3
    global a
    morpion.delete('all')

    #
    #ici on recréer les lignes qui délimite les colones et les cases
    #


    morpion.create_line(0,100,300,100,fill="white",width=4)

    morpion.create_line(0,200,300,200,fill="white",width=4)

    morpion.create_line(100,300,300,-100000,fill="white",width=4)

    morpion.create_line(200,300,300,-100000,fill="white",width=4)
    
    C1=[2,2,2]
    L1=[2,2,2]

    C2=[3,3,3]
    L2=[3,3,3]

    C3=[4,4,4]
    L3=[4,4,4]

    a=1

def Verif():
    global C1, C2,C3,C1RC,C1R,C2RC,C2R,C3RC,C3R,L1RC,L1R,L2RC,L2R,L3RC,L3R,L1,L2,L3
    C1RC = C1.count(1)
    C1R = C1.count(0)
    C2RC = C2.count(1)
    C2R = C2.count(0)
    C3RC = C3.count(1)
    C3R = C3.count(0)
   
    L1RC = L1.count(1)
    L1R = L1.count(0)
    L2RC = L2.count(1)
    L2R = L2.count(0)
    L3RC = L3.count(1)
    L3R = L3.count(0)

    #
    #ici on affiche le joueur qui a gagner
    #

    if C1RC == 3 or C2RC == 3 or C3RC == 3 or (C1[0]==1 and C2[1]==1 and C3[2]==1) or (C1[2]==1 and C2[1]==1 and C3[0]==1) or L1RC == 3 or L2RC == 3 or L3RC == 3:
        """
        Joueur 1
        """
        add_point_score()
        replay_game()
    if C1R == 3 or C2R == 3 or C3R == 3 or (C1[0]==0 and C2[1]==0 and C3[2]==0) or (C1[2]==0 and C2[1]==0 and C3[0]==0) or L1R == 3 or L2R == 3 or L3R == 3:
        """
        Joueur 2
        """
        add_point_score2()
        replay_game()
   
#
#ici on initialise les colones et les lignes
#

C1RC,C1R,C2RC,C2R,C3RC,C3R,L1RC,L1R,L2RC,L2R,L3RC,L3R = 0,0,0,0,0,0,0,0,0,0,0,0
       

   
a=1

C1=[2,2,2]
L1=[2,2,2]

C2=[3,3,3]
L2=[3,3,3]

C3=[4,4,4]
L3=[4,4,4]



#
# Création de la fenêtre principale
#

root = Tk()
root.title("Morpion")
root.minsize(600, 500)
root.resizable(False, False)
root.config(background='#C4C4C4')
root.title("Sn'Game | Morpion")
root.iconbitmap("core/64px.ico")



#
# Création d'un widget Canvas
#

title1 = Frame(root)

hcan = Canvas(root, width = 500, height =500, bg ="#2B2B2B", highlightthickness=0)
hcan.place(x=0,y=0)

Largeur = 300
Hauteur = 300
morpion = Canvas(root, width = Largeur, height =Hauteur, bg ="#2B2B2B", highlightthickness=0)

#
# La méthode bind() permet de lier un événement avec une fonction :
#
# un clic gauche sur la zone graphique provoquera l'appel de la fonction utilisateur Clic()
#


morpion.bind("<Button-1>", Clic)
morpion.place(x=100,y=100)


#
#ici on créer les lignes qui délimite les colones et les cases
#


morpion.create_line(0,100,300,100,fill="white",width=4)

morpion.create_line(0,200,300,200,fill="white",width=4)

morpion.create_line(100,300,300,-100000,fill="white",width=4)

morpion.create_line(200,300,300,-100000,fill="white",width=4)

#
# Création du texte
#

text = Label(root, text="    Morpion    ", font=('Arial', 48),bg='#2B2B2B', fg='white')
text.place(x=450,y=0)

handmade = Label(root, text="Handmade by Kijusu", font=('Roboto', 20),bg='#C4C4C4', fg='#121212')
handmade.place(x=520,y=445)

#
# Création des boutons et des Entrée de texte
#

valider_button =Button(root, text="Valider", bg='#5E5E5E',font=('Arial', 15), fg='#C4C4C4',activebackground = "#5E5E5E", activeforeground = "#C4C4C4", command=lambda: [f() for f in [player_info, change_name]])
valider_button.place(x=598, y=360, width=100, height=27)

pseudo_txt = Label(root, text="Pseudo joueur 1 :", font=('Arial', 18),bg='#C4C4C4', fg='#2B2B2B')
pseudo_txt.place(x=558, y=165)

pseudonyme = Entry(root, text="Pseudo", bg='#EDEDED', fg='#2B2B2B', bd=0 ,width=29,highlightthickness=0, justify='center', font=('Arial', 9))
pseudonyme.place(x=550, y=200, height=25)

pseudo_txt_two = Label(root, text="Pseudo joueur 2 :", font=('Arial', 18),bg='#C4C4C4', fg='#2B2B2B')
pseudo_txt_two.place(x=558, y=265)

pseudonyme_two = Entry(root, text="Pseudotwo", bg='#EDEDED', fg='#2B2B2B', bd=0 ,width=29,highlightthickness=0, justify='center', font=('Arial', 9))
pseudonyme_two.place(x=550, y=300, height=25)

def ascore():

    line = Canvas(root, width=50, height=60, bg='#2A2A2A', highlightthickness=0)
    line.create_line(20,30,30,-100000,fill="white",width=3)
    line.place(x=228, y=30)

    score_canvas1 = Canvas(root, width=120, height=60, bg='#2A2A2A', highlightthickness=0)
    score_canvas1.create_rectangle(0, 15, 120, 45, fill='#443F42', width=0)
    score_canvas1.place(x=128, y=15)

    score_canvas2 = Canvas(root, width=120, height=60, bg='#2A2A2A', highlightthickness=0)
    score_canvas2.create_rectangle(0, 15, 120, 45, fill='#443F42', width=0)
    score_canvas2.place(x=250, y=15)
ascore()

joueur1 = Label(root, text="Joueur 1", bg="#2A2A2A", fg="white", font=("Arial",10))
joueur1.place(x=128, y=5)

joueur2 = Label(root, text="Joueur 2", bg="#2A2A2A", fg="white", font=("Arial",10))
joueur2.place(x=316, y=5)

def change_name():
    global pseudonyme
    psde1= pseudonyme.get()
    psde2 = pseudonyme_two.get()
    # prevoir la variable pour recevoir le texte saisi
    joueur1['text'] = psde1
    joueur2['text'] = psde2
    joueur1.place(x=128, y=5)
    joueur2.place(x=357-7*(len(psde2)-1), y=5)

    """
    x= 360
    y= 5
    """

#
# Centrer la fenêtre en fonction de l'écran de l'ordinateur
#

w =800
h =500

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
# calculate position x, y
x = (ws/2) - (w/2)    
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#
# Afficher la fennetre
#

mainloop()
