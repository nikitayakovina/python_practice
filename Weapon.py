class Weapon:
    def __init__(self, n, dmg, effect):
        self.name = n
        self.dmg = dmg
        self.effect = effect

    def get_dmg(self):
        raise Exception('Method not implemented!')

    def dmg_attack(self):
        raise Exception('Method not implemented!')

    def get_effect(self):
        raise Exception('Method not implemented!')

    def __le__(self, other):
        return self.get_dmg() <= other.get_dmg()

    def __gt__(self, other):
        return self.get_dmg() > other.get_dmg()
