import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        if not (isinstance(other, Point)):
            raise TypeError("other must be instance of Point.")

        sub = Point(self.x - other.x, self.y - other.y)
        return sub

    def __gt__(self, other):
        if not (isinstance(other, Point)):
            raise TypeError("other must be instance of Point.")

        if (self.x > other.x) and (self.y > other.y):
            return True
        else:
            return False

    def __lt__(self, other):
        if not (isinstance(other, Point)):
            raise TypeError("other must be instance of Point.")

        if (self.x < other.x) and (self.y < other.y):
            return True
        else:
            return False

    def distance_from(self, point):
        if not (isinstance(point, Point)):
            raise TypeError("point must be instance of Point.")

        x, y = point - self
        return math.hypot(x, y)

    def __repr__(self):
        return f"({self.x},{self.y})"


class Rectangle:
    def __init__(self, lower_left, upper_right):
        if not upper_right > lower_left:
            if lower_left > upper_right:
                lower_left, upper_right = upper_right, lower_left  # Swap points
            else:
                raise ValueError("one of the points should be greater than other point.")

        self.lower_left = lower_left
        self.upper_right = upper_right
        self.width = self.upper_right.x - self.lower_left.x
        self.height = self.upper_right.y - self.lower_left.y
        print(self)

    def area(self):
        return self.width * self.height

    def is_point_in_rectangle(self, point: Point):
        if not isinstance(point, Point):
            raise TypeError("point must be instances of Point.")

        if (self.lower_left.x <= point.x <= self.upper_right.x) \
                and (self.lower_left.y <= point.y <= self.upper_right.y):
            return True
        else:
            return False

    def __str__(self):
        return f"Rectangle is defined; Lower Left is {self.lower_left} and Upper Right is {self.upper_right}"
