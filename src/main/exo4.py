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
import itertools
import time
from src.main.exo2 import genererMDPtailleN

def boucleAttaqueBF(tailleCleM : int, tag : str, tailleMDP : int, hashCible : str, cleMaitre : str) -> bool:
    """
    Boucle de génération de mots à hasher de taille <taille>
    :param hashCible:
    :param tag:
    :param tailleCleM: taille du mot de passe
    :return: mot hashé (Exemple : aaa ... b-E pour taille 3)
    """

    tempsDebut : float = time.time()
    chaineASCII : str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

    if tailleCleM in [1, 2, 3, 4, 5]:
        print(f"\nDébut de la recherche de la clé maître pour le mot de passe {hashCible}\n")
        for comb in itertools.product(chaineASCII, repeat=tailleCleM):
            cle = ''.join(comb)
            motHashe = genererMDPtailleN(tag, cle, tailleMDP)
            if motHashe == hashCible and cleMaitre == cle:
                tempsFin = time.time()
                tempsTotal = tempsFin - tempsDebut
                print(f"HashCible trouvé : {motHashe} avec le tag {tag} et la clé {cle} en {round(tempsTotal, 6)} secondes")
                return True
            elif motHashe == hashCible and cleMaitre != cle:
                print(f"Collisions trouvé : {motHashe} avec le tag {tag} et la clé {cle}")
    else:
        print("Taille non supportée (1,2,3)")
    print("\nFin de la recherche de la clé maître\n")
    return False


def trouverCollisions():
    """
    Trouve des collisions entre les tags
    - Unilim
    - Amazon
    - Netflix
    """

    print("\nDébut de la recherche de collisions\n")

    chaineASCII : str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

    tentatives : int = 0

    tempsDebut : float = time.time()

    print("Recherche de collisions pour taille 1\n")
    for comb in itertools.product(chaineASCII, repeat=1):
        tentatives += 1
        cleMaitre = ''.join(comb)
        motHasheUnilim = genererMDPtailleN('Unilim', cleMaitre, 1)
        motHasheAmazon = genererMDPtailleN('Amazon', cleMaitre, 1)
        motHasheNetflix = genererMDPtailleN('Netflix', cleMaitre, 1)
        if motHasheUnilim == motHasheAmazon and motHasheAmazon == motHasheNetflix and motHasheNetflix == motHasheUnilim:
            print(f"Collision trouvée pour le mot {cleMaitre} : {motHasheUnilim} - {motHasheAmazon} - {motHasheNetflix}")

    print("\nRecherche de collisions pour taille 2\n")
    for comb in itertools.product(chaineASCII, repeat=2):
        tentatives += 1
        cleMaitre = ''.join(comb)
        motHasheUnilim = genererMDPtailleN('Unilim', cleMaitre, 2)
        motHasheAmazon = genererMDPtailleN('Amazon', cleMaitre, 2)
        motHasheNetflix = genererMDPtailleN('Netflix', cleMaitre, 2)
        if motHasheUnilim == motHasheAmazon and motHasheAmazon == motHasheNetflix and motHasheNetflix == motHasheUnilim:
            print(f"Collision trouvée pour le mot {cleMaitre} : {motHasheUnilim} - {motHasheAmazon} - {motHasheNetflix}")

    print("\nRecherche de collisions pour taille 3\n")
    for comb in itertools.product(chaineASCII, repeat=3):
        tentatives += 1
        cleMaitre = ''.join(comb)
        motHasheUnilim = genererMDPtailleN('Unilim', cleMaitre, 3)
        motHasheAmazon = genererMDPtailleN('Amazon', cleMaitre, 3)
        motHasheNetflix = genererMDPtailleN('Netflix', cleMaitre, 3)
        if motHasheUnilim == motHasheAmazon and motHasheAmazon == motHasheNetflix and motHasheNetflix == motHasheUnilim:
            print(f"Collision trouvée pour le mot {cleMaitre} : {motHasheUnilim} - {motHasheAmazon} - {motHasheNetflix}")

    print(f"\nRecherche de collisions pour taille 4\n")
    for comb in itertools.product(chaineASCII, repeat=4):
        tentatives += 1
        cleMaitre = ''.join(comb)
        motHasheUnilim = genererMDPtailleN('Unilim', cleMaitre, 4)
        motHasheAmazon = genererMDPtailleN('Amazon', cleMaitre, 4)
        motHasheNetflix = genererMDPtailleN('Netflix', cleMaitre, 4)
        if motHasheUnilim == motHasheAmazon and motHasheAmazon == motHasheNetflix and motHasheNetflix == motHasheUnilim:
            print(f"Collision trouvée pour le mot {cleMaitre} : {motHasheUnilim} - {motHasheAmazon} - {motHasheNetflix}")

        tempsFin : float = time.time()
        tempsTotal = tempsFin - tempsDebut
        print(f"\nNombre total de tentatives : {tentatives} en {round(tempsTotal, 6)} secondes")
        print("\nFin de la recherche de collisions\n")