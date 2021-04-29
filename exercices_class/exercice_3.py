class Vehicule:
    moteur = 1
    def __init__(self):
        self.marque = "la marque de mon vehicule"

class Voiture(Vehicule):
    fenetres = 4
    volant = 1
    def __init__(self, marque):
        self.marque = marque
    def rouler(self):
        return "vroum vroum"

class Moto(Vehicule):
    roues = 2

ma_moto = Moto()
print(ma_moto.roues)
print(ma_moto.marque)