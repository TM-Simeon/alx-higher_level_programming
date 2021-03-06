#!/usr/bin/python3
"""Rectangle module to define a rectangle"""


class Rectangle:
    """Rectangle class: defines a rectangle"""
    def __init__(self, width=0, height=0):
        """instance attributes:
        Args:
            height: height of rectangle
            width: width of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Args:
            value: the value for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            value: the value for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
