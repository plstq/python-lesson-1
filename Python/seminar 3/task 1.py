# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке некое число.
# Пример:
# ['114411', 'sjngsjgng', '123fsghs'] -> No
# ['12', 12] -> Yes

List = ['114411', 'sjngsjgng', 123]

j = 0
for i in range (len(List)):
    if type(List[i]) == int or type(List[i]) == float:
        print("Элемент ", i, "- число")
        j += 1
if j == 0:
        print("Среди элементов чисел нет")