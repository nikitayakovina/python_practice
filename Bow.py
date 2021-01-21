import random

from Weapon import Weapon
from Cold import Cold
from Fire import Fire


class Bow(Weapon):
    def __init__(self, n, dmg, chance, effect):
        super().__init__(n, dmg, effect)
        self.chance = chance

    def dmg_attack(self):
        if random.random() < self.chance:
            return [self.get_dmg(), self.get_effect()]
        else:
            print('Промах!')
            return [0, self.get_effect()]

    def get_effect(self):
        arr_effect = []
        if self.effect == 'Fire':
            arr_effect.append(Fire(10, 5))
        if self.effect == 'Cold':
            arr_effect.append(Cold(2))
        return arr_effect

    def get_dmg(self):
        return round(self.chance * self.dmg)

    def __le__(self, other):
        return self.get_dmg() <= other.get_dmg()

    def __str__(self):
        return self.name + ' урон  ' + str(self.dmg) + '  шанс попадания  ' + str(self.chance) +\
               ' эффект ' + str([str(i) for i in self.effect])
