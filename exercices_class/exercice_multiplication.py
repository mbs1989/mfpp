"""
Generateurs. Écrivez une classe TableMultiplication qui crée des objets initialisés
avec un nombre entier. Ajouter une méthode .prochain() qui renvoie à chaque appel un nouveau
terme de la table de multiplication correspondante.
"""

class TableMultiplication:
    n = 0

    def __init__(self, i):
        self.entier = i

    def prochain(self):
        multi = self.entier * self.n
        self.n += 1
        return multi

tab = TableMultiplication(2)

i = 0
while i < 1000:
    resultat = tab.prochain()
    if resultat == 1990:
        print("nineties")
    else:
        print(resultat)
    i = i + 1






"""
>>> tab = TableMultiplication(3)
>>> tab.prochain()
0
>>> tab.prochain()
3
>>> tab.prochain()
6
>>> tab.prochain()
9
"""