import turtle

def correct_password():
    screen = turtle.Screen()
    ''' изменить путь до файла .gif, не убирать r после = если в пути есть '\'
    
     использовать только .gif т.к поддерживает только такой тип файла '''
    image = r"C:\Users\12\Desktop\win.gif"
    screen.addshape(image)
    turtle.shape(image)
    turtle.done()

def pswrd():
    while True:
        pasword =input('Введите пароль: ')
        if pasword == '1t.start':
            correct_password()
            break
        else: print('Неверный пароль\n')


pswrd()