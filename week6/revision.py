"""
Создайте класс мобильного телефона. Определите непубличные
 атрибуты для imei, уровня
заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 %
заряда при каждом обращении.
Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
разряжен).
Также предусмотрите возможность заряжания батареи.
"""

""" 
Напишите класс ToDoList для списка завершенных заданий. Каждое задание (имплементируется для этого есть класс Task), состоит из одного стринга кот-е описывает задание и срочность этих заданий: 1(очень низкая), 2(низкая), 3(средняя), 4(высокая), 5(очень высокая). Конструктор принимает два аттрибута, по дефолту срочность будет 3.

    Есть три метода, Put кот-й добавляет таск в конец списка ToDoList.
    Get который выдает самый срочный таск т.е 5, если его нет то 4. Если нет ничего то None
    Count выдает кол-во тасков в ToDoList, если параметр Priority, должны быть посчитаны лишь Tasks, срочность кот-х соответсвует требуемости. Как default argument вы можете взять 1; когда не лежит на интервале от 1 до 5, выдайте 0
    Используйте обычный Python-List внутренний тип данных ToDoList, для GET используйте оператор <. Т.е Task меньше другого Task, когда его срочность ниже. Используйте str, чтобы получить результат каждого таска, а так же общий лист. 
"""

# from functools import reduce


# class ToDoList:
#     def init(self):
#         self.tasks = list() # creating an empty list 


#     def put(self, todo):
#         self.tasks.append(todo) # adding task to the list
        

#     def get(self):
#         get = [[i.task, i.priority] for i in self.tasks] # getting the objects from list
#         if get:  # checks if it is not empty
#            max_value = list(reduce(lambda x, y: x if y[1] < x[1] else y, get)) # getting the maximum urgent value 
#            return f'In my highest priority is to {max_value[0]}' # getting that corresponding task 
#         else:
#             return None # if list is empty


#     def count(self, priority=1):
#         self.priority = priority
#         self.counts = list() # empty list for adding filtered data

#         for i in self.tasks: # itering the list
#             if self.priority in range(1, 6): # checks if priority is between 1-5
#                 if i.priority == self.priority: 
#                     self.counts.append(i) # adding to the list 
#                     print(i) # showing the matching items
#             else:
#                 self.priority = 0 # changing to 0 if does not match
#         return f'i have {len(self.counts)} tasks with {self.priority} priority level '



# class Task(ToDoList):   

#     def __init__(self, task, priority=3):
#         self.task = task
#         self.priority = priority
    
#     def __str__(self):
#         return f"i have to {self.task} and its priority level is : {self.priority}"



# v = ToDoList()

# a = Task('go', 1)
# b = Task('wait', 4)
# c = Task('start', 4)
# d = Task('check', 3)
# v.put(a)
# v.put(b)
# v.put(c)
# v.put(d)


# print(v.get())

# print(v.count(5))

# print(v.count())

"""
 Задание:

  Класс Tomato:
1. Создайте класс Tomato
2. Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
3. Создайте метод init(), внутри которого будут определены два динамических protected свойства: 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
4. Создайте метод grow(), который будет переводить томат на следующую стадию созревания
5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)

Класс TomatoBush
1. Создайте класс TomatoBush
2. Определите метод init(), который будет принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая

Класс Gardener
1. Создайте класс Gardener
2. Создайте метод init(), внутри которого будут определены два динамических свойства: 1) name - передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является protected
3. Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
5. Создайте  метод knowledge_base(), который выведет в консоль справку по садоводству.

Реализуйте:
1. Вызовите справку по садоводству
2. Создайте объекты классов TomatoBush и Gardener
3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
4. Попробуйте собрать урожай
5. Если томаты еще не дозрели, продолжайте ухаживать за ними
6. Соберите урожай
"""

class Tomato:
    states = {
        0: 'nothing', 
        1: 'flower', 
        2: 'green tomato', 
        3: 'red tomato'
        }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state <3:
            self._state += 1
        self._print_state()

    def _print_state(self):
            print(f'Tomato {self._index} is {self._state}')

class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num - 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Gardener started to work')
        self._plant.grow_all()
        print('Gardener has finished work')

    def harvest(self):
        if self._plant.all_are_ripe() == True:
            self._plant.give_away_all()
            print('Harvesting is over')
        else:
            print('It is not time for harvest')

    def knowledge_base(self):
        print('Tomatoes should be harvetes in summer')

tomato_bush = TomatoBush(4)
gardener1 = Gardener('Juan', tomato_bush) 
gardener1.knowledge_base()
gardener1.work()