#!/usr/bin/python3
""" custom list class """


class MyList(list):
    """ list with sorted print """
    def print_sorted(self):
        """ print the list with data sorted """
        print(sorted(self))
