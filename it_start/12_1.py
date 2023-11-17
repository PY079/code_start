list_participants = []

count = int(input('Сколько будет участников: '))
''' нижнее подчеркивание в for in range тоже переменная, 
но для удобства можно ставить этот символ,
тк не будем использовать эту переменную'''

for _ in range(count):
    participants = input('\n\nДобавить участника: ')
    list_participants.append(participants)

if len(list_participants)>3:
    for group in range(1,3):
        print(f'Количество частников в {group} группе - {len(list_participants)//2} ')
else:
    print('Невозвожно разделить на 2 группы')



