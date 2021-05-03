"""Écrivez une classe Fraction qui crée des objets initialisés avec deux nombres entiers
.num et .denom pour le numérateur et le dénominateur. Ajoutez une méthode .affiche() qui
affiche une représentation de la fraction. Ajoutez des méthodes spéciales pour pouvoir utiliser les
opérateurs +, -, *, /.
Pour réduire la fraction, vous pouvez employer la fonction math.gcd(a, b) du module math, qui
calcule le plus grand commun diviseur entre deux entiers a et b."""

class Fraction:
    def __init__(self, x, y):
        self.num = x
        self.denom = y

    def affiche(self):
        R = str(self.num) + "/" + str(self.denom)
        return R

fra = Fraction(1,2)
print(fra.affiche())


"""
1
>>> f = Fraction(3, 4)
>>> f.affiche()
3/4
>>> g = Fraction(1, 2)
>>> g.affiche()
1/2
>>> r1 = f + g
>>> r.affiche()
5/4
>>> r2 = f / g
>>> r2.affiche()
"""