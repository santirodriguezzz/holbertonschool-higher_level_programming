#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0
    for i in range(0, x):
        try:
            print(f"{my_list[i]}", end="")
            element += 1
        except:
            pass
    print()
    return element
