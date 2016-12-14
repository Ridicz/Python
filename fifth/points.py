from math import sqrt


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        output = "("
        output += str(self.x)
        output += ", "
        output += str(self.y)
        output += ")"
        return output

    def __repr__(self):
        output = "Point"
        output += str(self)
        return output

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return sqrt(self.x * self.x + self.y * self.y)
