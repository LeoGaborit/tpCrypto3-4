"""
Tests pour la fonction genererMDP de l'exercice 1
/!\ Attention, les tests ne sont pas exhaustifs

Chemin vers le script principal : src/main/exo1.py
"""

from src.main.exo1 import genererMDP

print(genererMDP("hello", "world")) # 8 caractères
assert len(genererMDP("hello", "world")) == 8

print(genererMDP("test", "mdp")) # 8 caractères
assert len(genererMDP("test", "mdp")) == 8
