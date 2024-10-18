"""
Tests pour la fonction genererMDPtailleN de l'exercice 2
/!\ Attention, les tests ne sont pas exhaustifs

Chemin vers le script principal : src/main/exo2.py
"""

from src.main.exo2 import genererMDPtailleN
def test_exo2():
    # Test avec des entrées valides (4 + 4 => 8)
    print(genererMDPtailleN("hello", "world", 12)) # 12 caractères
    assert len(genererMDPtailleN("hello", "world", 12)) == 12

    print(genererMDPtailleN("test", "mdp", 1)) # 1 caractère
    assert len(genererMDPtailleN("test", "mdp", 1)) == 1

    print(genererMDPtailleN("essai", "password", 8)) # 8 caractères
    assert len(genererMDPtailleN("essai", "password", 8)) == 8

    print(genererMDPtailleN("leo", "florian", 4)) # 4 caractères
    assert len(genererMDPtailleN("leo", "florian", 4)) == 4