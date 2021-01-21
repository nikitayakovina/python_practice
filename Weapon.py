class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_damage(self):
        raise Exception('Method not implemented!')

    def attack(self):
        raise Exception('Method not implemented!')

