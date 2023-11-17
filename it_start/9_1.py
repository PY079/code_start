import turtle

n = int(input('Введите начало: '))
m = int(input('Введите конец: '))
list_=[i * i for i in range(n, m+1)]
# list_ - тк переменная list используется языком

obj = turtle.Turtle()
obj.write(list_)
turtle.done()
