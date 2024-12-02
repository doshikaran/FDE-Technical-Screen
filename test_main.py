import unittest
from main import main

class TestMainFunction(unittest.TestCase):
    def test_standard(self):
        # Not bulky and not heavy
        self.assertEqual(main(50, 40, 30, 10), "STANDARD")
        
    def test_bulky_not_heavy(self):
        # Bulky but not heavy
        self.assertEqual(main(200, 50, 30, 10), "SPECIAL")
        
    def test_heavy_not_bulky(self):
        # Heavy but not bulky
        self.assertEqual(main(50, 40, 30, 25), "SPECIAL")
        
    def test_both_bulky_and_heavy(self):
        # Both bulky and heavy
        self.assertEqual(main(200, 200, 200, 50), "REJECTED")
        
    def test_just_below_thresholds(self):
        # Just below thresholds for mass, but bulky due to volume
        self.assertEqual(main(149, 149, 149, 19.9), "SPECIAL")
        
    def test_just_at_thresholds(self):
        # Just at thresholds
        self.assertEqual(main(150, 150, 150, 20), "REJECTED")
        
    def test_volume_threshold(self):
        # Exactly at the volume threshold but dimensions below 150 cm
        self.assertEqual(main(100, 100, 100, 10), "SPECIAL")
        
    def test_mass_threshold(self):
        # Mass at the threshold but not bulky
        self.assertEqual(main(50, 50, 50, 20), "SPECIAL")

# Run the tests
if __name__ == "__main__":
    unittest.main()
