# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

n = [1, 5, 2, 3, 4, 6, 1, 7]
f = []
h = 0
for i in range(0, len(n)):
        if n[i] > h:
            h = n[i]
            f.append(h)
print(f)