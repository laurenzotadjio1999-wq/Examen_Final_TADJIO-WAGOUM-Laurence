#Création de la classe outils et du constructeur
class Outils:
    def __init__(self):
        self.nombres = []

#fonction pour saisir les 10 entiers
    def saisir(self):
        for i in range(10):
            n = int(input("Entrez un nombre : "))
            self.nombres.append(n)

#Fonction pour trouver le plus petit entier
    def min(self):
        petit = self.nombres[0]
        for x in self.nombres:
            if x < petit:
                petit = x
        return petit

# Fonction pour trouver le plus grand entier
    def max(self):
        grand = self.nombres[0]
        for x in self.nombres:
            if x > grand:
                grand = x
        return grand

 # Fonction pour calculer la somme
    def somme(self):
        total = 0
        for x in self.nombres:
            total = total + x
        return total

# Fonction pour calculer la moyenne
    def moyenne(self):
        return self.somme() / 10


#Création d'un objet (O) de type outils pour faire les tests.

O = Outils()
O.saisir()

print("Minimum :", O.min())
print("Maximum :", O.max())
print("Somme :", O.somme())
print("Moyenne :", O.moyenne())