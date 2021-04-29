"""Écrivez une classe Domino pour représenter une pièce de domino. Les objet sont
initialisés avec les valeurs des deux faces, A et B. Ajoutez une méthode .affiche_points() qui
affiche les valeurs des deux faces, et une méthode .totale() qui retourne la somme de deux
valeurs."""

class Domino:
    def __init__(self, A, B):
        self.faceA = A
        self.faceB = B
    def affiche_points(self):
        print("face A = ", self.faceA)
        print("face B = ", self.faceB)
    def change_face(self):
        self.faceX = self.faceA
        self.faceA = self.faceB
        self.faceB = self.faceX
    def totale(self):
        print("le total = ", self.faceA + self.faceB)

domino = Domino(4,6)
domino.affiche_points()
domino.change_face()
domino.totale()

"""
d = Domino(4, 6)
d.affiche_points()
face A: 4, face B: 6
x = d.totale()
print(x)
"""