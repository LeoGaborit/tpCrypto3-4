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


def genererMDPcleMaitre(entree: str, tailleMDP: int) -> str:
    """
    Génère un mot de passe de <taille> caractères à partir de deux entrées
    :param entree: une chaine de caractères
    :param tailleMDP: un entier entre 1 et 12
    :return: un mot de passe de 8 caractères
    """

    assert 1 <= tailleMDP <= 12, "La taille doit être comprise entre 1 et 12"

    chaineConcatenee: str
    chaineHashee: str
    cleMaitre : str
    choix : str

    chaineASCII: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    tailleASCII: int = len(chaineASCII)
    tailleSHA512: int = 128

    chaineMDP: str = ""

    i: int
    tailleSouslistes: int
    restants: int

    cleMaitre = lireMPWD()

    if tailleMDP < 1 or tailleMDP > 12:
        raise ValueError("La taille doit être comprise entre 1 et 12")

    if cleMaitre == "":
        cleMaitre = demanderNouveauMDP()

    choix=str(input("Voulez-vous changer de mot de passe maître ? (O/N) : "))
    if choix == "O":
        cleMaitre = demanderNouveauMDP()
    else :
        pass

    chaineConcatenee = entree + cleMaitre  # Concatène les deux entrées
    chaineHashee = hashlib.sha512(chaineConcatenee.encode('utf-8')).hexdigest()  # Hash en hexadécimal

    tailleSouslistes = tailleSHA512 // tailleMDP

    # Générer des sous-listes variables et créer le mot de passe
    for i in range(tailleMDP):
        chaineTemp = chaineHashee[i * tailleSouslistes: (i + 1) * tailleSouslistes]
        chaineMDP += chaineASCII[int(chaineTemp, 16) % tailleASCII]

    return chaineMDP


def lireMPWD() -> str:
    """
    Lit le mot de passe maître stocké dans le fichier mpwd.txt
    :return: le mot de passe maître
    """
    try :
        with open("mpwd.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "" # Si le fichier n'existe pas, retourne une chaine vide, pour que le programme demande un nouveau mot de passe


def demanderNouveauMDP() -> str:
    """
    Demande à l'utilisateur de rentrer un nouveau mot de passe maître
    """
    nouveauMDP : str
    nouveauMDP = input("Veuillez rentrer un nouveau mot de passe maître, il ne doit pas contenir d'espaces : ")
    return nouveauMDP

