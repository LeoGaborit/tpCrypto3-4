"""
Tests pour le fichier exo4.py
/!\ Attention, les tests ne sont pas exhaustifs

Chemin vers le script principal : src/main/exo4.py
"""
from src.main.exo2 import genererMDPtailleN
from src.main.exo4 import boucleAttaqueBF, trouverCollisions

def test_boucleAttaqueBF():
    """
    Test de la fonction boucleAttaqueBF
    LES TESTS PEUVENT ETRE LONGS
    """
    #Test avec une taille de 1
    cleMaitre = "a"
    tailleMDP = 5
    tag = "Unilim"

    hashCible = genererMDPtailleN(tag, cleMaitre, tailleMDP)
    assert boucleAttaqueBF(len(cleMaitre), tag, tailleMDP, hashCible, cleMaitre) == True

    #Test avec une taille de 2
    cleMaitre = "H3"
    tailleMDP = 8
    tag = "Netflix"

    hashCible = genererMDPtailleN(tag, cleMaitre, tailleMDP)
    assert boucleAttaqueBF(len(cleMaitre), tag, tailleMDP, hashCible, cleMaitre) == True

    #Test avec une taille de 3
    cleMaitre = "+d4"
    tailleMDP = 4
    tag = "Amazon"

    hashCible = genererMDPtailleN(tag, cleMaitre, tailleMDP)
    assert boucleAttaqueBF(len(cleMaitre), tag, tailleMDP, hashCible, cleMaitre) == True

    #Test avec une taille de 4
    cleMaitre = "X)*d"
    tailleMDP = 12
    tag = "Unilim"

    hashCible = genererMDPtailleN(tag, cleMaitre, tailleMDP)
    assert boucleAttaqueBF(len(cleMaitre), tag, tailleMDP, hashCible, cleMaitre) == True


def test_trouverCollisions():
    #Test avec une taille de 1
    assert trouverCollisions() == None


    # Fonction qui trouve des collisions entre les tags
    trouverCollisions()