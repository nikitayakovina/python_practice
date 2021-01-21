from Weapon import Weapon
import random


class Bow(Weapon):

    def __init__(self, name, damage, chance):
        super().__init__(name, damage)
        self.chance = chance

    def get_damage(self):
        return self.damage * (self.chance * 0.01)

    def attack(self):
        if random.random() <= self.chance * 0.01:
            return self.get_damage()
        else:
            return 0

    def __le__(self, other):
        return self.get_damage() <= other.get_damage()

    def __str__(self):
        return self.name + ' урон ' + str(self.damage) + ' шанс попадания ' + str(self.chance)