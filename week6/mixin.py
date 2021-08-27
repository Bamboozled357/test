
"""Напишите декоратор repeat, который принимает как именованный аргумент num целое число (количество выполнения декорированной функции) и запускает декорированную функции указанное количество раз.

Например
```python
@repeat(num=4)
def function(name):
    print(f"{name}")

При вызове function("Python"), вывод должен выглядеть так:
Python
Python
Python
Python
"""

# def repeat(num=1):
#     def momo(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 func(*args)
#         return wrapper
#     return momo

# @repeat(num=4)
# def function(name):
#     print(f'{name}')

# function ('Python')



"""Напишите декоратор countdown, который принимает параметр seconds и отсчитывает секунды до запуска декорированной функции.

Например:
```python
@countdown(seconds=5)
def func():
    print('Hello world')
```
#вывод
5
4
3
2
1
Hello world!
"""
# def repeat(num=1):
#     def momo(func):
#         def wrapper(*args, **kwargs):
#             n = num
#             for i in range(num):
#                 print(n)
#                 n -= 1
#             func(*args)
#         return wrapper
#     return momo

# @repeat(num=4)
# def function(name):
#     print(f'{name}')

# function ('Python')



#""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Multiple Inheritance

# class Parent:
#     def who_am_i(self):
#         print('I am a parent')

# class Child(Parent):
#     def who_am_i(self):
#         super().who_am_i()
#         print('I am a child')

# child = Child()
# child.who_am_i()

# class Father:
#     last_name = 'White'

# class Mother:
#     last_name = 'Brown'

# class Child(Father, Mother):
#     pass

# child = Child()
# print(child.last_name)

#""""""""""""""""""""""""TASKS""""""""""""""""""""""""""

"""Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water.
Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
"""
class Auto:
    pass
    def ride(self):
        print('Riding on a ground')

class Boat:
    pass
    def swim(self):
        print('Floating on water')

class Amphibian(Auto, Boat):
    pass

fishy = Amphibian()
fishy.ride()
fishy.swim()

"""Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""

class RadioMixin:

    def play_music(self, song_name):
        print(f'Сейчас для вас играет песня: {song_name}')

class Auto(RadioMixin):
    pass

class Boat(RadioMixin):
    pass

class Amphibian(RadioMixin):
    pass

auto = Auto()
boat = Boat()
amphibian = Amphibian()
auto.play_music('Peaches')
boat.play_music('Leave the Door Open')
amphibian.play_music('Con Altura')

"""Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включаться будильник."""

from datetime import datetime

class Clock:
    a = datetime.now()
    print (a.strftime('%H:%M:%S'))

class Alarm:
    
    def turn_on(self):
        print('Turn on an alarm')
    def turn_off(self):
        print('Turn off an alarm')

class AlarmClock(Clock, Alarm):

    def set_alarm(self):
        return self.turn_on()

alarm1 = AlarmClock()
alarm1.set_alarm()



"""Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""

# from abc import ABC, abstractmethod

# class Coder(ABC):
#     experience = {
#         'junior': 0,
#         'middle': 1,
#         'senior': 2,
#         'architect': 3,
#         'Adilet': 4
#         }
#     count_code_time = 0

#     @abstractmethod
#     def get_info(self):
#         pass

#     @abstractmethod
#     def coding(self):
#         pass

# class BackEnd(Coder):
#     def __init__(self,languages_backend):
#         self.language = languages_backend

# class FrontEnd(Coder):
#     def __init__(self,languages_frontend):
#         self.language = languages_frontend

# class FullStack(BackEnd, FrontEnd):
#     pass



#""""""""""""""""""""""Разбор Эльдияра"""""""""""""""

# class All:
#     def say_hi(self):
#         print('Hi people')

# class A(All):
#     def method_A(self):
#         print('Thiss is method A')


# class B(All):
#     def method_B(self):
#         print('Thiss is method B')


# class C(A, B):
#     def method_C(self):
#         print('This is method C')


# c = C()
# c.say_hi()

class Radio:
    def play_music(self, music):
        print(f'You are listening to {song}')


class Engine:
    pass


class Car:
    pass


class Boat:
    pass

class Bike:
    pass