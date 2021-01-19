class Warrior:
    def __init__(self, name, strength=20, health=100):
        self.name = name
        self.strength = strength
        self.health = health

    def attack(self, second_unit):
        print('%s attack %s' % (self.name, second_unit.name))
        second_unit.health -= self.strength
        print('%s осталось здоровья %s \n' % (second_unit.name, second_unit.health))

    def __str__(self):
        return self.name + ' здоровье: ' + str(self.health) + ' урон: ' + str(self.strength)

    def __del__(self):
        print(f"Valhalla, {self.name} is coming \n")
        del self
