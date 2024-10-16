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

import hashlib

from exo2 import genererMDPtailleN
from generateurDico import generer_dictionnaire

pathDicoT1 = "src/main/dictionnaireTaille1.txt"
pathDicoT2 = "src/main/dictionnaireTaille2.txt"
pathDicoT3 = "src/main/dictionnaireTaille3.txt"


def chargerDictionnaire(cheminFichier):
    """
    Charge le dictionnaire à partir d'un fichier.

    :param cheminFichier: Chemin du fichier dictionnaire.
    :return: Liste de mots de passe.
    """
    with open(cheminFichier, 'r') as fichier:
        return [ligne.strip() for ligne in fichier]


def attaqueBruteForce(dictionnaire, hashCible):
    """
    Tente de trouver un mot de passe en utilisant une attaque par dictionnaire avec SHA-256.

    :param dictionnaire: Liste des mots de passe potentiels.
    :param hashCible: Le hash SHA-256 cible que nous essayons de casser.
    :return: Le mot de passe correspondant si trouvé, sinon None.
    """
    for mot in dictionnaire:
        motHashe = hashlib.sha256(mot.encode()).hexdigest()
        if motHashe == hashCible:
            return mot
    return None


def genererTousLesDicos():
    """
    Génère et enregistre des dictionnaires de mots de passe de taille 1, 2 et 3.
    """
    generer_dictionnaire(1, pathDicoT1)
    generer_dictionnaire(2, pathDicoT2)
    generer_dictionnaire(3, pathDicoT3)

# Exemple d'utilisation pour générer les dictionnaires
genererTousLesDicos()

# Charger les dictionnaires à partir des fichiers générés
dictionnaireT1 = chargerDictionnaire(pathDicoT1)
dictionnaireT2 = chargerDictionnaire(pathDicoT2)
dictionnaireT3 = chargerDictionnaire(pathDicoT3)


# Supposons que vous ayez une fonction qui génère des mots de passe pour différents tags
def generer_mot_de_passe(tag, mot_de_passe_maitre):
    """
    Générez un mot de passe pour un tag spécifique en utilisant un mot de passe maître.

    :param tag: Le tag pour lequel générer le mot de passe.
    :param mot_de_passe_maitre: Le mot de passe maître.
    :return: Mot de passe généré.
    """
    return hashlib.sha256((tag + mot_de_passe_maitre).encode()).hexdigest()


# Generer un hash cible pour un tag donné en utilisant un mot de passe maître
mot_de_passe_maitre = 'Abc123!@#'  # Exemple de mot de passe maître de 10 caractères
hash_cible_unilim = generer_mot_de_passe('Unilim', mot_de_passe_maitre)+'Unilim'
hash_cible_amazon = generer_mot_de_passe('Amazon', mot_de_passe_maitre)
hash_cible_netflix = generer_mot_de_passe('Netflix', mot_de_passe_maitre)

# Attaque pour le tag Unilim
resultat_unilim = attaqueBruteForce(dictionnaireT1, hash_cible_unilim)

if resultat_unilim:
    print(f"Mot de passe maître trouvé pour Unilim: {resultat_unilim}")
else:
    print("Aucun mot de passe maître trouvé pour Unilim dans le dictionnaire de taille 1.")


# Attaque pour les tags Unilim, Amazon et Netflix ensemble
def attaque_par_force_brute_multiple(dictionnaire, hash_cibles):
    """
    Tente de trouver un mot de passe en utilisant une attaque par dictionnaire avec SHA-256
    pour plusieurs hashs cibles.

    :param dictionnaire: Liste des mots de passe potentiels.
    :param hash_cibles: Liste de hashs SHA-256 cibles que nous essayons de casser.
    :return: Le mot de passe correspondant si trouvé, sinon None.
    """
    for mot in dictionnaire:
        matched_all = all(
            hashlib.sha256((tag + mot).encode()).hexdigest() == hash_cible for tag, hash_cible in hash_cibles)
        if matched_all:
            return mot
    return None


hash_cibles = [
    ('Unilim', hash_cible_unilim),
    ('Amazon', hash_cible_amazon),
    ('Netflix', hash_cible_netflix)
]

resultat_multiple = attaque_par_force_brute_multiple(dictionnaireT1, hash_cibles)

if resultat_multiple:
    print(f"Mot de passe maître trouvé pour plusieurs tags: {resultat_multiple}")
else:
    print("Aucun mot de passe maître trouvé pour les tags dans le dictionnaire de taille 1.")
