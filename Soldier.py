import random

from Bow import Bow
from Sword import Sword
from Armor import Armor


class Soldier:
    def __init__(self, n, h=100):
        self.name = n
        self.hp = h
        self.weapon = self.get_weapon()
        self.armor = self.get_armor()
        self.state = []

    def get_weapon(self):
        arr_weapon = []
        number_weapon = random.randint(0, 2)
        for i in range(0, number_weapon):
            effect = {
                0: [],
                1: ['Fire'],
                2: ['Cold'],
            }.get(random.randint(0, 2))
            sword = Sword('sword', random.randint(20, 25), effect)
            bow = Bow('bow', random.randint(20, 30), random.randint(70, 90) / 100., effect)
            if bow.__le__(sword):
                print(self.name, 'получил sword Урон:', sword.get_dmg(), 'эффект', sword.effect)
                arr_weapon.append(sword)
            else:
                print(self.name, 'получил bow Урон:', bow.get_dmg(), 'эффект', bow.effect)
                arr_weapon.append(bow)
        return arr_weapon

    def get_armor(self):
        effect = {
            0: [],
            1: ['Fire'],
            2: ['Cold'],
            3: ['Fire', 'Cold']
        }.get(random.randint(0, 3))
        return Armor(100, effect)

    def attack(self, second_soldier):
        print(self.name, '!attack!', second_soldier.name)
        effect = self.get_state_effect()
        if 'Fire' in effect:
            self.hp -= 5
            print(self.name, 'is on Fire, получает 5 урона')
        if 'Cold' in effect:
            print(self.name, 'is on Cold')
        else:
            second_soldier.get_dmg(self.get_best_weapon_dmg())
            if second_soldier.hp < 0:
                print(self.name, ' убил ', second_soldier.name)
                if len(second_soldier.weapon) > 0:
                    self.weapon.append(second_soldier.weapon[0])

    def get_state_effect(self):
        arr_state_effect = []
        for item in self.state:
            if item.time_of_action < 0:
                self.state.remove(item)
            else:
                arr_state_effect.append(item.get_state())
        return arr_state_effect

    def get_best_weapon_dmg(self):
        self.weapon = sorted(self.weapon)
        print(self.name, 'has weapon: ', [str(elem) for elem in self.weapon])
        if len(self.weapon) > 0:
            return self.weapon[0].dmg_attack()
        else:
            return [5, []]

    def get_dmg(self, dmg):
        damage, effect = dmg
        if self.armor.get_hp() > 0:
            self.armor.get_dmg(damage)
            if self.armor.get_hp() < 0:
                self.hp -= abs(self.armor.get_hp())
                print('Armor', self.name, 'crashed!')
        else:
            self.hp -= dmg[0]
        print(self.name, f'Осталось: {round(self.hp, 2)} хп и {self.armor.get_hp()} брони')
        if len(effect) > 0 and len(self.armor.atr) > 0:
            for item in effect:
                if str(item) in self.armor.atr and random.randint(0, 100) < 80:
                    effect.remove(item)
                    print('Effect block!')
        if len(effect) > 0:
            print(f' На {self.name} были повешены эффекты {[str(i) for i in effect]}')
        self.state = self.state + effect

    def __str__(self):
        return self.name + ' здоровье: ' + str(round(self.hp, 2)) + ' оружие: ' + str([str(i) for i in self.weapon]) + \
               ' броня: ' + str(self.armor) + ' состояние: ' + str([str(i) for i in self.state])

    def __del__(self):
        print(f"Valhalla, {self.name} is coming")
        del self
