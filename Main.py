from Warrior import Warrior
import random

if __name__ == "__main__":
    unit1 = Warrior('Unit1')
    unit2 = Warrior('Unit2')
    unit3 = Warrior('Unit3')
    print()
    unit_list = [unit1, unit2, unit3]

    while True:
        first_unit = random.choice(unit_list)
        second_unit = random.choice(unit_list)
        if first_unit != second_unit:
            second_unit.attack(first_unit)
            for item in unit_list:
                if item.health <= 0:
                    item.__del__()
                    unit_list.remove(item)
        if len(unit_list) == 1:
            print(unit_list[0].name, 'is winner! \n')
            print(unit_list[0], '\n')
            break
