class HesapMakinesi:
    def topla(self, a, b):
        return a + b
    def cikar(self, a, b):
        return a - b
    def carp(self, a, b):
        return a * b
    def bol(self, a, b):
        if b == 0:
            return "Tanımsız!"
        return a / b
        
import unittest

class TestHesapMakinesi(unittest.TestCase):
    def test_topla(self):
        hm = HesapMakinesi()
        self.assertEqual(hm.topla(3, 5), 8)
    def test_cikar(self):
        hm = HesapMakinesi()
        self.assertEqual(hm.cikar(3, 5), -2)
    def test_carp(self):
        hm = HesapMakinesi()
        self.assertEqual(hm.carp(3, 5), 15)
    def test_bol(self):
        hm = HesapMakinesi()
        self.assertEqual(hm.bol(3, 5), 0.6)
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHesapMakinesi))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())