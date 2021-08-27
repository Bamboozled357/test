# class, static instance methods

"""
instance method -> self
class method -> @classmethod ->cls
static method -> @staticmethod
"""

# class Makers:
#     language_choices = 'Python', 'JavaScript'

#     def __init__(self, name) -> None:
#         self.name = name

#     def instance_method(self):
#         return f'Hello {self.name}'

#     @classmethod
#     def class_method(cls):
#         return f'Welcome to Makers! What type of language do you choose?: {cls.language_choices}'

#     @staticmethod
#     def static_method(choice):
#         return f'Great! You chose {choice} course'

# user1 = Makers(name='Juan Pablo Ecoscobrava Cortez')
# print(user1.instance_method())
# print(user1.class_method())
# print(user1.static_method(choice='Python'))
# print()
# user2 = Makers(name='Anna Maria Cortez')
# print(user2.instance_method())
# print(user2.class_method())
# print(user2.static_method(choice='JavaScript'))


"""
Использование class метода на примере класса User
"""
# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def get_info(self):
#         return f"{self.name}, {self.email}"

#     @classmethod
#     def add_data(cls, user_info:list):
#         name, email = user_info
#         return cls(name, email)

# list_of_users = [
#     ['Christopher Moltisanti', 'chrissy@gmail.com'],
#     ['Paulie Gaultieri', 'walnuts@yahoo.com'],
#     ['Silvio Dante', 'bing357@hotmail.com']
# ]

# for info in list_of_users:
#     user = User.add_data(info)
#     print(user.get_info())

# user1 = User(name='Anthony Soprano', email='gabagool@hotmail.com')
# print(user1.get_info())

"""
Использование static метода на примере класса Lottery
"""

# class Lottery:
#     def __init__(self, name):
#         self.name = name

#     @staticmethod
#     def _generate_number():
#         import random
#         number = random.sample(list('123456789'), k=5)
#         number = ''.join(number)
#         return number

#     def get_number(self):
#         number = self._generate_number()
#         self.number = number
#         return f"Dear, {self.name}! Your lucky number is {self.number}"

# guy1 = Lottery(name='Juan')
# print(guy1.get_number())

# guy2 = Lottery(name='Maria')
# print(guy2.get_number())

"""
Использование всех типов  методов в классе
"""

# class Pizza:
    
    # def __init__(self, ingredients:list):
    #     self.ingredients = ingredients

    # def __repr__(self):
    #     return f"Pizza with {self.ingredients}"

# pizza1 = Pizza(['tomatoes', 'mozarella', 'basil'])
# pizza2 = Pizza(['meatballs', 'chilli pepper', 'cheese'])

# print(pizza1)
# print(pizza2)

# class Pizza:

#     def __init__(self, ingredients:list):
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f"Pizza with {self.ingredients}"

#     @staticmethod
#     def circle_area(radius):
#         import math
#         area = round(math.pi * radius**2, 2)
#         return f"Pizza's area is {area} cm2"

#     def area(self, radius):
#         self.radius = radius
#         return self.circle_area(self.radius)

#     @classmethod
#     def margarita(cls):
#         return cls(['mozarella', 'tomatoes', 'basil'])

#     @classmethod
#     def pepperoni(cls):
#         return cls(['pepperoni', 'cheese'])

#     @classmethod
#     def chilli(cls):
#         return cls(['chilli peppers', 'cheese', 'sauce'])

# pizza1 = Pizza.margarita()
# print(pizza1)
# print(pizza1.area(4))
# print()
# pizza2 = Pizza.pepperoni()
# print(pizza2)
# print(pizza2.area(8))
# print()
# pizza3 = Pizza.pepperoni()
# print(pizza3)
# print(pizza3.area(2))

# print(Pizza.chilli())


""""""""""""""""""""""Разбор Адилета"""""""""""""""""""""

# Instance методы - имеют доступ к экземпляру класса, также через экземпляр к самому классу(имеют доступ ко всем методам и атрибутам, которые определены в классе)

# class A:
#     attr1 = 10

#     def __init__(self, value):
#         self.attr2 = value

#     def method1(self):
#         print(self.attr1)
#         print(self.attr2)

# Class методы - имеют доступ только к атрибутам и методам класса.

# class MyClass:
#     attr1 = 10

#     def __init__(self, value):
#         self.attr1 = value
    
#     def method1(self):
#         print(self.attr1)
#         # print(self.attr2)

#     @classmethod
#     def method2(cls):
#         print(cls.attr1)
#         # print(cls.attr2) #AttributeError

# obj1 = MyClass(20)
# obj1.method1()
# obj1.method2()

# MyClass.method1()
# MyClass.attr2()


# Static методы - отдельная функция, которая не имеет доступа ни к классу, ни к его объектам

# Они используются в двух случаях:
# 1. Когда нужно добавить в класс логически определённую функцию.

# class A:
    # def method1(self):
    #     print('Hello world')

    # @staticmethod
    # def method1():
    #     print('Hello world')

# class User:
#     def __new__(cls, *args, **kwargs):
#         email = args[0]
#         user = object.__new__(*args, *kwargs)
#         cls.send_mail(email)
#         return user

#     def __init__(self, email, password):
#         self.email = email
#         self.password = password

#     @staticmethod
#     def send_mail(email):
#         ...

# class A:
#     attr1 = 10

#     def method1(self, new_value):
#         self.attr1 = new_value

#     @classmethod
#     def method2(cls, new_value):
#         cls.attr1 = new_value

#     def method3(self, new_value):
#         self.__class__.attr1 = new_value

# a1 = A()
# a2 = A()
# a3 = A()

# # a1.method1(20)
# # a2.method2(30)
# a3.method3(50)

# print(a1.attr1)
# print(a2.attr1)
# print(a3.attr1)


# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# class Arithmetics:
#     @staticmethod
#     def add(x, y):
#         return x + y
    
#     @staticmethod
#     def add(x, y):
#         return x - y

class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = self.encrypt_password(password)

    @staticmethod
    def encrypt_password(raw_password):
        from hashlib import md5
        res = md5(raw_password.encode()).hexdigest()
        return res 

    def login(self, username, password):
        enc_pass = self.encrypt_password(password)
        self.password == enc_pass

user = User('Jon', 'qwerty')
print(user.password)


username1 = 'user1'
username2 = 'user2'
pass1 = 'qwerty'
pass2 = 'qwerty'

from hashlib import sha512, pbkdf2_hmac

hash1 = sha512((pass1+username1).encode()).hexdigest()
hash2 = sha512((pass2+username2).encode()).hexdigest()

print(hash1)
print()
print(hash2)

hash1 = pbkdf2_hmac('sha256', pass1.encode(), username1.encode(), 100000)
hash2 = pbkdf2_hmac('sha256', pass2.encode(), username2.encode(), 100000)


