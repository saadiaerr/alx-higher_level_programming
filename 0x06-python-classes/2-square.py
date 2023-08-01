#!/usr/bin/python3
"""
A class Square that definesjj a square by: (based on 1-square.py)
"""


class Square():
    """
    This is a class Squarsse
    """

    def __init__(self, size=0):
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
