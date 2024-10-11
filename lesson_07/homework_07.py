# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result >= 25:
            break
            # Enter the action to take if the result is greater than 25
        print(f'{str(number)} x {str(multiplier)} = {str(result)}')

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел."""

a = input("Введіть перше число:")
b = input("Введіть друге число:")
def add_numbers(a, b):
    return a + b
result = add_numbers(int(a), int(b))
print(f'Результат суми двох чисел = {result}')


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def calculate_average(numbers):
    return sum(numbers)/len(numbers)

list_of_numbers = input('Введіть список з чисел через пробіл: ')
numbers = [int(num) for num in list_of_numbers.split()]

result = calculate_average(numbers)
print(f'Середнє арифметичне = {result}')

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(s):
    return s[::-1]
item = input('Введіть рядок: ')
list_of_item = [str(word) for word in item.split()]
print (reverse_string(list_of_item))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(words):
    return max(words, key=len)

words = input('Введіть список слів через пробіл: ')
list_of_item = [str(word) for word in words.split()]

result = longest_word(list_of_item)
print(f'Найдовше слово = {result}')


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


# task 7 (Homework 6.1): Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.

def unique_count(item):
    unique_count_set = set(item)
    return len(unique_count_set) > 10

my_unique_list = input('Введіть список змінних:')
result = unique_count(my_unique_list )
print(result)

# task 8 (Homework 6.4): Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

def is_even(n):
    return n % 2 == 0
lst_1 = input('Введіть список з чисел через пробіл: ')
numbers = [int(num) for num in lst_1.split()]
filtered_numbers = filter(is_even, numbers)
even_numbers = list(filtered_numbers)
result = sum(even_numbers)
print(f'Сума парних чисел = {result}')

# task 9 (Homework 6.3): Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.

def item(n):
    return isinstance(n, str)
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for element in lst1:
    if item(element):
        lst2.append(element)
result = lst2
print(result)

# task 10 (Homework 6.2): Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

def has_letter_h(word):
    return 'h' in word.lower()

def get_word():
    return input('Введіть слово з літерою "h": ')

def main():
    while True:
        word = get_word()
        if has_letter_h(word):
            print('Слово має літеру "h".')
            break
        else:
            print('Ви ввели слово без літери "h".')
print(main())

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""