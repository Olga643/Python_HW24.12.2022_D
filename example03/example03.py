#Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import random
N = 20
a = [0] * N
for i in range(N):
    a[i] = int(random()*15)
    print(a[i], end=' ')
print()

my_list = []
for i in range(N):
    f = True
    for j in range(N):
        if a[i] == a[j] and i != j:
            f = False
            break
    if f == True:
       my_list.append(a[i])
       
print(my_list)

