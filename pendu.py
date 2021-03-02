#
#
#
#


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
	

def recupererMotAuHasard(): #Fonction pour choisir un mot au hasard à faire deviner
	return "bonjour"


def main():
	print("Bonjour")
	print("Bienvenue dans ce super jeu du pendu !")
	modeDeJeu = None
	while modeDeJeu != "1" and modeDeJeu != "2":
		modeDeJeu = input("Entrez 1 pour choisir un mot à deviner\nEntrez 2 pour prendre un mot au hasard : ")

	motADeviner = None
	if modeDeJeu == "1":
		motADeviner = input("Entrez le mot à deviner : ")
	else:
		motADeviner = recupererMotAuHasard()

	#boucle principale
	trouve = False
	perdu = False
	etatPendu = 0
	listeLettresTrouvees = [None]*len(motADeviner)
	while trouve == False and perdu == False:
		lettreActu = input("Entrez une lettre : ")

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


