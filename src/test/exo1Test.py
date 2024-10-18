"""
Tests pour la fonction genererMDP de l'exercice 1
/!\ Attention, les tests ne sont pas exhaustifs

Chemin vers le script principal : src/main/exo1.py
"""

from src.main.exo1 import genererMDP

def test_exo1():
    # Test avec des entrées valides (4 + 4 => 8)
    assert len(genererMDP("hello", "world")) == 8

    # Test avec des entrées valides (4 + 3 => 8)
    assert len(genererMDP("test", "mdp")) == 8

    # Test avec des entrées valides (5 + 3 => 8)
    assert len(genererMDP("BONJO", "URE")) == 8

    # Test avec des entrées valides (7 + 2 => 8)
    assert len(genererMDP("BONJOUR", "UR")) == 8
