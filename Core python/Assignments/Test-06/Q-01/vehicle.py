#Write a program which calculates toll calculation on some location following
# is data provided:
# Many vehicles goes through the toll every vehicle has to pay the basic
# toll + extra charges if any.
# two wheelers have to pay basic toll Rs 20 three wheelers have to pay
# 30 and four wheelers have to pay 40
# heavy veheicles i.e. Vehicles having wheels more than four, have to
# pay 60 Rs as basic toll
# extra charges :
# for two wheelers if no. of persons are more than two extra charge
# =10/person
# for three wheelers if no. of persons are more than 3 extra charge
# =20/person
# for four wheelers if no. of persons are more than 4 extra charge
# =40/person
# for heavy vehicle if no. of person are more than 6 extra charges
# =100/person.
# Show polymorphic behaviour in main. Main module should be
# designed in such way that toll should easily operate it through
# interactive menu driven program .
# Object of vehicle class should not be possible.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, persons):
        self.persons = persons

    @abstractmethod
    def calculate_toll(self):
        pass

class TwoWheeler(Vehicle):
    def calculate_toll(self):
        basic = 20
        extra = 0
        if self.persons > 2:
            extra = (self.persons - 2) * 10
        return basic + extra

class ThreeWheeler(Vehicle):
    def calculate_toll(self):
        basic = 30
        extra = 0
        if self.persons > 3:
            extra = (self.persons - 3) * 20
        return basic + extra

class FourWheeler(Vehicle):
    def calculate_toll(self):
        basic = 40
        extra = 0
        if self.persons > 4:
            extra = (self.persons - 4) * 40
        return basic + extra

class HeavyVehicle(Vehicle):
    def calculate_toll(self):
        basic = 60
        extra = 0
        if self.persons > 6:
            extra = (self.persons - 6) * 100
        return basic + extra