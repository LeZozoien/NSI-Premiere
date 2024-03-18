class Humain: # Définition d'une nouvelle classe


    # Définition des arguments de la classe
    def __init__(self, genre, age, maladie, puissance, pv, defense):
        self.maladies = maladie
        self.genre = genre
        self.age = age
        self.rok = puissance
        self.health = pv
        self.defense = defense

    # Nouvelle fonction qui augmente l'age de 1
    def anniv(self):
        self.age += 1

    # Nouvelle fonction pour attaquer qqn
    def attack(self, target):
        target.health -= self.rok
        target.defend()
    
    # Nouvelle fonction pour se défendre contre qqn
    def defend(self, target):
        target.health -= self.defense


# Attribution de la classe à des variables
clement = Humain("Homme", 15, "Cancer", 80, 100, 40)
enzo = Humain("Homme", 15, "", 75, 100, 50)


print(clement.health, enzo.health)
enzo.attack(clement)
print(clement.health, enzo.health)