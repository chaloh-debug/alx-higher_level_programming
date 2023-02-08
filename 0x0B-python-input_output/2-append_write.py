#!/usr/bin/python3
"""
module for appending text to file
"""


def append_write(filename="", text=""):
    """

    appends a string at the end of a text file  and returns chars added

    Args:
        filename: file name
        text: text to append

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
