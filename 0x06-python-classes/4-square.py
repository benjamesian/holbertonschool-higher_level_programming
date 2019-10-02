#!/usr/bin/python3
"""Square with validated size and area
"""


class Square:
    """Square class
    """
    def __init__(self, size=0):
        """Initialize a Square with a size
        """
        self.size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
