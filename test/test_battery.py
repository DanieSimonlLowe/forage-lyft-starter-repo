import unittest
import datetime
from car import Car
from parts.part import Part
from carFactory import CarFactory

from spindler import Spindler
from nubbit import Nubbint



class TestNubbit(unittest.TestCase):
    def just_seviced_test(self):
        battery = Nubbint(datetime.today().date())
        self.assertFalse(battery.needs_service())

    def allmost_needs_service_test(self):
        today = datetime.today().date()
        battery = Nubbint(today.replace(year=today.year - 4))
        self.assertFalse(battery.needs_service())

    def just_needs_service_test(self):
        today = datetime.today().date()
        battery = Nubbint(today.replace(year=today.year - 5))
        self.assertTrue(battery.needs_service())

    def very_needs_service_test(self):
        today = datetime.today().date()
        battery = Nubbint(today.replace(year=today.year - 10000))
        self.assertTrue(battery.needs_service())

class TestSpindler(unittest.TestCase):
    def just_seviced_test(self):
        battery = Spindler(datetime.today().date())
        self.assertFalse(battery.needs_service())

    def allmost_needs_service_test(self):
        today = datetime.today().date()
        battery = Spindler(today.replace(year=today.year - 2))
        self.assertFalse(battery.needs_service())

    def just_needs_service_test(self):
        today = datetime.today().date()
        battery = Spindler(today.replace(year=today.year - 3))
        self.assertTrue(battery.needs_service())

    def very_needs_service_test(self):
        today = datetime.today().date()
        battery = Spindler(today.replace(year=today.year - 10000))
        self.assertTrue(battery.needs_service())