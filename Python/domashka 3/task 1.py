# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
numbers = []
for i in range(5):
    numbers.append(randint(-10, 10))
print(numbers)

sum = 0

for i in range (1, len(numbers), 2):
    if i % 2 == 1:
        sum += numbers[i]
print(f"{numbers} - сумма элементов на нечетных позициях равна: {sum}")
