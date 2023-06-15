#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for element in range(x):
            if isinstance(my_list[element], int):
                print("{:d}".format(my_list[element]), end="")
                count += 1
        print()
    except (NameError, TypeError):
        pass
    return count
