#Création de la classe outils et du constructeur
class Outils:
    def __init__(self):
        self.nombres = []
#fonction pour saisir les 10 entiers
    def saisir(self):
        for i in range(10):
            n = int(input("Entrez un nombre : "))
            self.liste.append(n)