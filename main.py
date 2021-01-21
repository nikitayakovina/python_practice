import random
from Soldier import Soldier

if __name__ == '__main__':
    soldier1 = Soldier('soldier_1')
    soldier2 = Soldier('soldier_2')
    soldier3 = Soldier('soldier_3')
    soldiers = [soldier1, soldier2, soldier3]
    print()

    while True:
        random_soldier_1 = random.choice(soldiers)
        random_soldier_2 = random.choice(soldiers)
        if random_soldier_1 != random_soldier_2:
            random_soldier_1.attack(random_soldier_2)
            if random_soldier_2.hp <= 0:
                for elem in soldiers:
                    if random_soldier_2.name == elem.name:
                        soldiers.remove(elem)
                        elem.__del__()
            print()
            for elem in soldiers:
                if elem is not None:
                    print(elem)
            print()

        if len(soldiers) == 1:
            print(soldiers[0].name, 'is winner!')
            print(soldiers[0])
            break