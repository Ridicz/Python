from points import Point
from math import pi


class Circle:

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("Radius negative!")

        if not ((isinstance(x, float) or isinstance(x, int)) and (isinstance(y, float) or isinstance(y, int))) \
                and (isinstance(radius, float) or isinstance(radius, int)):
            raise ValueError("Invalid input argument type!")

        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return "Circle(" + str(self.pt.x) + ", " + str(self.pt.y) + ", " + str(self.radius) + ")"

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Invalid input argument type!")

        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return pi * self.radius * self.radius

    def move(self, x, y):
        if not (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
            raise ValueError("Invalid input argument type!")

        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Invalid input argument type!")

        radius = max((self.radius + other.radius + (other.pt - self.pt).length()) / 2, self.radius, other.radius)
        temp = (radius - self.radius) / (2 * radius - self.radius - other.radius)
        circle_x = self.pt.x + temp * (other.pt.x - self.pt.y)
        circle_y = self.pt.y + temp * (other.pt.y - self.pt.y)
        return Circle(circle_x, circle_y, radius)
