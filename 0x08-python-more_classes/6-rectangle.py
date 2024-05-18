#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Defines a rectangle with width and height"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        number_of_instances += 1 #  increments each time an instance is created
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """Return the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """Prints the rectangle with the character #"""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                print("#" * self.width, end='')
                if i != self.height - 1:
                    print()

        return ""

    def __repr__(self):
        return f"Rectangle({self.width}, {self.heigh})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        number_of_instances -= 1 #  decrement each time an instance is deleted
        print("Bye rectangle...")
