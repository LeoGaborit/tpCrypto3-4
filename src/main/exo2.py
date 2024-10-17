"""
Exercice 2 : Des mots de passe d’une taille demandée
Faites une extension à votre programme qui permet de prendre en entrée un entier N, ainsi que les deux
chaines de caractères utilisés dans l’exercice précédent. L’entier N peut varier entre 1 et 12 et il représente
la taille attendue par l’output. Si besoin, changez de fonction de hachage pour avoir une sortie plus longue.

La validation de l’état actuel de votre programme se fera par des jeux d’essais. Veuillez indiquer les jeux
d’essais les plus importants, ainsi qu’une liste de cas de tests, dans votre rapport.
"""

import hashlib

def genererMDPtailleN(entree1: str, entree2: str, tailleMDP : int) -> str:
    """
    Génère un mot de passe de <taille> caractères à partir de deux entrées
    :param entree1: une chaine de caractères
    :param entree2: une chaine de caractères
    :param tailleMDP: un entier entre 1 et 12
    :return: un mot de passe de 8 caractères
    """

    assert 1 <= tailleMDP <= 12, "La taille doit être comprise entre 1 et 12"

    chaineConcatenee : str
    chaineHashee : str

    chaineASCII : str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    tailleASCII : int = len(chaineASCII)
    tailleSHA256 : int = 64

    chaineMDP : str = ""

    i : int
    tailleSouslistes : int
    restants : int

    chaineConcatenee = entree1 + entree2    # Concatène les deux entrées
    chaineHashee = hashlib.sha512(chaineConcatenee.encode('utf-8')).hexdigest() # Hash en hexadécimal

    tailleSouslistes = tailleSHA256 // tailleMDP

    # Générer des sous-listes variables et créer le mot de passe
    for i in range(tailleMDP):
        chaineTemp = chaineHashee[i * tailleSouslistes : (i + 1) * tailleSouslistes]
        chaineMDP += chaineASCII[int(chaineTemp, 16) % tailleASCII]

    return chaineMDP # Renvoi des 8 premiers caractères du hash