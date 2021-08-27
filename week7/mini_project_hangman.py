"""
ТЗ "Виселица" 
Требования: 
1) Есть список слов, из которых будет выбираться рандомом(случайным образом) одно для угадывания. 
2) Сразу же будет печататься длина слова знаками "*" 
3) Дальше участнику нужно ввести какую-либо букву и если она есть, то "*" заменяются на эту букву, а если ее нет, то количество попыток снижается на 1. 
Все эти операции будут проходить в цикле while, где условием закрытия программы будут: 
● угадывание слова (победа) 
● либо количество попыток == 0. 
Например: 
● Слово: "Книга" 
● Печатается: "*****" 
● По мере угадывания появляются буквы: "*нига" 
● Также, параллельно принтится количество попыток
"""

'''
4. Разработчики
Напишите абстрактный класс Coder с атрибутом count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать обязательный параметр languages_backend, а Frontend — languages_frontend соответственно.

Переопределите в обоих классах методы get_info(Должен возвращать язык программирования и количество часов кодинга) и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time).

Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов.

Создайте экземпляры от классов Backend, Frontend, FullStack (obj_back, obj_front, obj_full_stack) и вызовите все их методы.
'''
# from abc import ABC, abstractmethod

# class Coder(ABC):
#     pass

"""
Given an integer n, return a string array answer (1-indexed) where:
    • answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    • answer[i] == "Fizz" if i is divisible by 3.
    • answer[i] == "Buzz" if i is divisible by 5.
    • answer[i] == i if non of the above conditions are true.
 
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]
Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuz

"""

# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         for i in

