import unittest
import sys
sys.path.insert(0, '../src')

from IVehicle import IVehicle, VEHICLE_TYPE
from Car import Car
from Truck import Truck

class TestTruck(unittest.TestCase):
    truck = Truck(55)
    truck2 = Truck(70)

    def test_max_speed(self):
        self.assertEqual(self.truck.max_speed(), 55)
        self.assertNotEqual(self.truck.max_speed(), 50)

    def test_max_speed2(self):
        self.assertEqual(self.truck2.max_speed(), 70)

    def test_type(self):
        self.assertEqual(self.truck.get_type(), VEHICLE_TYPE.TRUCK)

    def test_type2(self):
        self.assertNotEqual(self.truck.get_type(), VEHICLE_TYPE.CAR)

    def test_wheels(self):
        self.assertEqual(self.truck.get_wheels(), 8)

    def test_wheels2(self):
        self.assertNotEqual(self.truck.get_wheels(), 4)

    def test_is_faster(self):
        self.assertFalse(self.truck.is_faster(self.truck2))

    def test_is_faster2(self):
        temp = Car(40)
        self.assertTrue(self.truck2.is_faster(temp))

    def test_is_faster3(self):
        self.assertFalse(self.truck.is_faster(self.truck))

    def test_is_faster4(self):
        temp = Truck(40)
        self.assertTrue(self.truck2.is_faster(temp))

if __name__ == '__main__':
    unittest.main()
