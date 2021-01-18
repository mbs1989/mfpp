"""
Ecrire un programme en Python qui demande à l'utilisateur
de saisir 3 nombre x, y et z et de lui afficher leur maximum
"""

x = int(input("Saisissez le premier chiffre "))
y = int(input("Saisissez le deuxieme chiffre "))
z = int(input("Saisissez le troisieme chiffre "))

if x > y > z:
    print("Le maximum est", x)
elif y > x > z:
    print("Le maximum est", y)
else:
    print("Le maximum est", z)




