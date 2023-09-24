import random
from shapes import Point
from drawers import Drawer, RectangleDrawer
import turtle

random_coord_range = (0, 500)


class GeometryGame(Drawer):
    # TODO: user point property
    def __init__(self):
        Drawer.__init__(self)

        self._rectangle = None
        self._user_point = None

    def start(self):
        # draw rectangle
        self.rectangle.set_canvas(self.canvas)
        self.rectangle.draw()

        # get point in rectangle
        self.get_user_point()
        self.draw_user_point()

        # validate user point in rectangle
        if self.rectangle.is_point_in_rectangle(self._user_point):
            self.correct_guess_point_in_rec()

        else:
            self.incorrect_guess_point_in_rec()

        turtle.done()

    def correct_guess_point_in_rec(self):
        self.write("CORRECT, BRAVO!", position=Point(0, -100), font=40)

    def incorrect_guess_point_in_rec(self):
        self.write("Oops! INCORRECT :(", position=Point(0, -100), font=40)

    @property
    def rectangle(self):
        if not self._rectangle:
            self._rectangle = self.random_rectangle

        return self._rectangle

    def get_user_point(self):
        """Get user guess point"""
        x = turtle.numinput('point in rec', 'Guess X:')
        y = turtle.numinput('point in rec', 'Guess Y:')
        # relate user point to 0,0 of rectangle lower point
        self._user_point = Point(x, y)

    def draw_user_point(self):
        user_point = self._user_point - self.rectangle.lower_left
        self.draw_dot(user_point)
        self.write("Your Point", movement="relative", position=Point(0, 0))

    @property
    def build_random_point(self):
        x = random.randint(*random_coord_range)
        y = random.randint(*random_coord_range)
        return Point(x, y)

    @property
    def build_rectangle(self):
        p1 = self.build_random_point
        p2 = self.build_random_point

        try:
            return RectangleDrawer(upper_right=p1, lower_left=p2)
        except ValueError:
            return False

    @property
    def random_rectangle(self):
        rec = False
        while not rec:
            rec = self.build_rectangle

        return rec


if __name__ == '__main__':
    GeometryGame().start()
