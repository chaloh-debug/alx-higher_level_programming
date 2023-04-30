#!/usr/bin/python3
"""script to find peak val"""


def find_peak(list_of_integers):
    """sort and return peak val"""
    length = len(list_of_integers)
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[length - 1]
