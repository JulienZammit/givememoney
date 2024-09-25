import unittest
from givememoneyjulienbis.main import give_me_money_julien_bis

class MyTestCase(unittest.TestCase):
    def test_something(self):
        compte_en_banque = give_me_money_julien_bis(8, 10)
        self.assertEqual(compte_en_banque, 18)
        
if __name__ == '__main__':
    unittest.main()
