""""# task 3
  Написати функцію, яка розрахує середнє арифметичне списку чисел."""

list_of_numbers = [5, 8, 5, 88, 45, 3, 12, 9]
def average(numbers):
    return sum(numbers)/len(numbers)

"""# task 5
  Написати функцію, яка повертає найдовше слово у списку."""

words = ['hello', 'meet', 'red', 'friend', 'by']

def longest_word(words):
    return max(words, key=len)

def check_single_occurence(words, value):
    return words.count(value) == 1



"""# task 8 (Homework 6.4): Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті"""

list_1 = [4, 7, 0, 6, 13, 9, 2, 20]

def is_even(n):
    return n % 2 == 0


"""# task 10 (Homework 6.2): Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі)."""


word = "hello"
word_2 = "friends"

def has_letter_h(word):
    return 'h' in word.lower()



"""# task 9 (Homework 6.3): Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1."""

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2=[]

def item(n):
    return isinstance(n, str)


"""# task 7 (Homework 6.1): Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False."""

uni_str = "54,67,42,59,46,70,22,86,11,38,65"
uni_str_1 = "1,3,5,7,8,6,3,15"

def list_unique(item):
    unique_set = set(item)
    return len(unique_set) > 10