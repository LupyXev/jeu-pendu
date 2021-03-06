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

        # Affichage du mot dans la console avec des "_" pour les trous

        motAAfficher = ""  # Mot à faire deviner qu'on affiche dans la fenetre

        for lettre in listeLettresTrouvees:

            if lettre == None:

                motAAfficher += "_"

            else:

                motAAfficher += lettre

            motAAfficher += " "

        messageMot = tk.Label(fenetre, text=motAAfficher)

        messageMot.grid(row=1)

        lettreActu = None
        messagePrincipal = tk.Label(fenetre, text="Entrez une lettre")
        messagePrincipal.grid(row=2)


        while lettreActu in listeLettresDonnees or lettreActu == None: #On vérifie qu'on ne rentre pas 2 fois la même lettre
            clear_window(fenetre, [textCredits, messagePrincipal, messageMot])
            canvas = tk.Canvas(fenetre, width=640, height=380)
            img = tk.PhotoImage(file=f'images/{etatPendu}.png')
            canvas.create_image(0, 0, image=img, anchor="nw")

            canvas.grid(row=0)

            valide = tk.BooleanVar() #le booléen si lettre validée
            boutonValider = tk.Button(fenetre, text="Valider", command=lambda: valide.set(True)) #le bouton de validation
            boutonValider.grid(row=5)
            lettreActuEntry = tk.StringVar() #l'objet contenant la lettre renseignée

            entree=tk.Entry(fenetre, textvariable=lettreActuEntry, width=10)
            entree.grid(row=3)
            while len(lettreActuEntry.get()) != 1: #tant que le texte n'est pas un caractère
                boutonValider.wait_variable(valide)  # attend la validation des données
                if len(lettreActuEntry.get()) != 1:
                    fenetre_error("Erreur de donnée", "Le texte renseigné n'est pas un caractère unique")

            lettreActu = lettreActuEntry.get().upper()
            if lettreActu in listeLettresDonnees: #si la lettre est déjà essayée
                fenetreLettreDejaRentree = messagebox.showinfo("Lettre déjà renseignée", "La lettre que vous avez entrée a déjà été essayée")


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

    clear_window(fenetre, [textCredits])
    messageAAfficher = None

    if perdu:
        messageAAfficher = "Dommage, vous avez perdu, le mot à deviner était " + motADeviner + "."
    elif trouve:
        messageAAfficher = "Bravo vous avez réussi à trouver le mot " + motADeviner + " ! Nous vous félicitons !"
    else:
        fenetre_error("Erreur", "Le joueur n'a ni gagné ni perdu")

    messagePrincipal = tk.Label(fenetre, text=messageAAfficher)
    messagePrincipal.grid(row=2)

arborescence = "dico.txt"


fenetre=tk.Tk() #Utilise la classe Tk() pour créer une fenêtre
fenetre.geometry("640x480")
fenetre.title("Le jeu du pendu")


textBienvenue = tk.Label(fenetre,text='Bienvenue sur notre jeu du pendu !')
textBienvenue.grid(row=1, column=1)

boutonJouerSolo = tk.Button(fenetre, text="Jouer en solo", command=lambda : jeu_solo())
boutonJouerSolo.grid(row=2,column=1)

textCredits = tk.Label(fenetre,text='© By Nicolas & Lucien')
textCredits.grid(row=99, column=1)

fenetre.mainloop()

print("fin du programme")
