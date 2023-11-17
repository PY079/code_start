import math, turtle
# xcor() и ycor() выдают координаты по x и y как дробные числа

obj = turtle.Turtle()
a, b = 250, 100
coordinates_x, coordinates_y = obj.xcor(), obj.ycor()


for degree in range(361):
    radius = math.radians(degree)
    x = a * math.sin(radius) + coordinates_x
    y = -b * math.cos(radius) + b + coordinates_y
    obj.goto(x, y)
turtle.done()