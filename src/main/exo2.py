"""
Exercice 2 : Des mots de passe d’une taille demandée
Faites une extension à votre programme qui permet de prendre en entrée un entier N, ainsi que les deux
chaines de caractères utilisés dans l’exercice précédent. L’entier N peut varier entre 1 et 12 et il représente
la taille attendue par l’output. Si besoin, changez de fonction de hachage pour avoir une sortie plus longue.

La validation de l’état actuel de votre programme se fera par des jeux d’essais. Veuillez indiquer les jeux
d’essais les plus importants, ainsi qu’une liste de cas de tests, dans votre rapport.
"""

import hashlib

def genererMDPtailleN(entree1: str, entree2: str, taille : int) -> str:
    """
    Génère un mot de passe de <taille> caractères à partir de deux entrées
    :param entree1: une chaine de caractères
    :param entree2: une chaine de caractères
    :param taille: un entier entre 1 et 12
    :return: un mot de passe de 8 caractères
    """

    chaineConcatenee : str
    chaineHashee : str

    if taille < 1 or taille > 12:
        raise ValueError("La taille doit être comprise entre 1 et 12")

    chaineConcatenee = entree1 + entree2    # Concatène les deux entrées
    chaineHashee = hashlib.sha256(chaineConcatenee.encode('utf-8')).hexdigest() # Hash

    return chaineHashee[:taille] # Renvoi des <taille> premiers caractères du hash

# Test

