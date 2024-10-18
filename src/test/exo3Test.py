"""
Tests pour le fichier exo3.py
/!\ Attention, les tests ne sont pas exhaustifs

Chemin vers le script principal : src/main/exo3.py
"""
from src.main.exo3 import genererMDPcleMaitre

def test_genererMDPtailleN():
    #Test avec une taille de 1
    assert len(genererMDPcleMaitre("hello", 1)) == 1
    #Test avec une taille de 2
    assert len(genererMDPcleMaitre("olleh", 2)) == 2
    #Test avec une taille de 3
    assert len(genererMDPcleMaitre("test", 3)) == 3
    #Test avec une taille de 4
    assert len(genererMDPcleMaitre("mdp", 4)) == 4
    #Test avec une taille de 5
    assert len(genererMDPcleMaitre("bonjour", 5)) == 5
    #Test avec une taille de 6
    assert len(genererMDPcleMaitre("noix", 6)) == 6
    #Test avec une taille de 7
    assert len(genererMDPcleMaitre("igloo", 7)) == 7
    #Test avec une taille de 8
    assert len(genererMDPcleMaitre("gingembre", 8)) == 8
    #Test avec une taille de 9
    assert len(genererMDPcleMaitre("gourde", 9)) == 9
    #Test avec une taille de 10
    assert len(genererMDPcleMaitre("ere", 10)) == 10
    #Test avec une taille de 11
    assert len(genererMDPcleMaitre("reflexe", 11)) == 11
    #Test avec une taille de 12
    assert len(genererMDPcleMaitre("salutation", 12)) == 12

