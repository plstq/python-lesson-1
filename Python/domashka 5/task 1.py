# Создайте программу для игры с конфетами человек против человека.
# Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

import random
name1 = input("Введите имя первого игрока: ")
name2 = input("Введите имя второго игрока: ")

igrok = random.randrange(1,3)
a = int(input("Введите количество конфет: "))
if igrok == 1:
    print("Первый ход делает: ", name1)
else:
    print("Первый ход делает: ", name2)

while a > 0:
    if a > 28:
        igrok1 = int(input("Ты можешь взять не больше 28 конфет, сколько конфет ты взял? "))
        a = a - igrok1
        print("Конфет осталось", a)
        if a > 28:
            igrok2 = int(input("Ты можешь взять не больше 28 конфет, сколько конфет ты взял? "))
            a = a - igrok2
            print("Конфет осталось", a)
            if a <= 28:
                if igrok == 1:
                    print("Осталось ", a, "шт, их забирает", name1, "а значит победил", name1)
                else:
                    print("Осталось ", a, "шт, их забирает", name2, "а значит победил", name2)
        else:
            if igrok == 1:
                print("Осталось ", a, "шт, их забирает", name2, "а значит победил", name2)
            else:
                print("Осталось ", a, "шт, их забирает", name1, "а значит победил", name1)