#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ret = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            ret += 1
        except Exception as e:
            break
    print()
    return ret
