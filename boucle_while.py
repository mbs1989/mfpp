# Pour tous les chiffres allant jusqu'à 100, afficher les nombres pairs

i = 200

while i < 100:
    if i%2 == 0:
        print(i)
    else:
        print("ceci est un nombre impair")
    i += 1
else:
    print("le chiffre est trop grand")