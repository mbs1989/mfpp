class Vehicule:
    roues = 4
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

#Modifier ce qu'il faut dans la classe Voiture pour qu'elle hérite des attributs de la classe
#Vehicule et qu'elle surcharge sa marque au moment de la création de l'objet

ma_marque = "mercedes"
ma_marque2 = "bmw"
mercedes = Voiture(ma_marque)
bmw = Voiture(ma_marque2)
print(mercedes.marque)
print(bmw.marque)
print(dir(bmw.rouler()))
print(bmw.__dict__)

mon_vehicule = Voiture(ma_marque)
print(mon_vehicule.marque)
print(mon_vehicule.roues)