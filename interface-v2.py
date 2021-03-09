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

def recuperer_mot_au_hasard():
    with open(arborescence, 'r') as f:
        texte = f.read()
        texte = texte.split("\n")
        indexMot = randint(0, len(texte) - 1)
        return texte[indexMot]

def clear_window(fenetre, listeAGarder=[]):
    for widget in fenetre.winfo_children():
        if widget not in listeAGarder:
            widget.destroy()


def jeu_solo():
    print("jeu solo")
    clear_window(fenetre, [textCredits])

    modeDeMot = tk.IntVar()
    valide = tk.BooleanVar() #pour savoir si le choix a été validé
    messagePrincipal = tk.Label(fenetre, text="Comment souhaitez-vous obtenir le mot ?")
    radioButtonMotAleatoire = tk.Radiobutton(fenetre, text="Mot aléatoire", variable=modeDeMot, value=1)
    radioButtonMotChoisi = tk.Radiobutton(fenetre, text="Mot choisi   ", variable=modeDeMot, value=2)
    boutonValider = tk.Button(fenetre, text="Valider", command=lambda: valide.set(True))

    messagePrincipal.grid(row=0)
    radioButtonMotAleatoire.grid(row=1)
    radioButtonMotChoisi.grid(row=2)
    boutonValider.grid(row=3)

    while modeDeMot.get() != 1 and modeDeMot.get() != 2: #tant que l'utilisateur n'a pas un choix valide
        boutonValider.wait_variable(valide) #attend la validation des données
        if modeDeMot.get() != 1 and modeDeMot.get() != 2:
            fenetre_error("Erreur d'entrée de donnée", "Votre choix n'est pas correctement validé")

    print("choix de type de mot défini")

    mot = None
    if modeDeMot.get() == 1: #si le mot est choisi au hasard
        mot = recuperer_mot_au_hasard().upper()
    else: #si le mot est choisi par l'utilisateur
        clear_window(fenetre, [textCredits])
        messagePrincipal = tk.Label(fenetre, text="Entrez un mot")
        messagePrincipal.grid(row=0)

        mot = tk.StringVar() #variable qui contiendra le mot
        mot.set(value="MOT")
        valide = tk.BooleanVar()

        champDeTexte = tk.Entry(fenetre, textvariable=mot, width=40)
        champDeTexte.grid(row=1)

        boutonValider = tk.Button(fenetre, text="Valider", command=lambda: valide.set(True))
        boutonValider.grid(row=2)

        boutonValider.wait_variable(valide)
        mot = mot.get().upper() #on met la valeur du mot dans cette variable

    print("mot choisi")
    clear_window(fenetre, [textCredits])
    #on a fini de choisir le mot
    play(mot)


def play(motADeviner):
    #boucle principale
    trouve = False
    perdu = False
    etatPendu = 0
    listeLettresTrouvees = [None]*len(motADeviner)
    listeLettresDonnees = [] #Liste de toutes les lettres dejà proposées par l'utilisateur

    while trouve == False and perdu == False:

        lettreActu = None
        while lettreActu in listeLettresDonnees or lettreActu == None: #On vérifie qu'on ne rentre pas 2 fois la même lettre
            clear_window(fenetre)
            valide = tk.BooleanVar()
            boutonValider = tk.Button(fenetre, text="Valider", command=lambda: valide.set(True))
            boutonValider.grid(row=5)
            lettreActuEntry = tk.StringVar()
            valide = tk.BooleanVar()
            entree=tk.Entry(fenetre, textvariable=lettreActuEntry, width=30)
            entree.grid(row=2,column=10)
            boutonValider.wait_variable(valide) #attend la validation des données
            lettreActu = lettreActuEntry.get().upper()


        listeLettresDonnees.append(lettreActu)

        #On regarde si la lettre appartient au mot
        reponseJuste = False
        for index in range(len(motADeviner)):
            if motADeviner[index] == lettreActu:
                listeLettresTrouvees[index] = lettreActu
                reponseJuste = True

        if reponseJuste:
            print("Cette lettre appartient au mot")
        else:
            etatPendu += 1
            print("Cette lettre est incorrecte")

        print(dessinPendu(etatPendu))

        #Affichage du mot dans la console avec des "_" pour les trous
        for lettre in listeLettresTrouvees:
            if lettre == None:
                print("-", end="")
            else:
                print(lettre, end="")
        print("")

        #On regarde si on a gagné ou perdu
        if etatPendu >= 6:
            perdu = True
        elif None not in listeLettresTrouvees:
            trouve = True



arborescence = "dico.txt"


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
