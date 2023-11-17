import turtle, os

''' Цвета можно взять любые с сайта https://barzunov.ru/python/turtle/color/colors-list/ 
можно изментять координаты перемещения и размер фигуры'''

list_color = ['black', 'white', 'gray', 'blue', 'cyan', 'red']
choice_color = []


def color():
    return 'white\nblack\ngray\nblue\ncyan\nred'


def menu():
    question_l()
    obj = turtle.Turtle()
    box(obj)
    circle(obj)
    triangle(obj)


def question_l():
    os.system('cls') # очистить териманл от текста
    print('Введите цвет линий ')
    print(color())
    choice = input('Выберите вариант цвета:  ')
    choice_color.append(choice) # записывается в список выбранный цвет




def box(obj):
    obj.penup();obj.goto(400, 100);obj.pendown()
    obj.color(choice_color[0]) # цвет линии выбирается из списка

    for _ in range(4):
        obj.forward(50)
        obj.left(90)




def circle(obj):
    obj.penup();obj.goto(200, 100);obj.pendown()

    obj.color(choice_color[0])
    obj.circle(150)




def triangle(obj):
    obj.penup(); obj.goto(-100, 100); obj.pendown()
    obj.color(choice_color[0])

    for _ in range(3):
        obj.forward(100)
        obj.left(120)




# выполенние кода, если он запущен напрямую, а не импортирован в другой файл но можно убрать проверку
if __name__ == '__main__':
    os.system('cls')
    menu()
    turtle.done()