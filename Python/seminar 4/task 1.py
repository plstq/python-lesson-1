# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел. 1 2 3 4 10 25 3 -> 25 1

list = input ("Введите набор чисел: ").split()
list = [int(i) for i in list]
print(max(list), ' ', min(list))
print(list)