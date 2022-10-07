##### 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа):периметр квадрата, площадь квадрата и диагональ квадрата.
#import math

#def square(width, height,):
#	area = width * height
#	perimeter = 2 * (width + height)
#	diagonal = math.sqrt(2) * (width)
#	print("Area of a square is:", area)
#	print("Perimeter of a square is:", perimeter)
#	print("Diagonal of a square is:", diagonal)
#width = float(input('Enter the Width: '))
#height = float(input('Enter the Height: '))
#square(width, height)



##### 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
     # в формате аргумент: значение. Например:
	# name: John
	# last_name: Smith
	# age: 35
	# position: web developer

#def person(name, last_name, age, position):
#	return ("First Name: {}\nLast Name: {} \nAge: {} \nPosition: {}".format(name, last_name, age, position))
#print(person(name='Diana', last_name= 'Florea', age=26, position ='Ingineer'))



# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#     положительные числа

#my_list = [20, -3, 15, 2, -1, -21]
#pos_num = list(filter(lambda x: (x >= 0), my_list))
#print(pos_num)

##### 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке

#from functools import reduce
#def new_list(my_list):
#	result = reduce(lambda x, y: x*y, my_list)
#	return result
#my_list = [20, -3, 15, 2, -1, -21]
#print("Multiply all the numbers of the list:", new_list(my_list))

##### 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
     # Примените эти функции в качестве методов в другом файле.

