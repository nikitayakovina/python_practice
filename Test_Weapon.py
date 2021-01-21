import unittest

import Bow
import Sword


class TestWeaponMethods(unittest.TestCase):

    def test_Sword_Dmg_Attack(self):
        sword = Sword.Sword('Sword', 20)
        self.assertEqual(sword.attack(), 20)

    def test_Sword_Get_Dmg(self):
        sword = Sword.Sword('Sword', 20)
        self.assertEqual(sword.get_damage(), 20)

    def test_Bow_Dmg_Attack(self):
        bow = Bow.Bow('Bow', 20, .9)
        dmg = bow.attack()
        self.assertTrue(dmg == 18 or dmg == 0)

    def test_Bow_Get_Dmg(self):
        bow = Bow.Bow('Bow', 20, .9)
        self.assertEqual(bow.get_damage(), 18)

    def test_le_1(self):
        sword = Sword.Sword('Sword_1', 20)
        bow = Bow.Bow('Bow', 20, .9)
        self.assertFalse(sword.__le__(bow))

    def test_le_2(self):
        sword = Sword.Sword('Sword_1', 20)
        bow = Bow.Bow('Bow', 25, .9)
        self.assertTrue(sword.__le__(bow))


if __name__ == '__main__':
    unittest.main()
