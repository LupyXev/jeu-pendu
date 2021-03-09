import tkinter as tk #Importer le module
from tkinter import messagebox
from random import randint
import time

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

def fenetre_error(titre, message):
    '''fenetreErreur = Frame(fenetre)

    textErreur = Label(fenetreErreur,text=f'Erreur : {message}')
    textErreur.grid(row=1)

    boutonClique = IntVar() #var pour savoir si le bouton fermer a été cliqué
    print(boutonClique.get())
    boutonFermer = Button(fenetreErreur, text="Fermer", command=lambda: boutonClique.set(1))
    boutonFermer.grid(row=2)


    print(boutonClique.get())
    boutonFermer.wait_variable(boutonClique)
    print(boutonClique.get())

    fenetreErreur.mainloop()'''
    fenErreur = messagebox.showwarning(titre, message)



def clear_window(fenetre, listeAGarder=[]):
    for widget in fenetre.winfo_children():
        if widget not in listeAGarder:
            widget.destroy()


def jeu_solo():
    print("jeu solo")
    clear_window(fenetre, [textCredits])

    modeDeMot = tk.IntVar()
    valide = tk.BooleanVar() #pour savoir si le choix a été validé
    radioButtonMotAleatoire = tk.Radiobutton(fenetre, text="Mot aléatoire", variable=modeDeMot, value=1)
    radioButtonMotChoisi = tk.Radiobutton(fenetre, text="Mot choisi   ", variable=modeDeMot, value=2)
    boutonValider = tk.Button(fenetre, text="Valider", command=lambda: valide.set(True))

    radioButtonMotAleatoire.grid(row=1)
    radioButtonMotChoisi.grid(row=2)
    boutonValider.grid(row=3)

    while modeDeMot.get() != 1 and modeDeMot.get() != 2: #tant que l'utilisateur n'a pas un choix valide
        boutonValider.wait_variable(valide) #attend la validation des données
        if modeDeMot.get() != 1 and modeDeMot.get() != 2:
            fenetre_error("Erreur d'entrée de donnée", "Votre choix n'est pas correctement validé")

    print(modeDeMot.get())
    print("choix défini")



fenetre=tk.Tk() #Utilise la classe Tk() pour créer une fenêtre
fenetre.geometry("640x480")


textBienvenue = tk.Label(fenetre,text='Bienvenue sur notre jeu du pendu !')
textBienvenue.grid(row=1, column=1)

boutonJouerSolo = tk.Button(fenetre, text="Jouer en solo", command=lambda : jeu_solo())
boutonJouerSolo.grid(row=2,column=1)

textCredits = tk.Label(fenetre,text='© By Nicolas & Lucien')
textCredits.grid(row=99, column=1)

fenetre.mainloop()

print("fin du programme")
