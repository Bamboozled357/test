"""Модификаторы доступа:
1. public - password, get_info()
2. protected - _password, _get_info()
3. private - __password, __get_info()
"""

# class User:
#     def __init__(self, username, password) -> None:
#         self.username = username
#         self.__password = password

#     def get_password(self, username):
#         if self.username == username:
#             return self.__password
#         else:
#             return 'Screw You, scammer!'

#     def set_password(self, old_password, new_password):
#         if self.__password == old_password:
#             self.__password == new_password
#         else:
#             return 'I told you to get the hell outta here!'

#     def __get_info(self):
#         print(f'Username {self.username}, password {self.__password}')

# user1 = User(username='skunkhunt42', password='zxcqwerty')
# print(user1.username)
# print(user1.get_password(username='skunkhunt42'))
# user1.set_password(old_password='zxcqwerty', new_password='pepperonimakaroni')
# print(user1.get_password(username='qwerty'))
# print(user1.get_password(username='skunkhunt42'))




# class Divider:
#     def __init__(self) -> None:
#         self.__divide_num = 2

#     @property          #-> getter
#     def divider(self):
#         return self.__divide_num

#     @divider.setter   # -> setter
#     def divider(self, value):
#         if not value == 0:
#             self.__divide_num = value
#             return 'Successfully changed divide number!'
#         else:
#             return 'You are fanook!'

#     def divide(self, value):
#         return value / self.__divide_num

# obj = Divider()

# print(obj.divider)
# print(obj.divide(7))
# obj.divider = 14
# print(obj.divider)




# class Person:
#     def __init__(self, name, last_name) -> None:
#         self.name = name
#         self.last_name = last_name
#     @property
#     def full_name(self):
#         return f'{self.name} {self.last_name}'

# person = Person(name='Jaime', last_name='Lannister')
# print(person.full_name)


# class Car:

#     def _inject_fuel(self):
#         print('Fuel injected')

#     def _init_bang(self):
#         print('Bang!')

#     def _send_signal_to_ignition_system(self):
#         print('Ingnition started')
#         self._inject_fuel()
#         self._init_bang()

#     def _send_signal_to_pc(self):
#         print('Start')
#         self._send_signal_to_ignition_system()

#     def start_engine(self):
#         self._send_signal_to_pc()

# car1 = Car()
# car1.start_engine()



"""
1. underscore
2. protected - we still can get hidden data
3. protected data inheritating in daughter classes
"""

# class A:
#     def __say_hello(self):
#         print('Hello, my friends!')

# class B(A):
#     pass

# b = B()
# b.__say_hello()

"""
РАЗБОР Classwork
"""

"""Классная работа
По теме: Инкапсуляция
Создайте класс Terminal. Создайте объект-карточку от этого класса, передав номер своей карточки и пин код. При этом, необходимо проверить валидность карточки: номер карточки должен содержать строго 16 цифр, а пин код - 4 цифры (для этого используйте инкапсуляцию). При создании карточки в ней содержится 0 сом. Далее в классе должны быть следующие методы:
метод put, который будет принимать в качестве аргументов: пин код карточки, вторым аргументом - сумму денег, которую вы хотите закинуть на эту карточку. Прежде, чем закидывать деньги, необходимо проверить введенный пин код на совпадение (используйте инкапсуляцию)
метод get_money, который также принимает первым аргументом пин код, вторым аргументом - сумму денег, которую вы хотите извлечь из карточки. Здесь также необходимо использовать валидацию: проверка пин кода + сумма денег должна быть округленной до десятичных чисел, типа 10, 100, 200, 5000 и т.д. (67, 899, 45.6 - невалидные данные). И только после проверки деньги извлекаются.
Примените данные методы к своей карточке несколько раз и в конце выдайте, сколько денег на карточке. Примечание: нельзя извлечь сумму денег, если она больше, чем сумма денег на карточке; также нельзя вытащить пин код карточки (эти данные должны быть скрыты)"""

# class Terminal:

#     money_count = 0

#     def __init__(self, card, pin) -> None:
#         self.card = card
#         self.__pin = pin
#         if len(self.card) == 16 and len(self.__pin) == 4:
#             print('Here you go!')
#         else:
#             print('No way!')

#     def put(self, pin, money):
#         if pin == self.__pin:
#             self.money_count += money
#             print('Money accepted')
#         else:
#             print('Wrong pin!')
#         return self.money_count

#     def get_money(self, pin, money):
#         if pin == self.__pin:
#             if money % 10 <= self.money_count:
#                 if money % 10 == 0:
#                     self.money_count -= money
#                 else:
#                     print('No such a bill')
#             else:
#                 print('You do not have enough money')
#         else:
#             print('Pin is incorrect')
            


# credit_card = Terminal('1234567898765432', '7208')
# credit_card.get_money('7208', 2000)
# credit_card.get_money('7208', 2000)


"""Homework"""

