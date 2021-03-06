#
#
#
#
import os
from random import randint

arborescence = "dico.txt"


def dessinPendu(nb): #Fonction de dessin du pendu
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


def recupererMotAuHasard(): #Fonction pour choisir un mot au hasard à faire deviner
	with open(arborescence,'r') as f:
		texte = f.read()
		texte = texte.split("\n")
		indexMot = randint(0,len(texte)-1)
		return texte[indexMot]


def main():
	print("Bonjour")
	print("Bienvenue dans ce super jeu du pendu !")

    #-----Choix mode de jeu-----
	modeDeJeu = None
	while modeDeJeu != "1" and modeDeJeu != "2":
		modeDeJeu = input("Entrez 1 pour choisir un mot à deviner\nEntrez 2 pour prendre un mot au hasard : ")


    #----Récupération du mot à faire deviner-----
	motADeviner = None
	if modeDeJeu == "1":
		motADeviner = input("Entrez le mot à deviner : ")
	else:
		motADeviner = recupererMotAuHasard()

	motADeviner = motADeviner.upper()

	#boucle principale
	trouve = False
	perdu = False
	etatPendu = 0
	listeLettresTrouvees = [None]*len(motADeviner)
	listeLettresDonnees = [] #Liste de toutes les lettres dejà proposées par l'utilisateur

	while trouve == False and perdu == False:

		lettreActu = None
		while lettreActu in listeLettresDonnees or lettreActu == None: #On vérifie qu'on ne rentre pas 2 fois la même lettre
			lettreActu = input("Entrez une lettre : ").upper()

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

	if trouve:
		print("Bravo vous avez gagné !")
	else:
		print(f"Dommage vous avez perdu, le mot était {motADeviner}")


main()
