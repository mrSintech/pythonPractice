import math
import turtle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_in_rectangle(self, rectangle):
        if not isinstance(rectangle, Rectangle):
            raise TypeError("rectangle must be instances of Rectangle.")

        if (rectangle.lower_left.x <= self.x <= rectangle.upper_right.x) \
                and (rectangle.lower_left.y <= self.y <= rectangle.upper_right.y):
            return True
        else:
            return False

    def __sub__(self, other):
        if not (isinstance(other, Point)):
            raise TypeError("other must be instance of Point.")

        sub = (self.x - other.x, self.y - other.y)
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

    def __str__(self):
        return f"Rectangle is defined; Lower Left is {self.lower_left} and Upper Right is {self.upper_right}"

    def draw(self):
        ...

    def draw_rectangle(self):
        ...


class RectangleDrawer(Rectangle):

    def __init__(self, lower_left, upper_right, scale=4):
        Rectangle.__init__(self, lower_left, upper_right)

        self.scale = scale
        self._myturtle = None
        self._user_point = None

    @property
    def my_turtle(self) -> turtle.Turtle:
        if not self._myturtle:
            self._myturtle = turtle.Turtle()
            screen = turtle.Screen()
            screen.setup(500, 600)

        return self._myturtle

    @property
    def user_point(self):
        x = turtle.numinput('point in rec', 'Guess X:')
        y = turtle.numinput('point in rec', 'Guess Y:')
        self._user_point = Point(x, y)
        return self._user_point

    def change_pen_position(self, x, y, movement="absolute"):
        myturtle = self.my_turtle
        if movement == "relative":
            x = self.my_turtle.pos()[0] + x
            y = self.my_turtle.pos()[1] + y

        myturtle.penup()
        myturtle.goto(x, y)
        myturtle.pendown()

    def write(self, text, font=10, position=None, movement="absolute"):
        if position:
            self.change_pen_position(position.x, position.y, movement)

        myturtle = self.my_turtle
        myturtle.write(f'{text}', align="center", font=("Arial", font, "normal"))

    def write_rectangle_coordinates(self):
        myturtle = self.my_turtle
        self.write(self.lower_left, position=Point(self.lower_left.x - 10, self.lower_left.y - 30))
        self.draw_dot(self.lower_left)

        self.write(self.upper_right, position=Point(self.upper_right.x + 10, self.upper_right.y + 10))
        self.draw_dot(Point(self.upper_right.x, self.upper_right.y))

    def draw_dot(self, position):
        myturtle = self.my_turtle
        self.change_pen_position(position.x, position.y)
        myturtle.dot(5, 'black')

    def draw_rectangle(self):
        """ draw rectangle """
        myturtle = self.my_turtle
        self.change_pen_position(self.lower_left.x, self.lower_left.y)
        myturtle.forward(self.width)
        myturtle.left(90)
        myturtle.forward(self.height)
        myturtle.left(90)
        myturtle.forward(self.width)
        myturtle.left(90)
        myturtle.forward(self.height)

    def draw(self):
        self.draw_rectangle()
        self.write_rectangle_coordinates()
        self.draw_user_point()
        turtle.mainloop()

    def draw_user_point(self):
        myturtle = self.my_turtle
        user_point = self.user_point
        self.draw_dot(user_point)
        self.write("Your Point", movement="relative", position=Point(0,0))





