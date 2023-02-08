#!/usr/bin/python3
"""module to read from text file"""


def read_file(filename=""):
    """
    reads from file and prints to stdout
    Args:
        filemname:file name
    """


    with open(filename, 'r', encoding="utf-8") as f:
        f_read = f.read()
        print(f_read, end='')
