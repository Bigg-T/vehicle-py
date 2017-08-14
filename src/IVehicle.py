from abc import ABC, abstractmethod
from enum import Enum, unique

@unique
class VEHICLE_TYPE(Enum):
    CAR = 'car'
    TRUCK = 'truck'

class IVehicle(ABC):

    @abstractmethod
    def get_wheels(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def max_speed(self):
        pass

    @abstractmethod #'''Return True if self vehicle is faster than given vehicle.'''
    def is_faster(self, vehicle):
        pass
