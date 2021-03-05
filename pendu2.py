#-*- coding: utf-8 -*-
import os


#---------- DEFINITIONS VARIABLES ------------
print("Entrer 0 si la lettre proposée n'est pas dans le mot.")
print("Sinon entrer la position de la lettre dans le mot")
print("Si elle est à plusieurs endroits, entrer chaque position séparée par une virgule\n")

nb_lettre = int(input("Nombre de lettres : "))#Nombre de lettre du mot à trouver
#f = open("gros_dico.txt",'r',errors='ignore')
f = open("tres_gros_dico.txt",'r',errors='ignore')
liste = f.read().split("\n")
liste_mots_possibles = [i for i in liste if len(i)==nb_lettre]#Mots que l'on peut former à partir de la position des lettres trouvées
etat_pendu=0
mot_final = [None]*nb_lettre #Mot à trouver écrit sous forme de liste
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
occurence_lettres = {}#Nombre d'occurences de chaque lettre dans la liste des mots possibles pour choisir la lettre la plus adaptée
for lettre in alphabet:
    occurence_lettres[lettre] = 0
lettres_proposees = []#Liste de toutes les lettres deja proposées
perdu = False#Variables pour savoir quand sortir de la boucle principale
trouve = False


#------------- DEFINITIONS FONCTIONS -----------
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

def proposition_lettre(occurence_lettres, lettres_proposees):#Fonction qui choisie la lettre la plus adaptée à proposer
    lettre_valeur_max = "A"
    for lettre in alphabet:
        if occurence_lettres[lettre]>occurence_lettres[lettre_valeur_max]:
            lettre_valeur_max = lettre
    if lettre_valeur_max not in lettres_proposees:#Cette lettre n'a jamais été proposée,on choisi donc celle là
        return lettre_valeur_max
    else:
        occurence_lettres[lettre_valeur_max]=0#Cette lettre a deja été proposée, on met son occurence à 0 pour ne pas le reproposer
        return proposition_lettre(occurence_lettres, lettres_proposees)#et on rappelle la fonction encore une fois


#--------- BOUCLE PRINCIPALE ----------
while perdu==False and trouve==False:

	os.system('clear')

	print(dessinPendu(etat_pendu))

	for i in mot_final:#Affichage du mot dans la console
		if i == None:
			print("_", end=" ")
		else:
			print(i, end = " ")
	print("")

	for i in range(len(mot_final)):
		print(str(i+1), end=" ")

	print("\n")

	for lettre in alphabet: #On remet à 0 le dictionnaire
		occurence_lettres[lettre] = 0

	for mot in liste_mots_possibles:#On remplit le dictionnaire avec les nouvelles valeurs
		for lettre in mot:
			try:
				occurence_lettres[lettre]+=1
			except:
				pass


	lettre_proposee = proposition_lettre(occurence_lettres, lettres_proposees)#On récupère dans la variable lettre_proposee la lettre la plus adaptée à proposer

	resultat = input("En quelle position le mot comporte un "+ lettre_proposee+" ? ")
	#resultat = str(resultat)

	#----On supprime de la liste tous les mots qui ne correspondent plus----
	nb_mots_supprimes =0
	if resultat == "0":#Le mot ne comporte pas cette lettre, on enlève tous les mots qui ont cette lettre
		etat_pendu +=1
		for i in range(len(liste_mots_possibles)):
			if lettre_proposee in liste_mots_possibles[i-nb_mots_supprimes]:
				liste_mots_possibles.pop(i-nb_mots_supprimes)
				nb_mots_supprimes+=1
	else:#On a donné la/les position(s) de la lettre dans le mot. On peut donc supprimer les mots qui ne correspondent pas
		resultat = resultat.split(",")
		for i in resultat:
			nb_mots_supprimes = 0
			index = int(i)-1
            #print(type(mot))
			mot_final[index] = lettre_proposee
			for i in range(len(liste_mots_possibles)):
				if lettre_proposee != liste_mots_possibles[i-nb_mots_supprimes][index]:
					liste_mots_possibles.pop(i-nb_mots_supprimes)
					nb_mots_supprimes+=1
	lettres_proposees.append(lettre_proposee) #On ajoute la lettre à la liste pour ne pas la proposer une nouvelle fois




	#----On vérifie si on a terminé la partie----
	if etat_pendu>=7:
		perdu = True
		print("L\'ordinateur n'a pas trouvé, le pendu est mort avant...")
	if None not in mot_final:#Il y a plus de lettres inconnues dans le mot donc on a gagné
		print("Trouvé ! Le mot était "+"".join(mot_final))
		trouve = True
	if len(liste_mots_possibles)==0 and trouve==False:#Le mot qu'on cherche n'est visiblement pas dans le dictionnaire, on a donc perdu
		print("L'ordinateur n'a pas réussi à trouver")
		perdu = True
