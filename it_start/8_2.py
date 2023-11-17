import turtle, sys
from random import randint, choice
from os import system

# Цвета можно взять любые с сайта https://barzunov.ru/python/turtle/color/colors-list/ 

list_color=['WhiteSmoke','Gainsboro','Silver','Black','SlateGray',
            'CornflowerBlue','RoyalBlue','Blue','MediumBlue','Navy',
            'DarkBlue','MidnightBlue','Cyan','PaleTurquoise','DarkTurquoise',
            'Turquoise','LightSeaGreen']

def circle(x:int, y:int, radius:float, color:str):
    obj.color(color)
    obj.penup(); obj.goto(x,y); obj.pendown()
    obj.circle(radius)
    


system('cls')
obj = turtle.Turtle()
obj.speed(100)


for count in range(1,101):
    rand_x, rand_y = randint(-400, 400), randint(-400, 400)
    rand_rad, rand_color = randint(5, 30), choice(list_color)
    circle(rand_x, rand_y, rand_rad, rand_color)
    sys.stdout.write(f'Выполенено: {count} из 100\r')
    if count == 100:
        system('cls')
        print('Завершено')
    
turtle.done()
