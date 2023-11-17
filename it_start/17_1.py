# можно генерировать любые числа, но не меня число в for
from random import randint
arr = [randint(1,500) for _ in range(100)]
a = int(input('Введите число от 1 до 500: '))
print([number for number in arr if number<a])