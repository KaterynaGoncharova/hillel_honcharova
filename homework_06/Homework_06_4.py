lst_1 = input('Введіть список з чисел через пробіл: ')
numbers = [int(num) for num in lst_1.split()]
lst_2 = []
for number in numbers:
    if number % 2 == 0:
        lst_2.append(number)
if lst_2:
    res = sum(lst_2)
    print(f'Сума парних чисел = {res}')
else:
    print('Введіть хоч одне парне число')

