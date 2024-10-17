"""
Exercice 4 : Attaques sur des mots de passe
Dans cet exercice, vous allez tenter de trouver des préimages possibles pour le mot de passe maître, c’est
à-dire, vous allez tenter de casser la sécurité de votre générateur de mots de passe.
Votre tâche sera de trouver un mot de passe valide en connaissant le tag utilisé mais pas le mot de passe
maître.

Assurez-vous premièrement que votre fichier de mots de passe maître contient un mot de passe maître
de 10 caractères (à vous de les choisir). Dans votre rapport discutez quelle est la probabilité qu’un
attaquant retrouve ce mot de passe maître par force brute.

Générez, en utilisant votre générateur de mots de passe et le mot de passe maître, des mots de passe
d’un caractère (N=1) pour les tags suivants : Unilim, Amazon, Netflix.

Dans un premier temps votre attaque devra trouver un mot de passe maître qui donnera le même mot
de passe que celui produit par votre vrai mot de passe sur le tag Unilim.

La stratégie sera celle d’une attaque par dictionnaire. Votre dictionnaire doit contenir tous les mots de
passe possibles, avec toutes les possibilités pour chaque caractère. Itérez sur les mots de passe possibles
sur 10 caractères, chaque caractère provenant de votre dictionnaire, jusqu’à trouver un mot de passe
identique (pour le tag Unilim) à celui produit par le gestionnaire de mots de passe. Combien de possibilités
avez-vous essayées ? Quelle est la probabilité théorique de trouver un mot de passe maître qui provoque
une collision et comment votre nombre d’essais se compare à cette valeur ?

Dans un deuxième temps, votre attaque devra retrouver un mot de passe maître qui provoque une
collision sur les 3 tags : Unilim, Amazon et Netflix. Comparez le nombre d’essais nécessaire pour votre
attaque dans ce cas par rapport au cas précédent.

Finalement, essayez la même attaque pour N = 2 et N = 3, en enregistrant le nombre d’essais.

Analyse : Dans votre rapport utilisez les données sur le nombre d’essais pour N = 1, 2 et 3 pour pouvoir
formuler une hypothèse sur le nombre d’essais demandé pour retrouver un mot de passe maître qui
donne des collisions pour des mots de passe de taille N = 8, 10 et 12. Comparez ces chiffres à la probabilité
théorique de réussir, ainsi qu’à la probabilité de trouver le mot de passe maître (quia avait 10 caractères).
Quelles sont vos conclusions par rapport à un design sécurisé et une utilisation correcte de votre
générateur de mots de passe ?
"""

import time
from exo2 import genererMDPtailleN

def boucleAttaqueBF(taille : int, tag : str, hashCible : str, cleMaitre : str) -> bool:
    """
    Boucle de génération de mots à hasher de taille <taille>
    :param hashCible:
    :param tag:
    :param taille: taille du mot de passe
    :return: mot hashé (Exemple : aaa ... b-E pour taille 3)
    """

    tempsDebut : float = time.time()
    chaineASCII : str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    tailleASCII : int = len(chaineASCII)

    collisions : str = ""

    if taille == 1:
        for i in range(tailleASCII):
            mot = chaineASCII[i]
            motHashe = genererMDPtailleN(tag, mot, taille)
            print(mot, motHashe, hashCible)
            if motHashe == hashCible and cleMaitre == mot:
                tempsFin : float = time.time()
                tempsTotal = tempsFin - tempsDebut
                print(f"HashCible trouvé : {motHashe} avec le tag {tag} et le mot {mot} en {round(tempsTotal, 6)} secondes")
                print(f"Collisions trouvées : {collisions}")
                return True
            elif motHashe == hashCible and cleMaitre != mot:
                collisions = collisions + "| cleMaitre : " + mot + " - hash : " + motHashe

    elif taille == 2:
        for i in range(tailleASCII):
            for j in range(tailleASCII):
                mot = chaineASCII[i] + chaineASCII[j]
                motHashe = genererMDPtailleN(tag, mot, taille)
                print(mot, motHashe, hashCible)
                if motHashe == hashCible and cleMaitre == mot:
                    tempsFin : float = time.time()
                    tempsTotal = tempsFin - tempsDebut
                    print(f"HashCible trouvé : {motHashe} avec le tag {tag} et le mot {mot} en {round(tempsTotal, 6)} secondes")
                    print(f"Collisions trouvées : {collisions}")
                    return True
                elif motHashe == hashCible and cleMaitre != mot:
                    collisions = collisions + "| cleMaitre : " + mot + " - hash : " + motHashe

    elif taille == 3:
        for i in range(tailleASCII):
            for j in range(tailleASCII):
                for k in range(tailleASCII):
                    mot = chaineASCII[i] + chaineASCII[j] + chaineASCII[k]
                    motHashe = genererMDPtailleN(tag, mot, taille)
                    print(mot, motHashe, hashCible)
                    if motHashe == hashCible and cleMaitre == mot:
                        tempsFin : float = time.time()
                        tempsTotal = tempsFin - tempsDebut
                        print(f"HashCible trouvé : {motHashe} avec le tag {tag} et le mot {mot} en {round(tempsTotal, 6)} secondes")
                        print(f"Collisions trouvées : {collisions}")
                        return True
                    elif motHashe == hashCible and cleMaitre != mot:
                        collisions = collisions + " | cleMaitre : " + mot + " - hash : " + motHashe

    else:
        print("Taille non supportée (1,2,3)")

    print("\nHashCible non trouvé")
    return False

# Generer un hash cible pour un tag donné en utilisant un mot de passe maître
cleMaitre = 'X*$y' # MAX 3 CARACTERES (1,2,3)
tailleCle = len(cleMaitre)

mdpCibleUnilim = genererMDPtailleN('Unilim', cleMaitre, tailleCle)
mdpCibleAmazon = genererMDPtailleN('Amazon', cleMaitre, tailleCle)
mdpCibleNetflix = genererMDPtailleN('Netflix', cleMaitre, tailleCle)

# Attaque pour le tag Unilim
resultatUnilim = boucleAttaqueBF(tailleCle, 'Unilim', mdpCibleUnilim, cleMaitre)
