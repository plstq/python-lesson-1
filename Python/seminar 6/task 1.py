# Задача 1
# Вводятся названия городов в одну строчку через запятую. Необходимо определить функцию map,
# которая бы возвращала названия городов только длиной более 5 символов. Вместо остальных названий -
# строку с дефисом ("-").
# Сформировать список из полученных значений и отобразить его на экране в одну строчку через запятую.

# Ввод:
# Москва,Уфа,Вологда,Тула,Владивосток,Хабаровск
# Вывод:
# Москва,-,Вологда,-,Владивосток,Хабаровск

str1 = "Москва,Уфа,Вологда,Тула,Владивосток,Хабаровск"
str2 = ",".join(i if len(i) > 5 else "-" for i in str1.split(","))
print(str2)

# citys = 'Москва,Уфа,Вологда,Тула,Владивосток,Хабаровск'
# a = list(map((lambda x: x if len(x) > 5 else '-'), citys.split(',')))
# print(','.join(a))