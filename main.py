from random import randrange


class Soldier:
    def __init__(self, h, d, n):
        self.hp = h
        self.dmg = d
        self.name = n

    def random_attack(self, arr_soldiers):
        if self in arr_soldiers:
            arr_soldiers.remove(self)
        for item in arr_soldiers:
            if item is None:
                arr_soldiers.remove(item)
        if len(arr_soldiers) > 0:
            self.attack(arr_soldiers[randrange(len(arr_soldiers))], arr_soldiers)
        arr_soldiers.append(self)
        return arr_soldiers

    def attack(self, second_soldier, arr_soldiers):
        print(self.name, '!attack!', second_soldier.name)
        second_soldier.get_dmg(self.dmg)

    def get_dmg(self, dmg):
        self.hp = self.hp - dmg
        print(self.name, f'Осталось: {self.hp} хп')

    def get_info(self):
        print(self.name, self.hp, self.dmg)

    def __del__(self):
        print(f"Valhalla, {self.name} is coming")
        del self

    def __str__(self):
        return self.name


if __name__ == '__main__':
    soldier1 = Soldier(100, 20, 'soldier_1')
    soldier2 = Soldier(100, 20, 'soldier_2')
    soldier3 = Soldier(100, 20, 'soldier_3')
    soldiers = [soldier1, soldier2, soldier3]
    while True:
        soldier = soldiers[randrange(len(soldiers))]
        if 'soldier1' in locals() and len(soldiers) > 1 and soldier == soldier1:
            if soldier1.hp == 0:
                soldiers.remove(soldier1)
                del soldier1
            else:
                soldier1.random_attack(soldiers)
        if 'soldier2' in locals() and len(soldiers) > 1 and soldier == soldier2:
            if soldier2.hp == 0:
                soldiers.remove(soldier2)
                del soldier2
            else:
                soldier2.random_attack(soldiers)
        if 'soldier3' in locals() and len(soldiers) > 1 and soldier == soldier3:
            if soldier3.hp == 0:
                soldiers.remove(soldier3)
                del soldier3
            else:
                soldier3.random_attack(soldiers)

        if 'soldier1' in locals():
            if soldier1.hp <= 0:
                soldiers.remove(soldier1)
                del soldier1
        if 'soldier2' in locals():
            if soldier2.hp <= 0:
                soldiers.remove(soldier2)
                del soldier2
        if 'soldier3' in locals():
            if soldier3.hp <= 0:
                soldiers.remove(soldier3)
                del soldier3

        for elem in soldiers:
            if elem is not None:
                elem.get_info()
        if len(soldiers) == 1:
            print(soldiers[0], 'is winner!')
            soldiers[0].get_info()
            break
