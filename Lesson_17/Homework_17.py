import os
import zipfile

archive_path = "/Users/katerynagoncharova/Hillel_course/pythonProject/hillel_honcharova/Lesson_17/randominfo.zip"
project_folder = "/Users/katerynagoncharova/Hillel_course/pythonProject/hillel_honcharova/Lesson_17/randominfo.project"

with zipfile.ZipFile (archive_path, "r") as zip_ref:
    zip_ref.extractall(project_folder)
print (f"Проект розпаковано у папку: {project_folder}")

test_file_content = """ import randominfo
person = randominfo.Person()
print(person.full_name, person.gender, person.country, person.address)
"""

test_file_path = os.path.join(project_folder , "test.py")
with open (test_file_path, "w") as file:
    file.write(test_file_content)

print(f"Файл test.py створено в {test_file_path}")