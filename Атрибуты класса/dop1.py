from random import choice

class Person:
    def __init__(self, name:str, age:int ,job=None):
        self._name=name
        self._age=age        
        self._job= job if job else 'РЅРµ СЂР°Р±РѕС‚Р°СЋ'

    @property
    def get_name_age_job(self):
        return f'Привет!\nМеня зовут {self._name}, мне {self._age}. Моя работа: {self._job}\n\n'
    
    @property
    def get_favorite_color(self):
        return f"Меня зовут {self._name} и мой любимый цвет - это {choice(['красный','зеленый','белый','серый','голубой'])}"


people1=Person('Игорь',20,'dev')
people2=Person('Алина',15)
print(people1.get_name_age_job, people1.get_favorite_color)
print(people2.get_name_age_job, people2.get_favorite_color)
