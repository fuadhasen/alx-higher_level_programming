#!/usr/bin/python3
""" python script to find peak form list of integer"""


def find_peak(list_of_integers):
    """ function to find the peak
        from the list of integers
    """
    for i in range(len(list_of_integers) - 1):
        if i == 0:
            continue
        if list_of_integers[i] > list_of_integers[i + 1] and\
           list_of_integers[i] > list_of_integers[i - 1]:
            return list_of_integers[i]
    if len(list_of_integers) > 0:
        return list_of_integers[0]
