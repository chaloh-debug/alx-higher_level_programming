#!/usr/bin/python3
"""
module to write a string to a txt file
"""


def write_file(filename="", text=""):
    """

    writes string to txt file and no. of chars written

    Args:
        filename: file name
        text: string to write

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return  f.write(text)
