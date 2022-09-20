import math
from abc import ABC, abstractmethod

# Abstraction: Abstract Superclass
class Shape(ABC):
    # Dunder method with Arguments/Parameters
    def __init__(self, width, height):
        # Self
        # Attributes
        self.width = width
        self.height = height

    # Interface
    @abstractmethod
    # Self
    def area(self, width, height):
        pass

    # Static variable
    pi = math.pi

# Inheritance : Subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.area(width, height)

    # Operator overloading
    def area(self, width, height):
        self.area = width * height

# Inheritance : Subclass
class Triangle(Shape):
    # Dunder method with Arguments
    def __init__(self, width, height):
        super().__init__(width, height)
        self.area(width, height)

    # Operator overloading
    def area(self, width, height):
        self.area = 0.5 * self.width * self.width * Shape.pi
