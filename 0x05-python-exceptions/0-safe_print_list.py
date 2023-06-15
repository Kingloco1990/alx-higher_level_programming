#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num_printed = 0
        for i in range(x):
            print(my_list[i], end="")
            num_printed += 1
        print()

    except IndexError:
        print()
        pass

    return num_printed
