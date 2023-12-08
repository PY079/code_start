from random import randint

def random_number() -> list:
    return [randint(-100,100) for _ in range(100)]

def rand_numb_yeild()-> list:
    yield [randint(-100,100) for _ in range(100)]

print(random_number())

print(next(rand_numb_yeild()))



