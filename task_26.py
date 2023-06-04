def powering(a, b):
    if b == 0:
        return 1
    else:
        return powering(a, b - 1) * a


x = int(input("Введите число: "))
y = int(input("В какую степень возвести: "))
print(f'{x} в степени {y} равен {powering(x, y)}')