# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите число: '))

factor = []
d = 2
while d * d <= number:
    if number % d == 0:
        factor.append(d)
        number  = number // d
    else:
        d += 1
if number > 1:
    factor.append(number)
print(factor)