"""
1)Создайте класс и объявите в нём 3 метода: публичный, защищённый и приватный. Затем создайте экземпляр данного класса и вызовите по очереди каждый из методов.
"""
# class A:
#     def public(self):
#         print('I am public method!')

#     def _protected(self):
#         print('I am protected method!')

#     def __private(self):
#         print('I am private method!')

# a = A()
# print(a.public())
# print(a._protected())
# print(a.__private())



"""
2)Определите класс A, в нём объявите метод method1, который печатает строку "Hello World". Затем создайте класс B, который будет наследоваться от класса A. Создайте экземпляр от класса B, и через него вызовите метод method1.
"""
# class A:
    
#     def method1(self):
#         print('Hello World!')

# class B(A):
#     pass

# obj = B()
# obj.method1()

"""
3)Объявите класс Car, в котором будет приватный атрибут экземпляра speed. Затем определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, с помощью которого Вы будете получать значение скорости.
"""
# class Car(object):
    
#     def set_speed(self):
#         pass
    
#     def show_speed(self):
#         pass


        

"""
4)Перепишите класс Car из предыдущего задания.
Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора @property, для того чтобы можно было работать с данным классом следующим образом:

car = Car()
car.speed = 120
print(car.speed)
"""
# class Car:

#     def __init__(self):
#         self.speed = 80

#     @property          #-> getter
#     def speed(self):
#         return self.__speed

#     @speed.setter   # -> setter
#     def divider(self, value):
#        pass

#     def divide(self, value):
#         return value / self.__divide_num

# car = Car()
# car.speed = 120
# print(car.speed)

"""
1.Создайте класс PrivateProject. Внутри этого класса есть атрибуты класса: github_link и developers.
В github_link хранится ссылка на проект (любая), а в developers хранится список с юзернеймами, у которых есть доступ к этой ссылке (атрибуту github_link).
Создайте объект класса PrivateProject, при создании необходимо передать в качестве аргумента username.
Далее, попытайтесь через созданный объект класса получить атрибут github_link. При этом, если данный username есть в списке developers, ему открыт доступ к ссылке.
В противном случае выводится сообщение: Forbidden. Список developers должен быть скрыт.
"""

class PrivateProject:
    github_link = 'https://github.com/features/codespaces'
    developers = ['Lyuba', 'Sergei', 'Alesha', 'Matthew']

    def __init__(self, username, github_link, developers):
        self.username = username
        self.__github_link = github_link
        self.__developers = developers

    def check_username(self):
        if self.username in self.__developers:
            return f'Вот ваша ссылка: {self.__github_link}'
        else:
            return 'Forbidden'

obj = PrivateProject(username='Lyuba', github_link, developers)
print(obj.check_username)



"""
2.Создайте класс User. В этом классе есть защищенный метод _create_user, который принимает email и password. Этот метод вызывается в публичных методах create_user и create_superuser. Оба метода отличаются друг от друга тем, что в методе create_user атрибут is_superuser имеет значение False, а в методе create_superuser - True.
Также в классе есть метод admin_login, который принимает password.
Создайте два объекта от класса User. К первому объекту примените метод create_superuser, а ко второму - create_user. Далее у обоих объектов вызовите метод admin_login, передав правильные пароли.
У первого объекта должно выдаваться сообщение Successfully logged in, а у второго - Forbidden, так как поле is_superuser у второго объекта имеет значение False. Также если даже is_superuser у первого объекта True, ему не удасться залогиниться, если он передал неправильный пароль password в метод admin_login и ему выдается сообщение: Invalid password.
"""




"""РАЗБОР АДИЛЕТА"""    

# Инкапсуляция

"""
1. Объединение данных и функций, которые работают с этими данными в один объект
2. Набор инструментов для сокрытия реализации объекта
"""

# Модификаторы доступа:

# public - Публичные атрибуты и методы доступны в классе, в дочерних классах и вне класса

# protected - Защищённые атрибуты и методы недоступны вне класса, но при этом доступны в самом классе и его дочерних классах

# private - Приватные атрибуты и методы доступны только внутри самого класса, где они определяются и недоступны в дочерних классах и вне классов

# class A:

#     attr1 = 10 # public
#     _attr2 = 12 # protected
#     __attr3 = 24 # private

#     def method(self): # public
#         pass

# class B(A):
#     pass

# b = B()
# b._attr2()
# b._attr2 = 20

# b.__attr3
# b._A__attr3

#Сеттеры и геттеры

# class A:
#     def __init__(self, value) -> None:
#         self.__attr1 = value

#     def set_attr1(self, new_value):
#         self.__attr1 = new_value

#     def get_attr1(self):
#         return self.__attr1

# a1 = A(value=10)
# a1._A__attr1 = 20
# a1.get_attr1()

# class Car:
#     __speed = 0

#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self, new_speed):
#         self.__speed = new_speed

# car1 = Car()
# car1.speed = 20
# print(car1.speed)




