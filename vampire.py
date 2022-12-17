from Character import Character

class Vampire(Character):


    def __init__(self, name, health=100, damage=1, defence=0):
        Character.__init__(self, name, health, damage, defence)


    def healing(self, target):
        healing = self.damage
        self.health = self.health + healing