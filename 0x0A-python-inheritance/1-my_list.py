#!/usr/bin/python3
class MyList(list):
    """ Class that inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
