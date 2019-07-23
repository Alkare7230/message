#coding:utf-8

class vehicule:

    def __init__(self, nm_vehicule, sp98):
        self.nom = nm_vehicule
        self.essence = sp98

    def mouv(self):
        print("ça roule {} lol".format(self.nom))

class voiture(vehicule):
    def __init__(self, type_voiture, essence, puissance):
        vehicule.__init__(self, nm_vehicule, essence)
        self.puissance = puissance



voiture1 = voiture("New Beetle", 45, 250)
voiture1.mouv()
