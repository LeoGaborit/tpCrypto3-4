"""Retravaillez votre code pour qu’il prenne (et stocke) dans un fichier un mot de passe maître, qui
correspond à la première des deux chaines de caractères prises en entrée. Ce fichier s’appellera mpwd
(l’extension sera de votre choix). Votre générateur de mot de passe devra désormais prendre en entrée
seulement la taille du mot de passe attendu et une chaine de caractère.
Le mot de passe sera calculé à partir du mot de passe maître et de la chaine de caractères pour un output
de taille N.
Particularités : Attention à la gestion du mot de passe maître ! Les règles suivantes doivent être observées
par votre programme :
• Un mot de passe maître ne peut pas contenir des espaces (mais peut contenir les autres
caractères permis dans l’exercice 1)
• S’il n’y a aucun mot de passe dans le fichier ou si le fichier n’existe pas : demandez un nouveau
mot de passe maître
• L’utilisateur doit pouvoir demander un changement de mot de passe dans la console, au début
de chaque exécution (on ne veut pas lui demander de changer le fichier directement !)
Extension possible : si jamais vous avez fini le TP et vous souhaitez avancer d’avantage, vous pouvez
également penser à mettre en place un fichier de stockage pour les tags utilisés. Ce type de fichier pourrait
par exemple stocker la correspondance entre l’URL ou le service pour lequel on utilise un mot de passe et
le tag utilisé."""

import hashlib

def genererMDPtailleN(entree1: str, taille : int) -> str:
    """
    Génère un mot de passe de <taille> caractères à partir de deux entrées
    :param entree1: une chaine de caractères
    :param entree2: une chaine de caractères
    :param taille: un entier entre 1 et 12
    :return: un mot de passe de 8 caractères
    """

    chaineConcatenee : str
    chaineHashee : str
    entree2 : str
    choix : str

    entree2 = lireMPWD()
    print(entree2)

    if taille < 1 or taille > 12:
        raise ValueError("La taille doit être comprise entre 1 et 12")

    if entree2 == "":
        entree2 = demanderNouveauMDP()

    choix=str(input("Voulez-vous changer de mot de passe maître ? (O/N)"))
    if choix == "O":
        entree2 = demanderNouveauMDP()
    else :
        pass

    chaineConcatenee = entree1 + entree2    # Concatène les deux entrées
    chaineHashee = hashlib.sha256(chaineConcatenee.encode('utf-8')).hexdigest() # Hash

    return chaineHashee[:taille] # Renvoi des <taille> premiers caractères du hash

def lireMPWD() -> str:
    """
    Lit le mot de passe maître stocké dans le fichier mpwd.txt
    :return: le mot de passe maître
    """

    try :
        with open("mpAd.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""


def demanderNouveauMDP() -> str:
    """
    Demande à l'utilisateur de rentrer un nouveau mot de passe maître
    """
    nouveauMDP : str

    nouveauMDP = input("Veuillez rentrer un nouveau mot de passe maître, il ne doit pas contenir d'espaces : ")

    return nouveauMDP

print("Votre mot de passe est : " + genererMDPtailleN("iu?^qsfv:", 12)) # 8 caractères
