from IVehicle import IVehicle, VEHICLE_TYPE


class Truck(IVehicle):

    def __init__(self, speed):
        self.speed = speed

    def get_wheels(self):
        return 8

    def get_type(self):
        return VEHICLE_TYPE.TRUCK

    def max_speed(self):
        return self.speed

    def is_faster(self, vehicle):
        return self.max_speed() > vehicle.max_speed()
