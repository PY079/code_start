import turtle

obj = turtle.Turtle()

''' нижнее подчеркивание в for in range тоже переменная, 
но для удобства можно ставить этот символ,
тк не будем использовать эту переменную'''

def box():
    for _ in range(4):
        obj.color('red')
        obj.forward(200)
        obj.left(90)
    turtle.done()

box()