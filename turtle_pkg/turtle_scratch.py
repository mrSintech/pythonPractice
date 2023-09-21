# turtle is a built-in library to generate simple graphics by giving positions and distances and directions.
import turtle

myturtle = turtle.Turtle()  # turtle screen

myturtle.penup()  # don't draw line
myturtle.goto(200, 100)  # Go to a certain coordinates

myturtle.pendown()
myturtle.dot(10, 'black')  # draw a dot.

turtle.numinput(title="turle numinput", prompt="input x")  # user value input

myturtle.penup()

myturtle.goto(-200, -100)

myturtle.pendown()  # Draw line
myturtle.forward(100)  # move in Pixels
myturtle.left(90) # Angle
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()
