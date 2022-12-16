# from random import randint
# numbers = []
# for i in range(5):
#     numbers.append(randint(-10, 10))
# print(numbers)

# sum = 0

# for i in range (1, len(numbers), 2):
#     if i % 2 == 1:
#         sum += numbers[i]
# print(f"{numbers} - сумма элементов на нечетных позициях равна: {sum}")

from random import randint
numbers = []
for i in range(5):
    numbers.append(randint(-10, 10))

sum = 0

list = [i for i in range (1, len(numbers), 2) if i % 2 == 1]
    # if i % 2 == 1:
sum += numbers[i] #я не знаю как вставить в 21 строку это действие, поэтому он у меня не складывает
print(f"{numbers} - сумма элементов на нечетных позициях равна: {sum}")