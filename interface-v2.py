from tkinter import * #Importer toutes les classes du module
from random import randint

def dessinPendu(nb):
    tab = [

    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,

    """
       +-------+
       |	   |
       |	   O
       |
       |
       |
    ==============
    """,

    """
       +-------+
       |	   |
       |	   O
       |	   |
       |
       |
    ==============
    """,

    """
       +-------+
       |	   |
       |	   O
       |	  -|
       |
       |
    ==============
    """,

    """
       +-------+
       |	   |
       |	   O
       |	  -|-
       |
       |
    ==============
    """,

    """
       +-------+
       |	   |
       |	   O
       |	  -|-
       |	  |
       |
    ==============
    """,

    """
       +-------+
       |	   |
       |	   O
       |	  -|-
       |	  | |
       |
    ==============
    """
    ]
    return tab[nb]



def clear_window(fenetre, listeAGarder=[]):
    for widget in fenetre.winfo_children():
        if widget not in listeAGarder:
            widget.destroy()


def jeu_solo():
    print("jeu solo")
    clear_window(fenetre, [textCredits])



fenetre=Tk() #Utilise la classe Tk() pour créer une fenêtre
fenetre.geometry("640x480")


textBienvenue=Label(fenetre,text='Bienvenue sur notre jeu du pendu !')
textBienvenue.grid(row=1, column=1)

boutonJouerSolo=Button(fenetre, text="Jouer en solo", command=lambda : jeu_solo())
boutonJouerSolo.grid(row=2,column=1)

textCredits = Label(fenetre,text='© By Nicolas & Lucien')
textCredits.grid(row=3, column=1)

fenetre.mainloop()

print("fin du programme")
