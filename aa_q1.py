class plant:
    def __init__(self,name,health,damage):
        self.name = name
        self.health = health
        self.damage = damage
    def attack(self, zombie, turn):
        if self.name == "Sundew" and turn % 3 == 0:
            print(self.name, "uses Sticky Trap!")
            special_damage = self.damage * 2
            print(self.name, "attacks the zombie for", special_damage, "damage!")
            zombie.take_damage(special_damage)
        else:
            print(self.name, "attacks the zombie for", self.damage, "damage!")
            zombie.take_damage(self.damage)
class zombie:
    def __init__(self,name,health,damage):
        self.name = name
        self.health = health
        self.damage = damage
    def move(self):
        if self.distance > 0:
            self.distance -= 1
            print(self.name, "The zombie moves closer!")
    def attack(self, plant):
        print(self.name, "attacks the plant for", self.damage, "damage!")
        plant.take_damage(self.damage)
    def take_damage(self, damage):
        self.health -= damage
        print(self.name, "takes", damage, "damage! Health is now", self.health)
        if self.health <= 0:
            print(self.name, "has been defeated!")

Sundew = plant("Sundew", 39, 160)
Brightfleur = plant("Brightfleur", 35, 150)

Zombobious = zombie("Zombobious", 30, 120)

Turn = 1
while True: 
    print("\nTurn", Turn)
    if Brightfleur.health > 0:
        Brightfleur.attack(Zombobious, Turn)
        if Zombobious.health <= 0:
            print("The plants have defeated the zombie!")
            print("Plants win!!!")
            break
    if Sundew.health > 0:
        Sundew.attack(Zombobious, Turn)
        if Zombobious.health <= 0:
            print("The plants have defeated the zombie!")
            print("Plants win!!!")
            break
    if Zombobious.health > 0:
        Zombobious.attack(Brightfleur)
        if Brightfleur.health <= 0 and Sundew.health <= 0:
            print("The zombie has defeated the plants!")
            print("Zombie wins!!!")
            break
    