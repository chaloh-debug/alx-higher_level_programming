#!/usr/bin/python3

class BaseGeometry:
    """ Empty class"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates type and size of value
        Args:
            name: str
            value: value to validate
        """
        
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
