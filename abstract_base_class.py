

# abstractbase class.................................................
from abc import ABCMeta,abstractmethod
# from abc import ABC,abstractmethod   3.4 version or upto 3.4 version of python

class shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle:
    type= "Rectangle"
    sides= 4
    def __init__(self):
        self.length=6
        self.breadth=7

    def printarea(self):
        return self.length * self.breadth

rect1=Rectangle()
print(rect1.printarea())

# tryobje=shape()     can not create objects

