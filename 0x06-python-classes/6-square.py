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
    def position(self, position):
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(lambda x: isinstance(x, int) for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for _ in range(self.position[1]):
                print('')
            for _ in range(self.size):
                print("_" * self.position[0], end='')
                print("#" * self.size)
