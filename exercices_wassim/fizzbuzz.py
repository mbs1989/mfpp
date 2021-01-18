# Afficher chiffres de 1 à 50. Si le chiffre est multiple de 3, le système doit afficher
# fizz.
# Si le chiffre est multiple de 5, afficher buzz.
# Si le chiffre est multiple de 3 et de 5 afficher fizzbuzz

"""
for 1 to 50
if i module 3 == 0 and i modulo 5 == 0
print("fizzbuzz")
if i modulo 3 == 0
print("fizz")
if i modulo 5 == 0
print("buzz")
else print(i)
i = 10
i = 9
i = 15
"""

for i in range(50):
    if i%3 == 0 and i%5 == 0:
        print("fizzbuzz")
    elif i%3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzzz")
    else:
        print(i)