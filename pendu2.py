#-*- coding: utf-8 -*-
import os

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



f = open("gros_dico.txt",'r',errors='ignore')
liste = f.read().split("\n")

#print(liste)

etat_pendu=0


nb_lettre = int(input("Nombre de lettres : "))

mot_final = [None]*nb_lettre


liste_mots_possibles = [i for i in liste if len(i)==nb_lettre]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
occurence_lettres = {}

lettres_proposees = []

for lettre in alphabet:
    occurence_lettres[lettre] = 0

def proposition_lettre(occurence_lettres, lettres_proposees):
    lettre_valeur_max = "A"
    for lettre in alphabet:
        if occurence_lettres[lettre]>occurence_lettres[lettre_valeur_max]:
            lettre_valeur_max = lettre
    if lettre_valeur_max not in lettres_proposees:
        return lettre_valeur_max
    else:
        occurence_lettres[lettre_valeur_max]=0#Cette lettre a deja été proposée, on met son occurence à 0 pour ne pas le reproposer
        return proposition_lettre(occurence_lettres, lettres_proposees)




perdu = False
trouve = False

while perdu==False and trouve==False:

	os.system('clear')

	print(dessinPendu(etat_pendu))

	for i in mot_final:
		if i == None:
			print('_', end=" ")
		else:
			print(i, end = " ")
	print("\n")

	for lettre in alphabet:
		occurence_lettres[lettre] = 0

	for mot in liste_mots_possibles:
		for lettre in mot:
			try:
				occurence_lettres[lettre]+=1
			except:
				pass


	lettre_proposee = proposition_lettre(occurence_lettres, lettres_proposees)

	resultat = input("En quelle position le mot comporte un "+ lettre_proposee+" ? ")
	resultat = str(resultat)
    #print(type(resultat))
    #print(liste_mots_possibles)
	nb_mots_supprimes =0

	if resultat == "0":#Le mot ne comporte pas cette lettre, on enlève tous les mots qui ont cette lettre
		etat_pendu +=1
		for i in range(len(liste_mots_possibles)):
			if lettre_proposee in liste_mots_possibles[i-nb_mots_supprimes]:
				liste_mots_possibles.pop(i-nb_mots_supprimes)
				nb_mots_supprimes+=1
	else:#On a donné la/les position(s) de la lettre dans le mot. On peut donc supprimer les mots qui ne correspondent pas
		for i in resultat:

			nb_mots_supprimes =0
			index = int(i)-1
            #print(type(mot))
			mot_final[index] = lettre_proposee
			for i in range(len(liste_mots_possibles)):
				if lettre_proposee != liste_mots_possibles[i-nb_mots_supprimes][index]:
					liste_mots_possibles.pop(i-nb_mots_supprimes)
					nb_mots_supprimes+=1

		lettres_proposees.append(lettre_proposee)



	#print(mot_final)

	if etat_pendu>=6:
		perdu = True
		print("L\'ordinateur n'a pas trouvé, le pendu est mort avant...")


	if None not in mot_final:
		print("Trouvé ! Le mot était "+"".join(mot_final))
		trouve = True

	if len(liste_mots_possibles)==0:
		print("L'ordinateur n'a pas réussi à trouver")
		perdu = True

    #trouve = True
    #print(occurence_lettres)
