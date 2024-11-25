class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst[::-1]

    def __iter__(self):
        return iter(self.lst)

my_list = [1, 2, 3, 4, 5]
for item in ReverseIterator(my_list):
    print(item)

print(20*"_")

class EvenIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return iter(range(0, self.n + 1, 2))

for num in EvenIterator(10):
    print(num)