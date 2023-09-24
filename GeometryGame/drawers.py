import turtle
from shapes import Rectangle, Point


class Drawer:
    def __init__(self, canvas=None):
        self._canvas = canvas

    @property
    def canvas(self) -> turtle.Turtle:
        if not self._canvas:
            self._canvas = turtle.Turtle()

        return self._canvas

    def change_pen_position(self, x, y, movement="absolute"):
        canvas = self.canvas
        if movement == "relative":
            x = canvas.pos()[0] + x
            y = canvas.pos()[1] + y

        canvas.penup()
        canvas.goto(x, y)
        canvas.pendown()

    def draw_dot(self, position: Point):
        canvas = self.canvas
        self.change_pen_position(position.x, position.y)
        canvas.dot(5, 'black')

    def write(self, text, font=10, position=None, movement="absolute"):
        if position:
            self.change_pen_position(position.x, position.y, movement)

        canvas = self.canvas
        canvas.write(f'{text}', align="center", font=("Arial", font, "normal"))


class RectangleDrawer(Rectangle, Drawer):

    def __init__(self, lower_left, upper_right, canvas=None):
        Rectangle.__init__(self, lower_left, upper_right)
        Drawer.__init__(self, canvas)

        self._canvas = canvas

    def write_rectangle_coordinates(self):
        self.write(self.lower_left, position=Point(0, -20))
        self.draw_dot(Point(0, 0))

        self.write(self.upper_right, position=Point(self.width, self.height))
        self.draw_dot(Point(self.width, self.height))

    def draw_rectangle(self):
        """ draw rectangle """
        canvas = self.canvas
        # self.change_pen_position(self.lower_left.x, self.lower_left.y)
        canvas.forward(self.width)
        canvas.left(90)
        canvas.forward(self.height)
        canvas.left(90)
        canvas.forward(self.width)
        canvas.left(90)
        canvas.forward(self.height)

    def set_canvas(self, canvas):
        self._canvas = canvas

    def draw(self):
        self.draw_rectangle()
        self.write_rectangle_coordinates()
