"""3) Мебель
1. class House: тип дома, общая площадь, оставшаяся площадь и список мебели.
2. Мебель имеет название и площадь, например, кровать: 4 м2, шкаф-купе: 2 м2,
стол: 1,5 квадратных метров.
3. Добавьте вышеуказанную мебель в дом.
4. При печати информации о доме требуется вывод: тип дома, общая площадь,
оставшаяся площадь, список мебели."""

# class House:

#     def __init__(self, house_type, total_area, furniture):
#     self.house_type = house_type
#     self.total_area = total_area
#     self.furniture = furniture

#     def add_furniture(self):
#         remaining_area = self.total_area - sum(furniture)
#         print(self.type, self.total_area, remaining_area, furniture)

# furniture = {'кровать': 4, 'шкаф-купе': 2, 'стол': 1.5}

# house = House('house', 110, furniture)
# house.add_furniture
""" 
Напишите класс ToDoList для списка завершенных заданий. Каждое задание (имплементируется для этого есть класс Task), состоит из одного стринга кот-е описывает задание и срочность этих заданий: 1(очень низкая), 2(низкая), 3(средняя), 4(высокая), 5(очень высокая). Конструктор принимает два аттрибута, по дефолту срочность будет 3.

    Есть три метода, Put кот-й добавляет таск в конец списка ToDoList.
    Get который выдает самый срочный таск т.е 5, если его нет то 4. Если нет ничего то None
    Count выдает кол-во тасков в ToDoList, если параметр Priority, должны быть посчитаны лишь Tasks, срочность кот-х соответсвует требуемости. Как default argument вы можете взять 1; когда не лежит на интервале от 1 до 5, выдайте 0
    Используйте обычный Python-List внутренний тип данных ToDoList, для GET используйте оператор <. Т.е Task меньше другого Task, когда его срочность ниже. Используйте str, чтобы получить результат каждого таска, а так же общий лист. 
"""

"""Лекция Адилета"""

#Полиморфизм - метод с одинаковым названием и может реализовываться по-разному в разных объектах

# a = 1
# b = 2
# # сложение
# res = a + b #3
# res = a.__add__(b) # под капотом

# a = '1'
# b = '2'
# # конкатенация
# res = a + b #'12'
# res = a.__add__(b) # под капотом

# a = [1]
# b = [2]
# res a + b #[1, 2]

# Полиморфизм - возможность функции работать с объектами разных типов, если у них реализован определённый метод (интерфейс)

# len() - возвращает длину контейнера (строки, списки, кортежи, словари, множества)

# a1 = 'string'
# a2 = [1,2,3,4,5]
# a3 = (1,2,3,4,5)
# a4 = {'a': 1, 'b': 2}

# len(a1) #6 a1.__len__()
# len(a2) #5 a2.__len__()
# len(a3) #5 a3.__len__()
# len(a4) #2 a4.__len__()

# class MyClass:
#     def __len__(self):
#         return 0

# object1 = MyClass()
# print(len(object1))

# class MyClass:
#     def __init__(self, students):
#         self.students = students

# class1 = MyClass(['Aibek', 'Nursultan', 'Karim', 'Merina'])
# len(class1.students)

# def len(obj):
#     return obj.__len__()

# list

# class int:
#     def __init__(self, value):
#         pass

#     def __str__(self):
#         return str(self.value)

# a1 = 1
# a2 = '2'
# a3 = [1,2,3,4,5]

# class A(object):
#     pass
# a4 = A()
# print(dir(a4))

# print(a1)
# print(a2)
# print(a3)
# print(a4)



# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def triangle_area(self):
#         return 0.5 * self.base *self.height

# tr1 = Triangle(10, 10)

# class Square:
#     def __init__(self, side):
#         self.side = side      

#     def square_area(self):
#         return self.side **2

# squ = Square(10)

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def circle_area(self):
#         return 4.14 * self.radius ** 2

# crcl = Circle(10)

# def get_shape_area(shape):
#     if type(shape) == Square:
#         return shape.square_area()
#     elif type(shape) == Circle:
#         return shape.circle_area()
#     return shape.triangle()

# print(get_shape_area(tr1))

# Абстрактный класс  - класс, который имеет абстрактные методы (класс, который нужно уточнить при наследовании).

# class Transport:
#     def move(self):
#         raise NotImplementedError()

# class LandTransport(Transport):
#     def move(self):
#         print('Двигается по суше')

# tr1 = LandTransport()
# tr1.move()

# from abc import ABC, abstractclassmethod

# class Transport(ABC):
#     @abstractclassmethod
#     def move(self):
#         pass

# class AirTransport(Transport):
#     def move(self):
#         print('Летим')

# obj1 = AirTransport()

# class Transport:
#     def move(self):
#         pass

from Example.test1 import *
