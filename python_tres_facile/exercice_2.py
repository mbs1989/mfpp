"""
Ecrire un programme en Python qui demande à l'utilisateur
de saisir deux nombres a et b et de lui afficher leur somme : a + b
"""

def somme(a,b):
    r = a + b
    return r

x = int(input("Saisissez votre premier chiffre "))
y = int(input("saisissez votre deuxieme chiffre "))

mon_resultat = somme(x,y)
print("la somme est", mon_resultat)