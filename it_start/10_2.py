def print_squares_and_powers_of_two(N):
    i = 1
    while i * i <= N:
        if i !=1:print(i * i, end=" ")
        i += 1
    print()
    
    power_of_two = 1
    while power_of_two <= N:
        if i !=1:print(power_of_two, end=" ")
        power_of_two *= 2

n = int(input("Введите число N: "))
print_squares_and_powers_of_two(n)