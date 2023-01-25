import unittest
from car import Car
from parts.part import Part


from capulet import Capulet
from willoughby import Willoughby
from sternman import Sternman

class TestCapulet(unittest.TestCase):
    def test_just_serviced(self):
        engine = Capulet(0,0)
        self.assertFalse(engine.needs_service())
    
    def test_allmost_needs_service(self):
        engine = Capulet(0,30000)
        self.assertFalse(engine.needs_service())
    
    def test_just_needs_service(self):
        engine = Capulet(0,30000.001)
        self.assertFalse(engine.needs_service())
    
    def test_very_needs_service(self):
        engine = Capulet(0,3000000)
        self.assertFalse(engine.needs_service())

    def test_both_large_same(self):
        engine = Capulet(3000000,3000000)
        self.assertFalse(engine.needs_service())
    
    def test_both_large_allmost_need_service(self):
        engine = Capulet(3000000,3030000)
        self.assertFalse(engine.needs_service())
    
    def test_both_large_just_need_service(self):
        engine = Capulet(3000000,3030000.1)
        self.assertFalse(engine.needs_service())
    
    def test_both_large_needs_service(self):
        engine = Capulet(3000000,3090000)
        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_just_serviced(self):
        engine = Capulet(0,0)
        self.assertFalse(engine.needs_service())
    
    def test_allmost_needs_service(self):
        engine = Capulet(0,60000)
        self.assertFalse(engine.needs_service())
    
    def test_just_needs_service(self):
        engine = Capulet(0,60000.001)
        self.assertFalse(engine.needs_service())
    
    def test_very_needs_service(self):
        engine = Capulet(0,3000000)
        self.assertFalse(engine.needs_service())

    def test_both_large_same(self):
        engine = Capulet(3000000,3000000)
        self.assertFalse(engine.needs_service())
    
    def test_both_large_allmost_need_service(self):
        engine = Capulet(3000000,3060000)
        self.assertFalse(engine.needs_service())
    
    def test_both_large_just_need_service(self):
        engine = Capulet(3000000,3060000.1)
        self.assertFalse(engine.needs_service())
    
    def test_both_large_needs_service(self):
        engine = Capulet(3000000,3190000)
        self.assertFalse(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_light_on(self):
        engine = Sternman(True)
        self.assertTrue(engine.needs_service())
    
    def test_light_off(self):
        engine = Sternman(False)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()