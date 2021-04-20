import unittest
from watts import watts

class WattsTests(unittest.TestCase):
    
    def test_converts_megawatts_to_co2e_for_akgd(self):
        self.assertEqual(watts(1, "AKGD"), 1045.0)
    
    def test_converts_megawatts_to_co2e_for_frcc(self):
        self.assertEqual(watts(1, "FRCC"), 936.1)

    def test_converts_megawatts_to_co2e_for_us(self):
        self.assertEqual(watts(1, ""), 952.9)

if __name__ == '__main__':
    unittest.main()