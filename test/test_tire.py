import unittest
from car import Car
from parts.part import Part


from carrigan import Carrigan
from octoprime import Octoprime

class TestCarrigan(unittest.TestCase):
    def test_all_just_work(self):
        ware = [0.89,0.89,0.89,0.89]
        tire = Carrigan(ware)

        self.assertTrue(tire.needs_service())
    
    def test_fist_dosnt_work(self):
        ware = [0.90,0.89,0.89,0.89]
        tire = Carrigan(ware)

        self.assertTrue(tire.needs_service())

    def test_last_dosnt_work(self):
        ware = [0.89,0.89,0.89,0.9]
        tire = Carrigan(ware)

        self.assertTrue(tire.needs_service())
    
    def test_middle_dosnt_work(self):
        ware = [0.89,0.89,0.9,0.89]
        tire = Carrigan(ware)

        self.assertTrue(tire.needs_service())

    def test_fist_very_dosnt_work(self):
        ware = [1,0.89,0.89,0.89]
        tire = Carrigan(ware)

        self.assertTrue(tire.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_all_just_work(self):
        ware = [0.29,0.29,0.29,0.29]
        tire = Octoprime(ware)

        self.assertTrue(tire.needs_service())
    
    def test_fist_dosnt_work(self):
        ware = [0.3,0.29,0.29,0.29]
        tire = Octoprime(ware)

        self.assertTrue(tire.needs_service())

    def test_last_dosnt_work(self):
        ware = [0.29,0.29,0.29,0.3]
        tire = Octoprime(ware)

        self.assertTrue(tire.needs_service())
    
    def test_middle_dosnt_work(self):
        ware = [0.29,0.29,0.3,0.29]
        tire = Octoprime(ware)

        self.assertTrue(tire.needs_service())

    def test_fist_very_dosnt_work(self):
        ware = [1,0.29,0.29,0.29]
        tire = Octoprime(ware)

        self.assertTrue(tire.needs_service())
        

if __name__ == '__main__':
    unittest.main()