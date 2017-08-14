from IVehicle import IVehicle, VEHICLE_TYPE

class Car(IVehicle):

    def __init__(self, speed):
        self.speed = speed

    def get_wheels(self):
        return 4

    def get_type(self):
        return VEHICLE_TYPE.CAR

    def max_speed(self):
        return self.speed

    def is_faster(self, vehicle):
        return self.max_speed() > vehicle.max_speed()
