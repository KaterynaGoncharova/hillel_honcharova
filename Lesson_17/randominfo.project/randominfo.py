from faker import Faker

class Person:
    def __init__(self):
        fake = Faker()
        self.full_name = fake.name()
        self.gender = fake.random_element(['Male', 'Female'])
        self.country = fake.country()
        self.address = fake.address()

    def __str__(self):
        return f'{self.full_name}, {self.gender}, {self.country}, {self.address}'
