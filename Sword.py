from Weapon import Weapon
import random


class Sword(Weapon):

    def __init__(self, name, damage, stamina=1):
        super().__init__(name, damage)
        self.stamina = stamina

    def get_damage(self):
        return self.damage * self.stamina

    def attack(self):
        attack_damage = self.get_damage()
        if random.choice([True, False]) == True:
            self.stamina -= 0.1
        return attack_damage

    def __le__(self, other):
        return self.get_damage() <= other.get_damage()

    def __str__(self):
        return self.name + ' урон ' + str(self.damage) + ' целостность ' + str(self.stamina)