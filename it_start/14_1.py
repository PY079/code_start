import turtle
''' можно менять название фигуры, но только потом нужно переписывать функции чтобы нарисовать эту фигуру
можно менять цвет линий (lines), цвет заливки (background) и координаты в coordinates
Цвета можно взять любые с сайта https://barzunov.ru/python/turtle/color/colors-list/ 
'''

data_dict = {
    'data': [
        {
            'name':'Квадрат',
            'lines':'Turquoise',
            'background':'SpringGreen',
            'coordinates':{'x':100, 'y':200}
        },
        {
            'name':'Прямоугольник',
            'lines':'cyan',
            'background':'PaleTurquoise',
            'coordinates':{'x':00, 'y':200}
        },
        {
            'name':'Треугольник',
            'lines':'black',
            'background':'WhiteSmoke',
            'coordinates':{'x':-100, 'y':200}
        },
        {
            'name':'Круг',
            'lines':'red',
            'background':'Linen',
            'coordinates':{'x':-150, 'y':200}
        },
        {
            'name':'Параллепипед',
            'lines':'Yellow',
            'background':'Gold',
            'coordinates':{'x':-350, 'y':200}
        }
    ]
}


def box(lines,background,x,y):
    obj.penup(); obj.goto(x,y); obj.color(lines, background); obj.pendown()
    obj.begin_fill()
    for _ in range(4):
        obj.forward(90)
        obj.left(90)
    obj.end_fill()


def cirle(lines,background, x, y):
    obj.penup(); obj.goto(x,y); obj.color(lines,background); obj.pendown()
    obj.begin_fill()
    obj.circle(50)
    obj.end_fill()

def prm(lines,background, x,y):
    obj.penup(); obj.goto(x,y); obj.color(lines,background); obj.pendown()
    obj.begin_fill()
    for _ in range(2):
        obj.forward(90)
        obj.left(90)
        obj.forward(120)
        obj.left(90)
    obj.end_fill()


def tre(lines,background, x,y):
    obj.penup(); obj.goto(x,y); obj.color(lines,background); obj.pendown()
    obj.begin_fill()
    for _ in range(3):
        obj.forward(90)
        obj.left(120)
    obj.end_fill()


def parl(lines, background,x,y):
    obj.penup(); obj.goto(x,y); obj.color(lines,background); obj.pendown()
    obj.begin_fill()
    for _ in range(2):
        obj.forward(90)
        obj.left(60)
        obj.forward(90)
        obj.left(120)
    obj.end_fill()


obj = turtle.Turtle()
obj.pensize(2)
obj.speed(10)
for i in data_dict['data']:
    figure = i.get('name')
    lines, background = i.get('lines'), i.get('background')
    coord = i.get('coordinates')
    x = coord.get('x'); y = coord.get('y')

    if figure == 'Квадрат':
        box(lines,background,x,y)
    elif figure == 'Прямоугольник':
        prm(lines,background,x,y)
    elif figure == 'Треугольник':
        tre(lines,background,x,y)
    elif figure == 'Круг':
        cirle(lines,background,x,y)
    elif figure == 'Параллепипед':
        parl(lines, background,x,y)
turtle.done()