#!/usr/bin/python3
"""
contains a function that prints text

"""

def text_indentation(text):
    """
    Function that prints 2 new lines after ".?:" characters

    Args:
        text: text to print

    Raises:
        TypeError: If text is not a string

    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    
    i = text[:]

    for j in ".?:":
        list_text = i.split(j)
        i = ""
        for k in list_text:
            k = k.strip(" ")
            i = k + j if i is "" else i + "\n\n" + k + j

    print(i[:-3], end="")
