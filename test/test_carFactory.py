import unittest
import datetime
from car import Car
from parts.part import Part
from carFactory import CarFactory

from capulet import Capulet
from willoughby import Willoughby
from sternman import Sternman

from spindler import Spindler
from nubbit import Nubbin

today = datetime.today().date()



class TestCar(unittest.TestCase):
    def calliope_test(self):
        car = CarFactory.create_calliope(today,1000,1000)
        self.assertIsInstance(car.parts[0], Capulet)
        self.assertIsInstance(car.parts[1], Spindler)
    
    def glissade_test(self):
        car = CarFactory.create_glissade(today,1000,1000)
        self.assertIsInstance(car.parts[0], Willoughby)
        self.assertIsInstance(car.parts[1], Spindler)

    def palindrome_test(self):
        car = CarFactory.create_palindrome(today,False)
        self.assertIsInstance(car.parts[0], Sternman)
        self.assertIsInstance(car.parts[1], Spindler)
    
    def rorschach_test(self):
        car = CarFactory.create_rorschach(today,1000,1000)
        self.assertIsInstance(car.parts[0], Willoughby)
        self.assertIsInstance(car.parts[1], Nubbin)
    
    def thovex_test(self):
        car = CarFactory.create_thovex(today,1000,1000)
        self.assertIsInstance(car.parts[0], Capulet)
        self.assertIsInstance(car.parts[1], Nubbin)
                    

if __name__ == '__main__':
    unittest.main()