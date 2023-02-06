#!/usr/bin/python3

""" code to list methods and attributes
of a an object """

def lookup(obj):
    """ function that returns the list of available
    attributes and methods of an object

    Args: obj
    instance of a class

    Return: list of methods and attributes
    """
    return dir(obj)
