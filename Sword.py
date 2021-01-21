import random

from Weapon import Weapon
from Cold import Cold
from Fire import Fire


class Sword(Weapon):
    def __init__(self, n, dmg, effect):
        super().__init__(n, dmg, effect)
        self.wholeness = 1.

    def get_dmg(self):
        return round(self.dmg * self.wholeness) if self.wholeness > 0 else 0

    def dmg_attack(self):
        dmg = self.get_dmg()
        if self.wholeness > 0:
            if random.randint(0, 100) > 50:
                self.wholeness -= 0.1
            return [dmg, self.get_effect()]
        else:
            return [5, []]

    def get_effect(self):
        arr_effect = []
        if 'Fire' in self.effect:
            arr_effect.append(Fire(10, 5))
        if 'Cold' in self.effect:
            arr_effect.append(Cold(2))
        return arr_effect

    def __le__(self, other):
        return self.get_dmg() <= other.get_dmg()

    def __str__(self):
        return self.name + ' урон  ' + str(self.dmg) + '  целостность  ' + str(round(self.wholeness, 2)) + ' эффекты: '\
               + str([str(i) for i in self.effect])
