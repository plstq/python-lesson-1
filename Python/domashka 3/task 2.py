# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
numbers = []
for i in range(4):
    numbers.append(randint(-10, 10))
print(str(numbers))

result = []
for i in range(0, (len(numbers) + 1) // 2): 
    result.append(numbers[i] * numbers[len(numbers) - i - 1])
print("Произведение пар чисел списка будет: " + str(result))

