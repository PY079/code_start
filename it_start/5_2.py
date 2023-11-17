import math
# .3f - 3 знака после запятой, .5f - 5 знаков после запятой и тд

print('Введите коэффициенты дискриминанта:\nax^2 + bx + c = 0')

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
 
discr = b ** 2 - 4 * a * c
print(f'D = {discr:.3f}')
 
if discr > 0:
    print(f'x1 = {(-b + math.sqrt(discr)) / (2 * a):.3f}\n x2 = {(-b - math.sqrt(discr)) / (2 * a):.3f}')
elif discr == 0:
    print(f'x = {-b / (2 * a):.3f}')
else:
    print('Корней нет')