# Заменить в 9 строке на ваше фио

import os, pymorphy2
path_file='\\'.join(os.path.abspath(__file__).split("\\")[:-1])

def write_file_name():
    with open(fr'{path_file}\file.txt','+w') as file:
        for _ in range(10_000):
            file.write('ВАШЕ ФИО\n')

def read_file():
    with open(fr'{path_file}\file.txt','r') as file:
        text=file.readlines()
        for fio in text:
            fio_split=fio.rstrip().split(' ')
            last_name=fio_split[0]
            name=fio_split[1]
            otch=fio_split[2]

            morph1 = pymorphy2.MorphAnalyzer().parse(last_name)[0].inflect({'gent'}).word
            morph2 = pymorphy2.MorphAnalyzer().parse(name)[0].inflect({'gent'}).word
            morph3 = pymorphy2.MorphAnalyzer().parse(otch)[0].inflect({'gent'}).word
            print(morph1.title(),morph2.title(),morph3.title())

