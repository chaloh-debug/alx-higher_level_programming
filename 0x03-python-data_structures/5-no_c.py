#!/usr/bin/python3
def no_c(my_string):
    size = len(my_string)

    i = 0

    new_string = my_string

    for j in range(size):
        if (my_string[j] == 'c' or my_string[j] == 'C'):
            new_string = new_string[:(j - i)] + my_string[(j + 1):]
            i += 1

    return (new_string)
