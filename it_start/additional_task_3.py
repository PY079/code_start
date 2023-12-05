# пожете изменить название команды и переменных
import turtle, os
obj=turtle.Turtle()


def input_movement(movement:str):
    movement_list=movement.lower().split(' ')
    if movement_list[0]==' ':exit()
    else:
        if movement_list[0]=='пр': obj.forward(int(movement_list[1]))
        elif movement_list[0]=='наз': obj.backward(int(movement_list[1]))
        elif movement_list[0]=='вл': obj.left(int(movement_list[1]))
        elif movement_list[0]=='вп': obj.right(int(movement_list[1]))
        else: exit()

while True:
    print('Команды: пр-прямо, наз-назад, вл-влево, вп-вправо, выход - press enter\nПример: вп 50\n\n')
    a=input('Введите: ')
    os.system('cls')
    input_movement(a)
