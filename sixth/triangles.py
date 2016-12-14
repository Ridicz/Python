from points import Point
from math import sqrt


class Triangle:
    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        if not ((isinstance(x1, float) or isinstance(x1, int)) and (isinstance(y1, float) or isinstance(y1, int))
                and (isinstance(x2, float) or isinstance(x2, int)) and (isinstance(y2, float) or isinstance(y2, int))
                and (isinstance(x3, float) or isinstance(x3, int)) and (isinstance(y3, float) or isinstance(y3, int))):
            raise ValueError("Invalid input argument type!")

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
        if not isinstance(other, Triangle):
            raise ValueError("Invalid input argument type!")

        return self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y \
            and self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y \
            and self.pt3.x == other.pt3.x and self.pt3.y == other.pt3.y

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
        if not (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
            raise ValueError("Invalid input argument type!")

        self.pt1.x += x
        self.pt2.x += x
        self.pt3.x += x
        self.pt1.y += y
        self.pt2.y += y
        self.pt3.y += y

        return self

    def make4(self):
        triangle1 = Triangle(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, (self.pt3.x + self.pt1.x) / 2,
                             (self.pt3.y + self.pt1.y) / 2)

        triangle2 = Triangle(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, (self.pt2.x + self.pt1.x) / 2,
                             (self.pt2.y + self.pt1.y) / 2)

        triangle3 = Triangle(self.pt1.x, self.pt1.y, self.pt3.x, self.pt3.y, (self.pt3.x + self.pt2.x) / 2,
                             (self.pt3.y + self.pt2.y) / 2)

        triangle4 = Triangle(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, (self.pt2.x + self.pt1.x) / 2,
                             (self.pt2.y + self.pt1.y) / 2)

        return [triangle1, triangle2, triangle3, triangle4]
