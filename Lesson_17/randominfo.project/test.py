import random

allAddrs = [
    '123 Main St, Springfield',
    '456 Elm St, Shelbyville',
    '789 Oak St, Capital City'
]

def get_address():
    return random.choice(allAddrs) if allAddrs else "Немає доступних адрес"

class Person:
    def __init__(self):
        self.address = get_address()

person = Person()
print(person.address)