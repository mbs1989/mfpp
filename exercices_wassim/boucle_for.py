# Afficher uniquement le premier chiffre supérieur à 5

liste = [0,1,2,3,4]
new_liste = []

for i in liste:
    if i%2 == 0:
        print("ceci est un chiffre pair", i)
        new_liste.append(i)
    else:
        print("ceci est un chiffre impair", i)

print(new_liste)