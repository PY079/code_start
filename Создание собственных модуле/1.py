import turtle
from random import randint

class Shape:
    def draw(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def draw(self):
        x=randint(-300,300)
        y=randint(-300,300)
        turtle.penup();turtle.goto(x,y);turtle.pendown()
        for _ in range(4):
            turtle.forward(self.side_length)
            turtle.left(90)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        x=randint(-300,300)
        y=randint(-300,300)
        turtle.penup();turtle.goto(x,y);turtle.pendown()
        turtle.circle(self.radius)


def draw_shapes(shapes:list, speed:int):
    turtle.speed(speed)
    for shape in shapes:
        shape.draw()
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()


square = Square(100)
circle = Circle(50)

draw_shapes([square, circle],10)

turtle.done()
