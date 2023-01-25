import unittest
from car import Car
from parts.part import Part

class BrokenPart(Part):
    def __init__(self):
        super.__init__(self)
    
    def needs_service(self):
        return True

class WorkingPart(Part):
    def __init__(self):
        super.__init__(self)
    
    def needs_service(self):
        return False

class TestCar(unittest.TestCase):
    def test_no_parts(self):
        car = Car([])
        self.assertFalse(car.needs_service())

    def test_one_working_part(self):
        car = Car([WorkingPart()])
        self.assertFalse(car.needs_service())
    
    def test_many_working_parts(self):
        parts = []
        for i in range(20):
            parts.append(WorkingPart())

        car = Car(parts)
        self.assertFalse(car.needs_service())
    
    def test_one_broken_part(self):
        car = Car([BrokenPart()])
        self.assertTrue(car.needs_service())
    
    def test_many_broken_parts(self):
        parts = []
        for i in range(20):
            parts.append(BrokenPart())

        car = Car(parts)
        self.assertTrue(car.needs_service())
    
    def test_many_broken_parts_first_working(self):
        parts = []
        for i in range(20):
            parts.append(BrokenPart())
        parts[0] = WorkingPart()

        car = Car(parts)
        self.assertTrue(car.needs_service())

    def test_many_broken_parts_last_working(self):
        parts = []
        for i in range(20):
            parts.append(BrokenPart())
        parts[19] = WorkingPart()

        car = Car(parts)
        self.assertTrue(car.needs_service())
    
    def test_many_broken_parts_middle_working(self):
        parts = []
        for i in range(20):
            parts.append(BrokenPart())
        parts[10] = WorkingPart()

        car = Car(parts)
        self.assertTrue(car.needs_service())
    
    def test_many_working_parts_first_broken(self):
        parts = []
        for i in range(20):
            parts.append(WorkingPart())
        parts[0] = BrokenPart()

        car = Car(parts)
        self.assertTrue(car.needs_service())

    def test_many_broken_parts_last_working(self):
        parts = []
        for i in range(20):
            parts.append(WorkingPart())
        parts[19] = BrokenPart()

        car = Car(parts)
        self.assertTrue(car.needs_service())
    
    def test_many_broken_parts_middle_working(self):
        parts = []
        for i in range(20):
            parts.append(WorkingPart())
        parts[10] = BrokenPart()

        car = Car(parts)
        self.assertTrue(car.needs_service())


if __name__ == '__main__':
    unittest.main()