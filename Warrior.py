import random
from Sword import Sword
from Bow import Bow


class Warrior:
    def __init__(self, name, strength=20, health=100):
        self.name = name
        self.strength = strength
        self.health = health
        self.weapon = self.choice_weapon()

    def choice_weapon(self):
        sword = Sword('sword', random.randint(20, 25))
        bow = Bow('bow', random.randint(20, 30), random.randint(70, 90) / 100.)
        if bow.__le__(sword):
            print(self.name, 'get sword Урон:', sword.get_damage())
            return sword
        else:
            print(self.name, 'get bow Урон:', bow.get_damage())
            return bow

    def attack(self, second_unit):
        print('%s attack %s' % (self.name, second_unit.name))
        second_unit.health -= self.strength
        print('%s осталось здоровья %s \n' % (second_unit.name, second_unit.health))

    def __str__(self):
        return self.name + ' здоровье: ' + str(round(self.health, 2)) + ' урон: ' + str(round(self.weapon.get_damage()))

    def __del__(self):
        print(f"Valhalla, {self.name} is coming \n")
        del self
