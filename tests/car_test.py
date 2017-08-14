import unittest
import sys
sys.path.insert(0, '../src')

from IVehicle import IVehicle, VEHICLE_TYPE
from Car import Car
from Truck import Truck

class TestCar(unittest.TestCase):
    car = Car(50)
    car2 = Car(80)

    def test_max_speed(self):
        self.assertEqual(self.car.max_speed(), 50)
        self.assertNotEqual(self.car.max_speed(), 40)

    def test_max_speed2(self):
        self.assertEqual(self.car2.max_speed(), 80)

    def test_type(self):
        self.assertEqual(self.car.get_type(), VEHICLE_TYPE.CAR)

    def test_type2(self):
        self.assertNotEqual(self.car.get_type(), VEHICLE_TYPE.TRUCK)

    def test_wheels(self):
        self.assertEqual(self.car.get_wheels(), 4)

    def test_wheels2(self):
        self.assertNotEqual(self.car.get_wheels(), 8)

    def test_is_faster(self):
        self.assertFalse(self.car.is_faster(self.car2))

    def test_is_faster2(self):
        temp = Car(40)
        self.assertTrue(self.car.is_faster(temp))

    def test_is_faster3(self):
        self.assertFalse(self.car.is_faster(self.car))


if __name__ == '__main__':
    unittest.main()
