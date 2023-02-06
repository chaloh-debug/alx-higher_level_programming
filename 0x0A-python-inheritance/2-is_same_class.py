#!/usr/bin/python3

def is_same_class(obj, a_class):
    """ unction that returns True if the object is exactly
    an instance of the specified class ; otherwise False.

    Args:
        obj: object
        a_class: class

    Return:
        True: if obj type is exactly as a_class
        False: otherwise
    """
    return type(obj) is a_class
