# Полиморфизм 
"""
1. Объявите 3 переменные, запишите в них строку, список и словарь. Затем запишите эти
переменные в список, пройдитесь по нему циклом и распечатайте длину каждого из объектов.
"""


# a = 'string'
# b = [1,2,3,4,5]
# c = {'a': 1, 'b': 2, 'c': 3}





"""
2. Создайте классы Dog и Cat с одинаковым методом voice, для собак он должен печатать "Гав", для кошек "Мяу". Создайте экземпляр от каждого класса. Затем напишите функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()
"""

# class Dog:
#     print('Гав!')

# class Cat:
#     print('Мяу!')

# sobaken = Dog(self)
    




"""
3. Создайте 3 класса: Person, Employee и Student, при этом Employee и Student должны наследоваться от Person.
Определите во всех трёх классах метод get_info():
- для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.
- для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.
- для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.

Определите функцию get_human_info(), которая будет принимать объект одного из трёх классов, вызывать метод get_info и печатать результат.
"""

class Person(object):
    def get_info(self, first_name, last_name):
        self.name = first_name
        self.last_name = last_name
        print(f'Привет, меня зовут {first_name} {last_name}')


class Employee(Person):
    def get_info(self, first_name, last_name):
        print(f'Привет, меня зовут {first_name} {last_name}, я работаю в компании "Рога и копыта" на должности "директор"')

class Student(Person):
    def get_info(self, first_name, last_name):
        print(f'Привет, меня зовут {first_name} {last_name}, я учусь в КГТУ на 3 курсе')




"""
4. Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.
Затем наследуйте от Shape три класса: Triangle, Square и Circle.

- треугольник создаётся с заданными основанием и высотой
- квадрат создаётся с заданной длиной стороны
- круг создаётся с заданным радиусом

Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.
Затем создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area().

Подсказка: для создания абстрактных классов воспользуйтесь модулем [abc](https://docs.python.org/3/library/abc.html)
"""

#пишите код здесь