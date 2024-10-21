numbers = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
def calculate_sum(string):
    try:
        num_list = [int(num) for num in string.split(',')]
        return sum(num_list)
    except ValueError:
        return "Не можу це зробити"

for num_string in numbers:
    print(calculate_sum(num_string))


