# JSON ( JavaScript Object Notation) - формат обмена данными

# notebook = {
#     'brand': 'Acer',
#     'model': 'Aspire',
#     'ram': 8,
#     'hdd': 500,
#     'has_type_c': True,
#     'cd_drive': None
# }

# 1. Используются двойные кавычки
# 2. Ключом может быть только строка

# class Notebook:
#     def __init__(self, brand, model, ram, hdd, accessories) -> None:
#         self.brand = brand
#         self.model = model
#         self.ram = ram
#         self.hdd = hdd
#         self.accessories = accessories

# note1 = Notebook('Apple', 'MacBook Pro', 16, 256, ['headphones', 'case', 'mouse'])
# note2 = Notebook('Asus', 'ROG', 24, 1000, [])

# notebooks = [note1, note2]

# import json

# class NotebookEncoder(json.JSONEncoder):
#     def default(self, object):
#         return object.__dict__

# res = json.dumps(notebooks, indent=2, cls=NotebookEncoder)
# print(res)

# '[{},{}]'


# notes = '[{"brand": "Acer","model": "Aspire","ram": 8,"hdd": 500,"has_type_c": false,"cd_drive": null}]'

# class Notebook:
#     def __init__(self, brand, model, ram, hdd, has_type_c, cd_drive) -> None:
#         self.brand = brand
#         self.model = model
#         self.ram = ram
#         self.hdd = hdd
#         self.has_type_c = has_type_c
#         self.cd_drive = cd_drive



import json

# from collections import namedtuple

# def decoder(notebook_dict):
#     return namedtuple('Notebook', notebook_dict.keys())(*notebook_dict.values())


# notebooks = json.loads(notes, object_hook=decoder)
# print(notebooks)
# print(type(notebooks))

# students = [
#     {'name': 'Alisher', 'age': 25},
#     {'name': 'Ivan', 'age': 23}
# ]

# file = open('test.json', 'w')
# res = json.dumps(students)
# file.write(res)
# file.close()

# file = open('test.json', 'w')
# json.dump(students, file)
# file.close()

file = open('test.json')

content = file.read()

students = json.loads(content)

file.close()

file = open('test.json')
students = json.load(file)
file.close()
