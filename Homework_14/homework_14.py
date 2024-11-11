class Student:
    def __init__(self, name, surname, age, everage_mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.everage_mark = everage_mark

    def update_everage_mark(self, new_mark):
        self.everage_mark = new_mark

    def display_info(self):
        print = (f" Name={self.name}, Surname={self.surname}, Age={self.age}, Everage_mark={self.everage_mark}")

student = Student(name="Kate", surname="Honcharova", age="30", everage_mark=10)
student.display_info()

student.update_everage_mark(24)
student.display_info()



