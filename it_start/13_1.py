'''можно менять в этом словаре название фильмов, страну, жанр, рейтинг'''
film = {
    'films':[
        {'title':'Мистер робот',
         'country':[('США')],
         'genre':[('триллер'), ('драма'), ('криминал')],
         'rating':7.8},
         
         {'title':'Ходячие мертвецы: Дэрил Диксон',
         'country':[('США')],
         'genre':[('ужасы')],
         'rating':7.1},
         
         {'title':'Джон Уик',
         'country':[('США'),('Китай')],
         'genre':[('боевик'), ('триллер'), ('криминал')],
         'rating':7.0},

         {'title':'Пираты Карибского Моря: Проклятие Черной жемчужины',
         'country':[('США')],
         'genre':[('фентези'),('боевик'),('приключения')],
         'rating':8.4},

         {'title':'Доктор Стрэндж',
         'country':[('США')],
         'genre':[('фантастика'),('фентези'),('боевик'),('приключения')],
         'rating':7.4},
    ]
}

def filtr_c(data, coutr):
    for i2 in data['country']:
        if coutr in i2: return data.get('title')

def filtr_g(data, genr):
    for i2 in data['genre']:
        if genr in i2: return data.get('title')

def filtr_r(data, rat):
    for i2 in data['rating']:
        if rat in i2: return data.get('title')

repetition={'country':None,'genre':None,'rating':None}
def get_data():
    da = []
    for i in film['films']:
        for i2 in i['country']:
            if i2 not in da: 
                da.append(i2)

    repetition['country']=sorted([*da])
    da.clear()

    for i in film['films']:
        for i3 in i['genre']:
            if i3 not in da: da.append(i3)
    repetition['genre']=sorted([*da])
    da.clear()

    for i in film['films']:
        if i['rating'] not in da: da.append(i['rating'])
    repetition['rating']=sorted([*da])
    da.clear()



d = get_data()
print('Доступные критерии по 1. странам')
print('Доступные критерии по 2. жанру')
print('Доступные критерии по 3. рейтингу')

nu = int(input('Введите номер критерия: '))
if nu == 1: 
    print('Страны:',', '.join(list(repetition['country'])),'\n')
    ch = input('Введите страну: ')
    if ch.capitalize() in repetition['country']:
        for i3 in film['films']:
            de = filtr_c(i3,ch.capitalize())
            if de: print(f'Нашлись фильмы: {de}')
    else: print('Такой страны нет')

elif nu == 2: 
    print('Жанры:',', '.join(list(repetition['genre'])),'\n')
    ch = input('Введите жанр: ')
    if ch.lower() in repetition['genre']:
        for i3 in film['films']:
            de = filtr_g(i3,ch.lower())
            if de: print(f'По жанру {ch.lower()} фильм - {de}')
    else: print('Такого жанра нет')


elif nu == 3: 
    print('Рейтинг:',', '.join(str(x) for x in repetition['rating']),'\n')
    print(f"1. Найти фильм с наименьшим рейтингом")
    print(f"2. Найти фильм наибольшим рейтингом")
    ch = int(input('Введите номер: '))
    if ch == 1:
        m_r = float(min(str(x) for x in repetition['rating']))
        for i3 in repetition['rating']:
            if i3 == m_r:
                for i4 in film['films']:
                    if i4['rating'] == m_r: print(i4['title'])
    
    elif ch == 2:
        m_r = float(max(str(x) for x in repetition['rating']))
        for i3 in repetition['rating']:
            if i3 == m_r:
                for i4 in film['films']:
                    if i4['rating'] == m_r: print(i4['title'])
    
