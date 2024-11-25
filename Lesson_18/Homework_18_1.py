def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)

print(20*"_")

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for num in fibonacci(21):
    print(num)