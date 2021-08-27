"""
3) Создайте 3 декоратора, каждый из которых применяет к тексту определённый стиль:
выделение жирным <b>...</b>\
курсив <i>...</i>
подчеркивание <u>...</u>.
Далее создайте функцию которая будет возвращать текст “Hello world”, примените к этой функции цепочку декораторов
"""

# def decorator1(func):
#     def wrapper():
#         return f'<b>{func()}</b>'
#     return wrapper

# def decorator2(func):
#     def wrapper():
#         return f'<i>{func()}</i>'
#     return wrapper
    
# def decorator3(func):
#     def wrapper():
#         return f'<u>{func()}</u>'
#     return wrapper
    

# @decorator1
# @decorator2
# @decorator3
# def hello():
#     return 'Hello World'

# a = hello()
# print(a)

"""
4) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). 
Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. 
Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
"""
# from math import pi

# class Circle:
#     color = 'blue'
#     digit = pi

#     def __init__(self, radius):
#         self.r = radius
#     def square(self):
#         return self.digit*self.r**2

# first_circle = Circle(14)
# first_circle.color = 'red'
# print(first_circle.square())

"""
7) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, 
который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и 
вызовите метод method1.
"""

class A:

    def method1(self):
        print('Основной функционал')

class B(A):
    def __init__(self) -> None:
        super().__init__()
    def method1(self):
        super().method1()
        print('Дополнительный функционал')

instance1 = B()
instance1.method1()
