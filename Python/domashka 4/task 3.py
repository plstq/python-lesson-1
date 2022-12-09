# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
numbers = []
for i in range(5):
    numbers.append(randint(-10, 10))
print(numbers)

newlist = []
for i in numbers:
    if i not in newlist:
        newlist.append(i)
print(newlist)