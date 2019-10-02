#!/usr/bin/python3
"""Square with validated size
"""


class Square:
    """Square class
    """
    def __init__(self, size=0):
        """Initialize a Square with a size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
