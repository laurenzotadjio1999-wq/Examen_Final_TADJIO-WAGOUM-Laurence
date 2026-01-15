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

#Création de la classe Affichage
class Affichage:
    def executer(self):
        n = int(input("saisir le nombre de lignes : "))
        T=Triangle(n)
        for i in range(0, n):
            print(T.lignes(i))
Affichage().executer()