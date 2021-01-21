import unittest

import Bow
import Sword


class TestWeaponMethods(unittest.TestCase):

    def test_Sword_Dmg_Attack(self):
        sword = Sword.Sword('Sword', 20, 'Cold')
        self.assertEqual(sword.dmg_attack(), 20)

    def test_Sword_Get_Dmg(self):
        sword = Sword.Sword('Sword', 20, 'Fire')
        self.assertEqual(sword.get_dmg(), 20)

    def test_Bow_Dmg_Attack(self):
        bow = Bow.Bow('Bow', 20, .9, 'Cold')
        dmg = bow.dmg_attack()
        self.assertTrue(dmg == 18 or dmg == 0)

    def test_Bow_Get_Dmg(self):
        bow = Bow.Bow('Bow', 20, .9, 'Fire')
        self.assertEqual(bow.get_dmg(), 18)

    def test_le_1(self):
        sword = Sword.Sword('Sword_1', 20, 'Cold')
        bow = Bow.Bow('Bow', 20, .9, 'Fire')
        self.assertFalse(sword.__le__(bow))

    def test_le_2(self):
        sword = Sword.Sword('Sword_1', 20, 'Cold')
        bow = Bow.Bow('Bow', 25, .9, 'Fire')
        self.assertTrue(sword.__le__(bow))


if __name__ == '__main__':
    unittest.main()