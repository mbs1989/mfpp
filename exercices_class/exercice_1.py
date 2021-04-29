class Voiture:
    roues = 4
    fenetres = 4
    volant = 1
    def __init__(self, marque):
        self.marque = marque

ma_marque = "mercedes"
ma_marque2 = "bmw"
mercedes = Voiture(ma_marque)
bmw = Voiture(ma_marque2)
print(voiture.marque)
print(bmw.marque)