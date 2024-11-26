import os
import zipfile

archive_path = "/Users/katerynagoncharova/Hillel_course/pythonProject/hillel_honcharova/Lesson_17/randominfo.zip"
project_folder = "/Users/katerynagoncharova/Hillel_course/pythonProject/hillel_honcharova/Lesson_17/randominfo.project"


with zipfile.ZipFile(archive_path, "r") as zip_ref:
    zip_ref.extractall(project_folder)
print(f"Проект розпаковано у папку: {project_folder}")

randominfo_file_path = os.path.join(project_folder, "randominfo.py")

if not os.path.exists(randominfo_file_path):
    randominfo_content = """from faker import Faker

class Person:
    def __init__(self):
        fake = Faker()
        self.full_name = fake.name()
        self.gender = fake.random_element(['Male', 'Female'])
        self.country = fake.country()
        self.address = fake.address()

    def __str__(self):
        return f'{self.full_name}, {self.gender}, {self.country}, {self.address}'
"""

    with open(randominfo_file_path, "w") as file:
        file.write(randominfo_content)
    print(f"Файл randominfo.py створено в {randominfo_file_path}")


test_file_content = """import randominfo
person = randominfo.Person()
print(person.full_name, person.gender, person.country, person.address)
"""

test_file_path = os.path.join(project_folder, "test.py")
with open(test_file_path, "w") as file:
    file.write(test_file_content)

print(f"Файл test.py створено в {test_file_path}")