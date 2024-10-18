"""
Tests pour le fichier exo3.py
/!\ Attention, les tests ne sont pas exhaustifs

Chemin vers le script principal : src/main/exo3.py
"""

#Création des tests

from src.main.exo3 import genererMDPcleMaitre

def test_genererMDPtailleN():
    #Test avec une taille de 1
    assert len(genererMDPcleMaitre("hello", 1)) == 1
    #Test avec une taille de 2
    assert len(genererMDPcleMaitre("hello", 2)) == 2
    #Test avec une taille de 3
    assert len(genererMDPcleMaitre("hello", 3)) == 3
    #Test avec une taille de 4
    assert len(genererMDPcleMaitre("hello", 4)) == 4
    #Test avec une taille de 5
    assert len(genererMDPcleMaitre("hello", 5)) == 5
    #Test avec une taille de 6
    assert len(genererMDPcleMaitre("hello", 6)) == 6
    #Test avec une taille de 7
    assert len(genererMDPcleMaitre("hello", 7)) == 7
    #Test avec une taille de 8
    assert len(genererMDPcleMaitre("hello", 8)) == 8
    #Test avec une taille de 9
    assert len(genererMDPcleMaitre("hello", 9)) == 9
    #Test avec une taille de 10
    assert len(genererMDPcleMaitre("hello", 10)) == 10
    #Test avec une taille de 11
    assert len(genererMDPcleMaitre("hello", 11)) == 11
    #Test avec une taille de 12
    assert len(genererMDPcleMaitre("hello", 12)) == 12

