# пожете изменить название переменных

import turtle, os
def box():
    obj=turtle.Turtle()
    obj.speed(5)
    for _ in range(4):
        obj.forward(90)
        obj.left(90)
    turtle.done()


def get_data():
    fio,email,phone_number=input('Введите ФИО: '), input('Введите почту: '), input('Введите номер телефона: ')
    os.system('cls')
    return f'Ваши данные\n\nФИО: {fio}; Почта: {email}; Номер телефона: {phone_number}'

