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
        return self.size

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
