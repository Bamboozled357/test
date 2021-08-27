# class X:
#     pass

# obj = X()
# print(dir('makers'))

# def func():
#     pass

# print(dir(func))

# 1. __init__() - инициализирует объект

# class User:
#     def __init__(self, **kwargs):
#         print('Object is initializing...')
#         self.name = kwargs['name']
#         self.familia = kwargs['last_name']
#         print('Object is initialized')

# user = User(name='Linus', last_name='Torvalds')
# print(user.name)
# print(user.familia)

# 2. __new__() - конструктор, отвечающий за то, что происходит в момент создания объекта класса. Срабатывает раньше чем __init__().
 
# class Human:
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         instance = object.__new__(cls)
#         instance.heart = '4хкамерное'
#         print('Object created')
#         return instance

#     def __init__(self, name, last_name):
#         print('Object is initializing...')
#         self.name = name
#         self.familia = last_name

# human1 = Human(name='Linus', last_name='Torvalds')
# print(human1.heart)
# human2 = Human('Jon', 'Snow')

# Шаблон Singleton - предоставляет механизм создания одного и только одного экземпляра объекта, и предоставление к нему глобальную точку доступа.

# class Sun:
#     instance = None

#     def __new__(cls):
#         if not cls.instance:
#             cls.instance = object.__new__(cls)
#         return cls.instance

# sun1 = Sun()
# sun2 = Sun()
# sun3 = Sun()
# print(sun1 is sun2)
# print(id(sun1))
# print(id(sun2))
# print(id(sun3))


# 3. __str__

# class Human:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_fullname(self):
#         return f"{self.name}, {self.last_name}"

#     def __str__(self):
#         return self.get_fullname()
        

# human1 = Human('Linus', 'Torvalds')
# print(human1)

# 4. __repr__()


# class Human:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name

#     def __str__(self):
#         return f"{self.name}, {self.last_name} - сработал метод str"

#     def __repr__(self):
#         return f"{self.name}, {self.last_name} - сработал метод repr"

# human = Human('Jon', 'Snow')
# print(human)

"""
__add__(self, other) -> +
__sub__(self, other) -> - 
__mul__(self, other) -> *
__truediv__(self, other) -> /
__mod__(self, other) -> %

"""

# class MyInt(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         # self.value + other
#         return self.value + other/3

# a = MyInt(10)
# print(a + 5)

#"""""""""""""""""""""""""РАЗБОР АДИЛЕТА"""""""""""""""""""

# Magic methods, dunder, super methods

# __init__, __str__ - все те методы, которые с обеих сторон выделены двумя нижими подчеркиванимями

# __new__ - конструктор, отвечающий за создание объекта

# class Course:
#     _max_students = 10

#     def __new__(cls, *args, **kwargs):
#         print('NEW!')
#         students = args[0]
#         if len(students) > cls._max_students:
#             raise Exception('...')
#         # course = object.__new__(cls)
#         # course.__init__(*args, **kwargs)
#         return object.__new__(cls)


#     def __init__(self, students: list) -> None:
#         self.stidents = students
        

# course1 = Course(['A', 'B', 'C'])

# Синглтон это класс, у которого может быть только один объект

# class Contacts:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __init__(self, phone, email, address):
#         self.phone = phone
#         self.email = email
#         self.address = address

# contact1 = Contacts('99677403i5873', 'test@gmmai;.om', 'Токтогула 2434')
# contact1.email = 'test2@gamil.com'
# print(contact1.email)

        

# a = 4
# b = 45
# c = 10

# e = None
# f = None
# d = None

# Если пользователь пытается добавить число, большее, чем установлено максимумом, то не давать создавать курс

# __init__ - инициализатор, который устанавливает свойств объекта

# __del__ - деструктор, срабатывающий когда объект удаляется

# Магические методы арифметических операторов

# "+" -> __add__(self, other) -> self + other
# a, b = 10, 20
# a + b -> a.__add__(b)


# class A:
#     def __init__(self, value) -> None:
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value


# a1 = A(10)
# a2 = A(20)

# res = a1 + a2 #-> a1.__add__(a2)
# print(res)

# "-" self - other -> self.__sub__(other)

# "*" self * other -> self.__mul__(other)

# "/" self / other -> self.__truediv__(other)

# "//" self // other -> self.__floordiv__(other)

# "%" self % other -> self.__mod__(other)

# "**" self ** other -> self.__pow__(other)

# "abs()" abs(self) -> self.__abs__()
# round() __round__

# Операции сравнения:

# ">" __gt__
# ">=" __ge__
# "<" __lt__
# "<="__le__
# "!=" __ne__
# "==" __eq__

# class Student:
#     def __init__(self, name, age, rating) -> None:
#         self.name = name
#         self.age = age
#         self.rating = rating

#     def __gt__(self, other):
#         return self.rating > other.rating

# student1 = Student('Anna', 26, 100)
# student2 = Student('Tilek', 48, 26)

# print(student1 > student2)

# class int:
#     def __init__(self, value) -> None:
#         self.value = value

#     def __lt__(self, other):
#         return self.value < other.value

# print(student1 > student2)


# Преобразование типа:

# class int(object):
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return self.value

# a = 4
# a = int('4')
# str() #-> __str__()

# class A:
#     def __init__(self, value1, value2) -> None:
#         self.value1 = value1
#         self.value2 = value2

#     def __str__(self):
#         return 'Значение!'


# a1 = A(10, 20)
# res = str(a1)
# print(res)

# int() -> __int__()
# float() -> __float__()
# list() -> __list__()
# bool() -> __bool__()

# len() __len__()
# in __contains__()
# a = [1,2,3,4]

# a[0] #__getitem__()
# a[0] = 5 # __setitem__()
# del a[1] # __delitem__()

# b = {'a': 1, 'b': 2, 'c': 3}


# b['b']
# b['b'] = 10
# del b['b']

class A:
    attr = 10

a1 = A()

a1.attr # __getattribute__()
a1.attr = 20 # __setattr__()
del a1.attr # __delattr__()

getattr()
setattr()
delattr()

