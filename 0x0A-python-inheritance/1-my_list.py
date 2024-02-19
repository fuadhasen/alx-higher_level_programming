#!/usr/bin/python3
"""This Module Provide A function that print list
   in sorted order.
"""


class MyList(list):
    """Class that provide print_sorted function."""

    def print_sorted(self):
        """Function MyList print the list in sorted manner
           self point to list and copy and print.
        """

        ls = sorted(self)
        print(ls)
