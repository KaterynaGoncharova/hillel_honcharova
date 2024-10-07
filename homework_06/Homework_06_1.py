my_list = input('Введіть список змінних:')

unique_item = set(my_list)
unique_count = len(unique_item)

if unique_count > 10:
    print(True)
else:
    print(False)