# Créer une fonction qui prend deux paramètres, qui les compare et qui retourne le plus grand
# Deux paramètres donnés par utilisateur puis script

def compare(x,y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "les deux chiffres sont egaux"


A1 = int(input("quel est ton premier chiffre "))
A2 = int(input("quel est ton deuxieme chiffre "))


resultat = compare(A1,A2)
print(resultat)