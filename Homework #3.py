##### Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

#l = ['a', 'b', [1, 2, 3], 'd']
#a, b, c, d = l
#print(c)

##### Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
  # 1) получите сумму всех чисел,
  # 2) распечатайте все строки, где есть буква 'a'

#list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#1 print(*list_1, sep=", ")

#2 print(list_1[1], list_1[5])


# Printing the list using loop  (Not homework)
#list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#for i in range(len(list_1)):
#    print(list_1[i])

#####  Напишите программу, которая определяет, какая семья больше.
         #1) Программа имеет два input() - например, family_1, family_2.
         #2) Членов семьи нужно перечислить через запятую.
         #3)Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')


#family1 = input("Number of members on a 1st family: ").split(',')
#family2 = input("Number of members on a 2nd family: ").split(',')

#if family1 > family2:
#    print("Family 1")
#elif family1 == family2:
#    print("Equal!")
#else:
#    print("Family 2")

##### 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
  # 1) - о вашем любимом фильме.
  # 2)- распечатайте только ключи
  # 3) - распечатайте только значения
  # 4) - распечатайте пары ключ - значение

#dict = {1: 'title', 2: 'director', 3: 'year', 4: 'budget', 5: 'main_actor', 6: 'slogan'}
#keysList = [key for key in dict]
#print(dict.keys())
#print(dict.values())
#print(dict)


##### Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
#my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
#total = sum(my_dictionary.values())
#print(total)


##### Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
from itertools import groupby

#my_list = [1, 2, 3, 4, 5, 3, 2, 1]
#print(list(set(my_list)))

##### Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     #- найдите значения, которые встречаются в обоих множествах
     #- найдите значения, которые не встречаются в обоих множествах
     #- проверьте являются ли эти множества подмножествами друг друга

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

#print(set1.issubset(set2))
#print(set2.issuperset(set1))
print(set2.intersection(set1))
print(set2.difference(set1))
print(set1)












