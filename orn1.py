class Roket:
        def __init__(self, yakit):
                self.yakit = yakit
        def uc(self, mesafe):
                if mesafe <= self.yakit:
                    self.yakit -= mesafe
                    return f"{mesafe} km mesafe katedildi!"
                else:
                    return "Yetersiz yakıt!"

import unittest

class TestRoket(unittest.TestCase):
    def test_uc(self):
        roket = Roket(200)
        self.assertEqual(roket.uc(50), "50 km mesafe katedildi!")
        self.assertEqual(roket.uc(160), "Yetersiz yakıt!")
        
if __name__ == '__main__':
    unittest.main()