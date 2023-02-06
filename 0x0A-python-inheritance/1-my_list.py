#!/usr/bin/python3

class MyList(List):
    """ class that inherits from list parent class.
    Args: List
    parent class

    Return: sorted list
    """
    def print_sorted(self):
        """ method to print sorted list """
        ls_sort = self.copy()
        ls_sort.sort()
        print(ls_sort)
