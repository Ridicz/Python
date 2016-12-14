from points import Point
from math import sqrt


class Triangle:
    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):
        output = "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), ("
        output += str(self.pt2.x) + ", " + str(self.pt2.y) + "), ("
        output += str(self.pt3.x) + ", " + str(self.pt3.y) + ")]"
        return output

    def __repr__(self):
        output = "Triangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", "
        output += str(self.pt2.x) + ", " + str(self.pt2.y) + ", "
        output += str(self.pt3.x) + ", " + str(self.pt3.y) + ")"
        return output

    def __eq__(self, other):
        return self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y and \
               self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y and \
               self.pt3.x == other.pt3.x and self.pt3.y == other.pt3.y

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    def area(self):
        a = sqrt((self.pt2.x - self.pt1.x) * (self.pt2.x - self.pt1.x) +
                 (self.pt2.y - self.pt1.y) * (self.pt2.y - self.pt1.y))

        b = sqrt((self.pt3.x - self.pt1.x) * (self.pt3.x - self.pt1.x) +
                 (self.pt3.y - self.pt1.y) * (self.pt3.y - self.pt1.y))

        c = sqrt((self.pt3.x - self.pt2.x) * (self.pt3.x - self.pt2.x) +
                 (self.pt3.y - self.pt2.y) * (self.pt3.y - self.pt2.y))

        return sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4.

    def move(self, x, y):
        self.pt1.x += x
        self.pt2.x += x
        self.pt3.x += x
        self.pt1.y += y
        self.pt2.y += y
        self.pt3.y += y

        return self
