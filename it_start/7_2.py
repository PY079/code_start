import turtle

obj1 = turtle.Turtle()
obj2 = turtle.Turtle()
'''
да, у меня 2 стрелочки, но можно использоавть одну
можно изменять координаты

'''

def rectangle():
    obj1.speed(5); obj2.speed(5) # скорость 
    obj1.penup(); obj2.penup()
    obj1.back(400); obj2.back(100)
    obj1.pendown(); obj2.pendown()
    
    for _ in range(2):
        obj1.forward(200)
        obj1.left(90)
        obj1.forward(50)
        obj1.left(90)
    
    for _ in range(2):
        obj2.forward(200)
        obj2.left(90)
        obj2.forward(50)
        obj2.left(90)
    turtle.done()


# выполенние кода, если он запущен напрямую, а не импортирован в другой файл но можно убрать проверку
if __name__ == '__main__':
    rectangle()

