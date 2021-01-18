"""
Ecrire un programme en langage Python qui demande à l'utilisateur
de saisir son nombre entier et de lui afficher si ce nombre est pair ou impair.
"""

i = int(input("Saisissez un nombre entier "))

if i%2 == 0:
    print("Ce nombre est pair")
else:
    print("Ce nombre est impair")
