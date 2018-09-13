#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Demonstrating the has-a and is-a concepts with subclassing"""


import car


class CustomCar(car.Car):
    """Object that stores Car data."""

    def __init__(self, color=None, tires=None):
        """Constructor for the class CustomCar.

        Args:
            color (string): Color of the car.
            tires (mixed): Can be color of tires, the number of tires, or left
                as none.

        Attributes:
            color (string): Color of the car. Attribute inherited from car.Car.
            tires (mixed): Can simply be the passed argument or become a list if
                no argument is passed.
        """
        car.Car.__init__(self, color)
        self.tires = tires
        if self.tires == None:
            self.tires = []
            my_tires = CustomTire()
            my_wheels = CustomTire()
            my_rollers = CustomTire()
            mycarwheels = CustomTire()
            self.tires.extend([my_tires, my_wheels, my_rollers, mycarwheels])
        return


class CustomTire(car.Tire):
    """Object that stores Tire data.

    Attributes:
        __maximum_miles (int): Private variable that is specified at 500 miles.
    """

    __maximum_miles = 500
