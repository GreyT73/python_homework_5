def summ(a, b):
    if b == 0:
        return a
    else:
        return 1 + summ(a, b - 1)


x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
print(f'{x} + {y} = {summ(x, y)}')