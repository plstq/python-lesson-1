# Задача №4
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


# a = input()
# d = {'1' : 'x > 0 y > 0', '2' : 'x < 0 y > 0', '3' : ' x < 0 y < 0', '4' : 'x > 0 y < 0'}
# print(d[a])

a = int(input())
b = {'x > 0 y > 0', 'x < 0 y > 0', ' x < 0 y < 0', 'x > 0 y < 0'}
data = list(enumerate(b, 1))
print(data)
print(data[a-1])
