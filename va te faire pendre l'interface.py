#Carnet de bord 
#Mardi 02/03 : Organisation (Github) + jeux sans interface graphique
#Jeudi 04/03 : Interface graphique

from tkinter import * #Importer toutes les classes du module
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



arborescence = "U:/nicolas.marcel/Mes documents/1ere/NSI/2021-03-02/dico.txt"

def clear_window(fenetre):
    for widget in fenetre.winfo_children():
        widget.destroy()

def recupererMotAuHasard(): #Fonction pour choisir un mot au hasard à faire deviner
    with open(arborescence,'r') as f:
        texte = f.read()
        texte = texte.split("\n")
        indexMot = randint(0,len(texte)-1)
        return texte[indexMot]

def coucou():
    text1.destroy()
    bouton.destroy()
    modeDeMot = IntVar()
    boutonMotAleatoire = Radiobutton(fenetre, text="Mot aléatoire   ", variable=modeDeMot, value=0)
    boutonMotChoisi = Radiobutton(fenetre, text="Choisir un mot", variable=modeDeMot, value=1)
    boutonMotAleatoire.grid()
    boutonMotChoisi.grid()
    
    widgets = [boutonMotAleatoire, boutonMotChoisi]
    
    boutonValider=Button(fenetre, text="Valider", command=lambda : choixMot(modeDeMot))
    boutonValider.grid(row=2,column=1)
   
    
    

def choixMot(modeDeMot):
    clear_window(fenetre)
    
    if modeDeMot.get() == 1:
        motADeviner = StringVar()
        motADeviner.set("Entrer un mot...")
        entree = Entry(fenetre, textvariable=motADeviner, width=30)
        entree.grid()
        #motADeviner = "A FAIRE"
        #motADeviner = motADeviner.upper()
        boutonValider=Button(fenetre, text="Valider", command=lambda : main(motADeviner.get().upper()))
        boutonValider.grid(row=2,column=1)
    else:
        motADeviner = recupererMotAuHasard()
    
        main(motADeviner)
    
    
attente_validation = True
lettre_donnee = ""

def entree_lettre():
    
    motADeviner = StringVar()
    motADeviner.set("Entrer un mot...")
    entree = Entry(fenetre, textvariable=motADeviner, width=30)
    entree.grid()
    
    boutonValider=Button(fenetre, text="Valider", command=lambda : main(motADeviner.get().upper()))
    boutonValider.grid(row=2,column=1) 
    
    lettre_donnee = "E"
    attente_validation = False
    
def main(motADeviner):
    print(motADeviner)
    print("boucle principale")
    #boucle principale
    trouve = False
    perdu = False
    etatPendu = 0
    listeLettresTrouvees = [None]*len(motADeviner)
    listeLettresDonnees = [] #Liste de toutes les lettres dejà proposées par l'utilisateur
    while trouve == False and perdu == False:

        lettreActu = None
        while lettreActu in listeLettresDonnees or lettreActu == None:


            lettreActu = input("Entrez une lettre : ").upper()


        listeLettresDonnees.append(lettreActu)

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


        for lettre in listeLettresTrouvees:
            if lettre == None:
                print("-", end="")
            else:
                print(lettre, end="")
        print("")

        #si perdu
        if etatPendu >= 6:
            perdu = True
        elif None not in listeLettresTrouvees:
            trouve = True

    if trouve:
        print("Bravo vous avez gagné !")
    else:
        print(f"Dommage vous avez perdu, le mot était {motADeviner}")
    
    

fenetre=Tk() #Utilise la classe Tk() pour créer une fenêtre
fenetre.geometry("640x480")


text1=Label(fenetre,text='Bienvenue sur notre jeu du pendu !')
text1.grid(row=1, column=1)

bouton=Button(fenetre, text="Jouer en solo", command=coucou)
bouton.grid(row=2,column=1)

text1=Label(fenetre,text='© By Nicolas & Lucien')
text1.grid(row=3, column=1)

fenetre.mainloop()

print("fin du programme")

