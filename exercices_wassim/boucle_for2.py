# Pour un chiffre entre 1500 et 2700 inclus,
# vérifier que le chiffre est divisible par 7
# et en même temps multiple de 5

"""
for i in range(1500,2701)
if i%7 == 0 and i%5 == 0
print (i)
"""

j = 1715
ma_liste = []

for i in range(1500,2701):
    if i%7 == 0 and i%5 == 0:
        if i == j:
            i = "jackpot"
        ma_liste.append(i)

print(ma_liste)