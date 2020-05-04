from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def draw(this):
        pass
    @abstractmethod
    def area(this):
        pass

class Circle(Shape):
    def __init__(this,rad):
        this.radius=rad
    def draw(this):
        print("Draw a circle")
    def area(this):
        return math.pi * this.radius * this.radius

class Rectangle(Shape):
    def __init__(this,len,bre):
        this.length = len
        this.breadth = bre
    def draw(this):
        print("Draw a rectangle")
    def area(this):
        return this.length * this.breadth

shape = Circle(10)
shape.draw()
print("Area of circle is " ,shape.area())

shape2 = Rectangle(10,10)
shape2.draw()
print("Area of rectangle is " ,shape2.area())
