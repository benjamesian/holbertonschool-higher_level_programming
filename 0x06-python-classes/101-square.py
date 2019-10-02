#!/usr/bin/python3
"""Square with validated size and area
"""


class Square:
    """Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with a size
        """
        self.size = size
        self.position = position

    def __str__(self):
        out = ''
        if self.size != 0:
            for _ in range(self.position[1]):
                out += '\n'
            for _ in range(self.size):
                out += " " * self.position[0] + "#" * self.size
        return out

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        if not isinstance(pos, tuple) or len(pos) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(pos[0], int) and isinstance(pos[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (pos[0] >= 0 and pos[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = pos

    def area(self):
        return self.__size ** 2

    def my_print(self):
        print(str(self))
