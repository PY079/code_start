import turtle, os
obj=turtle.Turtle()


def input_movement(movement:str):
    movement_list=movement.lower().split(' ')
    if movement_list[0]==' ':exit()
    else:
        if movement_list[0]=='пр': obj.forward(int(movement_list[1]))
        elif movement_list[0]=='наз': obj.backward(int(movement_list[1]))
        elif movement_list[0]=='вл': obj.left(int(movement_list[1]))
        elif movement_list[0]=='РІРї': obj.right(int(movement_list[1]))
        else: exit()

while True:
    print('РљРѕРјР°РЅРґС‹: РїСЂ-РїСЂСЏРјРѕ, РЅР°Р·-РЅР°Р·Р°Рґ, РІР»-РІР»РµРІРѕ, РІРї-РІРїСЂР°РІРѕ, РІС‹С…РѕРґ - press enter\nРџСЂРёРјРµСЂ: РІРї 50\n\n')
    a=input('Р’РІРµРґРёС‚Рµ: ')
    os.system('cls')
    input_movement(a)
