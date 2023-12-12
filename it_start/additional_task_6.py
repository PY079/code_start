import turtle, os
path_file='\\'.join(os.path.abspath(__file__).split("\\")[:-1])

def box():
    obj=turtle.Turtle()
    obj.speed(5)
    obj.color('green')
    for _ in range(4):
        obj.forward(100)
        obj.left(90)

    turtle.getscreen().getcanvas().postscript(file=f'{path_file}\image.eps')
box()