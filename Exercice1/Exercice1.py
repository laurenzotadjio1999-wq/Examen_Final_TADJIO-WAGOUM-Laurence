#Création de la classe triangle et du constructeur
class Triangle:
    def __init__(self,n):
        self.n = n
        self.symbol = '*'
#Création des lignes d'étoiles
    def lignes(self, i):
        ligne = self.symbol * i
        espace = " " * (self.n - i)
        return espace + ligne + " " + ligne

