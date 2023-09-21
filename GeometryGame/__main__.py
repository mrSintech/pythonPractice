import random
from shapes import Point, Rectangle, RectangleDrawer

random_coord_range = (0, 100)


# -------------------------------------- Build random Rectangle
def build_random_point():
    x = random.randint(*random_coord_range)
    y = random.randint(*random_coord_range)
    return Point(x, y)


def build_points_pair():
    p1 = build_random_point()
    p2 = build_random_point()
    return p1, p2


def build_rectangle():
    p1, p2 = build_points_pair()
    try:
        return RectangleDrawer(upper_right=p1, lower_left=p2).draw()
    except ValueError:
        return False


def build_random_rectangle():
    rec = False
    while not rec:
        rec = build_rectangle()

    return rec


# --------------------------------------- Guess Game
def guess_point_in_rec(rec):
    print("Guess a point inside rectangle: ")
    user_point = Point(
        float(input("Guess X: ")),
        float(input("Guess Y: "))
    )
    return user_point.is_in_rectangle(rec)


def guess_rectangle_area(rec):
    user_area = float(input("Guess Area: "))
    if user_area == rec.area():
        return True
    else:
        return False


def main():
    while True:
        ingame_rectangle = build_random_rectangle()
        if guess_point_in_rec(ingame_rectangle):
            print("Hooray! you guessed right!")
            print("I see a smart Gamer! but can you guess the area of rectangle? B)")
            if guess_rectangle_area(ingame_rectangle):
                print("correct! you are a genius, My LORD!")
            else:
                print("ha ha! Wrong Answer, Maybe after all you aren't that smart :))")

        else:
            print("Oops! Wrong answer")

        print("try again...")
        print("----------------------------------")


if __name__ == '__main__':
    main()
