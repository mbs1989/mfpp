"""Écrivez une classe CompteBancaire. Les objets sont initialisés avec le nom du titulaire
et le solde. L’argument solde doit être facultatif et avoir une valeur prédéfinie zéro. Ajoutez
deux méthodes .depot(somme) et .retrait(somme) pour changer le solde. Ajoutez une méthode
.affiche() qui montre le solde courant."""

class CompteBancaire:
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde
    def depot(self, somme):
        self.solde += somme
        return self
    def retrait(self, somme):
        self.solde -= somme
        return self
    def affiche(self):
        print("le solde est =", self.solde)

compte1 = CompteBancaire("société générale")
print(compte1.solde)

print(compte1.depot(50).retrait(20).solde)
compte1.affiche()

"""
>>> compte1 = CompteBancaire(’Jean’, 1000)
>>> compte1.retrait(200)
>>> compte1.affiche()
Le solde du compte de Jean est 800 euros.
>>> compte2 = CompteBancaire(’Marc’)
>>> compte2.depot(500)
>>> compte2.affiche()
Le solde du compte de Marc est 500 euros."""