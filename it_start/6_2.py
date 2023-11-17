import turtle, os
from random import choice

'''
Цвета можно взять любые с сайта https://barzunov.ru/python/turtle/color/colors-list/ 

'''
list_color=['black','white','gray','blue','cyan','red']


def triangle(lines):
    while True:
        rand_color = choice(list_color)
        if rand_color != lines:
            break
        else:
            print(f'\nЦвет фона совпадает с цветом линий. Перевыбор\n\n')
    
    print(f'Цвет линий: {lines}, цвет фона: {rand_color}')
    
    obj.color(lines, rand_color) # цвет линий и цвет заливки
    obj.begin_fill() # начать заливку

    obj.forward(100)
    obj.back(200)
    obj.left(60)
    obj.forward(200)
    obj.right(120)
    obj.forward(200)
    
    obj.end_fill() # закончить заливку
    




   
        

    
    
# выполенние кода, если он запущен напрямую, а не импортирован в другой файл но можно убрать проверку
if __name__ == '__main__':
    os.system('cls')
    obj = turtle.Turtle()
    
    triangle(list_color[0])
    obj.penup()
    obj.goto(100, 20)
    obj.pendown()
    
    
    triangle(list_color[5])
    turtle.done()