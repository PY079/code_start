
class Person:
    def __init__(self, name:str, age:int ,job=None):
        self.name=name
        self.age=age        
        self.job= job if job else 'не работаю'

    @property
    def get_info(self):
        return f'Привет!\nМеня зовут {self.name}, мне {self.age}. Моя работа: {self.job}\n\n'


people1=Person('Игорь',20,'dev')
people2=Person('Алина',15)
print(people1.get_info)
print(people2.get_info)


