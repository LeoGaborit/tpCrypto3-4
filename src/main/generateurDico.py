"""
Généré par IA JetBrains PyCharm
Générateur de dictionnaire .txt
"""

from itertools import product
import string
import os


def generer_dictionnaire(taille_mot_de_passe, nom_fichier):
    """
    Génère un dictionnaire contenant toutes les combinaisons possibles de mots de passe
    d'une longueur spécifiée et les enregistre dans un fichier texte.

    :param taille_mot_de_passe: Longueur des mots de passe à générer.
    :param nom_fichier: Nom du fichier où enregistrer le dictionnaire.
    """
    # Vérifiez si le fichier existe déjà et supprimez-le
    if os.path.exists(nom_fichier):
        os.remove(nom_fichier)
        print(f"Le fichier {nom_fichier} existait déjà et a été supprimé.")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    with open(nom_fichier, 'w') as fichier:
        for mot_de_passe in product(caracteres, repeat=taille_mot_de_passe):
            fichier.write(''.join(mot_de_passe) + '\n')
    print(f"Le fichier {nom_fichier} a été généré avec succès.")


