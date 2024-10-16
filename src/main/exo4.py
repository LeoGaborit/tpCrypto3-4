"""
Exercice 4 : Attaques sur des mots de passe
Dans cet exercice, vous allez tenter de trouver des préimages possibles pour le mot de passe maître, c’est
à-dire, vous allez tenter de casser la sécurité de votre générateur de mots de passe.
Votre tâche sera de trouver un mot de passe valide en connaissant le tag utilisé mais pas le mot de passe
maître.

Assurez-vous premièrement que votre fichier de mots de passe maître contient un mot de passe maître
de 10 caractères (à vous de les choisir). Dans votre rapport discutez quelle est la probabilité qu’un
attaquant retrouve ce mot de passe maître par force brute.

Générez, en utilisant votre générateur de mots de passe et le mot de passe maître, des mots de passe
d’un caractère (N=1) pour les tags suivants : Unilim, Amazon, Netflix.

Dans un premier temps votre attaque devra trouver un mot de passe maître qui donnera le même mot
de passe que celui produit par votre vrai mot de passe sur le tag Unilim.

La stratégie sera celle d’une attaque par dictionnaire. Votre dictionnaire doit contenir tous les mots de
passe possibles, avec toutes les possibilités pour chaque caractère. Itérez sur les mots de passe possibles
sur 10 caractères, chaque caractère provenant de votre dictionnaire, jusqu’à trouver un mot de passe
identique (pour le tag Unilim) à celui produit par le gestionnaire de mots de passe. Combien de possibilités
avez-vous essayées ? Quelle est la probabilité théorique de trouver un mot de passe maître qui provoque
une collision et comment votre nombre d’essais se compare à cette valeur ?

Dans un deuxième temps, votre attaque devra retrouver un mot de passe maître qui provoque une
collision sur les 3 tags : Unilim, Amazon et Netflix. Comparez le nombre d’essais nécessaire pour votre
attaque dans ce cas par rapport au cas précédent.

Finalement, essayez la même attaque pour N = 2 et N = 3, en enregistrant le nombre d’essais.

Analyse : Dans votre rapport utilisez les données sur le nombre d’essais pour N = 1, 2 et 3 pour pouvoir
formuler une hypothèse sur le nombre d’essais demandé pour retrouver un mot de passe maître qui
donne des collisions pour des mots de passe de taille N = 8, 10 et 12. Comparez ces chiffres à la probabilité
théorique de réussir, ainsi qu’à la probabilité de trouver le mot de passe maître (quia avait 10 caractères).
Quelles sont vos conclusions par rapport à un design sécurisé et une utilisation correcte de votre
générateur de mots de passe ?

Chemin des dictionnaires :
- Taille 1 : src/main/dictionnaireTaille1.txt
- Taille 2 : src/main/dictionnaireTaille2.txt
- Taille 3 : src/main/dictionnaireTaille3.txt
"""

def charger_dictionnaire(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
            return [ligne.strip() for ligne in fichier]


def attaque_par_force_brute(dictionnaire, hash_cible, fonction_de_hashage):
    for mot in dictionnaire:
        if fonction_de_hashage(mot) == hash_cible:
            return mot
    return None


# Exemple d'utilisation
dictionnaire = charger_dictionnaire('dictionnaire.txt')


# Supposons que vous ayez une fonction qui hash un mot de passe maître
def fonction_de_hashage(mot_de_passe):
    import hashlib
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()


hash_cible = '5e884898da28047151d0e56f8dc6292773603d0d6aabbddad5e6f7e543661814'  # Ex. hash pour 'password'

resultat = attaque_par_force_brute(dictionnaire, hash_cible, fonction_de_hashage)

if resultat:
    print(f"Mot de passe maître trouvé: {resultat}")
else:
    print("Aucun mot de passe maître trouvé dans le dictionnaire.")
