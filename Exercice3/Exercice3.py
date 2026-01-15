#Création de la classe outils et du constructeur
class Outils:
    def __init__(self):
        self.nombres = []
#fonction pour saisir les 10 entiers
    def saisir(self):
        for i in range(10):
            n = int(input("Entrez un nombre : "))
            self.liste.append(n)

#Fonction pour trouver le plus petit entier
    def min(self):
        petit = self.liste[0]
        for x in self.liste:
            if x < petit:
                petit = x
        return petit

# Fonction pour trouver le plus grand entier
    def max(self):
        grand = self.liste[0]
        for x in self.liste:
            if x > grand:
                grand = x
        return grand

 # Fonction pour calculer la somme
    def somme(self):
        total = 0
        for x in self.liste:
            total = total + x
        return total

# Fonction pour calculer la moyenne
    def moyenne(self):
        return self.somme() / 10