def metniCevir(metin, duzen):
    if duzen == "küçük":
        return metin.lower()
    elif duzen == "büyük":
        return metin.upper()
    elif duzen == "tümce":
        return metin.title()
    else:
        return "hata"

import unittest
class TestMetin(unittest.TestCase):
    def test_metniCevir(self):
        self.assertEqual(metniCevir("AbC dEf", "küçük"), "abc def")
        self.assertEqual(metniCevir("AbC dEf", "büyük"), "ABC DEF")
        self.assertEqual(metniCevir("AbC dEf", "tümce"), "Abc Def")
        
if __name__ == '__main__':
    unittest.main(exit=False)