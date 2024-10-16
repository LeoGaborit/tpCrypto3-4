"""
Exercice 1 : Des mots de passe tout simples
Dans un premier temps, vous allez devoir produire une application qui doit, en prenant en entrée deux
chaines de caractères de taille arbitraire, produire une chaine de 8 caractères, qui peuvent être : des
lettres majuscules ou minuscules, des chiffres, ainsi que des caractères spéciaux arbitraires (mais pas
d’espaces, des caractères invisibles, etc.).

Vous n’avez pas besoin d’une interface particulière graphique, vous pouvez gérer les entrées et les sorties
dans la console.

L’algorithme de génération de mots de passe devra utiliser une fonction de hachage et suivre les étapes
suivantes :
• Concaténer les deux chaines de caractères en entrée
• Faire exécuter la fonction de hachage avec en entrée la suite de caractères obtenue ci-dessus
• Traduire (si besoin) la sortie dans une suite de 8 caractères comme détaillé dans la consigne. En
fonction de la fonction de hachage utilisée, vous devrez potentiellement tronquer l’output de la
fonction de hachage, ou justement changer de fonction de hachage car l’output est trop petit.
Détaillez ces étapes dans votre rapport

Particularités : Évaluez d’une façon convaincante votre programme, à la fois en termes du respect de la
consigne (est-ce que l’output est vraiment la bonne sortie de la fonction de hachage et à la bonne taille ?)
et en termes de la robustesse des mots de passe par rapport aux entrées (distributions des outputs).
Décrivez vos tests et résultats d’une façon à la fois lisible et succincte dans le rapport.
"""

import hashlib

def genererMDP(entree1: str, entree2: str) -> str | int:
    """
    Génère un mot de passe de 8 caractères à partir de deux entrées
    :param entree1: une chaine de caractères
    :param entree2: une chaine de caractères
    :return: un mot de passe hashé de 8 caractères
    """

    chaineConcatenee : str
    chaineHashee : str

    chaineASCII : str = ("abcdefghijklmnopqrstuvwxy"
                         "zABCDEFGHIJKLMNOPQRSTUVWX"
                         "YZ0123456789!@#$%^&*()_+")

    tailleASCII : int = len(chaineASCII)

    chaineMDP : str = ""

    i : int

    chaineConcatenee = entree1 + entree2    # Concatène les deux entrées

    chaineHashee = hashlib.sha256(chaineConcatenee.encode('utf-8')).hexdigest() # Hash en hexadécimal

    # On fait 8 listes de 8 caractères hashés
    for i in range(8):
        chaineTemp = chaineHashee[i*8:(i+1)*8]
        chaineMDP += chaineASCII[int(chaineTemp, 16) % tailleASCII]

    return chaineMDP # Renvoi des 8 premiers caractères du hash