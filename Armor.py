class Armor:
    def __init__(self, hp, atr):
        self.hp = hp
        self.atr = atr

    def get_dmg(self, hp):
        self.hp -= hp
        if self.hp >= 0:
            return 0
        else:
            return abs(self.hp)

    def get_hp(self):
        return self.hp if self.hp > 0 else 0

    def dmg_attack(self):
        raise Exception('Method not implemented!')

    def __le__(self, other):
        return self.dmg_attack() <= other.dmg_attack()

    def __str__(self):
        return 'Здоровье: ' + str(self.hp) + ' эффект: ' + str(self.atr)