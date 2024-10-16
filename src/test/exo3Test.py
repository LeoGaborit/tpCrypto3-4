"""
Tests pour le fichier exo3.py
/!\ Attention, les tests ne sont pas exhaustifs

Chemin vers le script principal : src/main/exo3.py
"""

#Création des tests

from ..main.exo3 import genererMDPtailleN, lireMPWD, demanderNouveauMDP
import hashlib

def test_genererMDPtailleN():
    #Test avec une taille de 1
    assert len(genererMDPtailleN("hello", 1)) == 1
    #Test avec une taille de 2
    assert len(genererMDPtailleN("hello", 2)) == 2
    #Test avec une taille de 3
    assert len(genererMDPtailleN("hello", 3)) == 3
    #Test avec une taille de 4
    assert len(genererMDPtailleN("hello", 4)) == 4
    #Test avec une taille de 5
    assert len(genererMDPtailleN("hello", 5)) == 5
    #Test avec une taille de 6
    assert len(genererMDPtailleN("hello", 6)) == 6
    #Test avec une taille de 7
    assert len(genererMDPtailleN("hello", 7)) == 7
    #Test avec une taille de 8
    assert len(genererMDPtailleN("hello", 8)) == 8
    #Test avec une taille de 9
    assert len(genererMDPtailleN("hello", 9)) == 9
    #Test avec une taille de 10
    assert len(genererMDPtailleN("hello", 10)) == 10
    #Test avec une taille de 11
    assert len(genererMDPtailleN("hello", 11)) == 11
    #Test avec une taille de 12
    assert len(genererMDPtailleN("hello", 12)) == 12

