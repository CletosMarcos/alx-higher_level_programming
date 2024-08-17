#!/usr/bin/python3
"""Defines a Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle

    __str__ method should return [Square] (<id>) <x>/<y> - <size>
        where size is width or height"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes

        *args is the list of arguments - no-keyworded arguments
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        **kwargs must be skipped if *args exists and is not empty"""
        if args:
            attr_list = ["id", "size", "x", "y"]
            for arg in range(len(args)):
                setattr(self, attr_list[arg], args[arg])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        "Returns a dictionary representation of a Square"
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
