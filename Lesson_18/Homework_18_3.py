def log_args_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Args: {args}, Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_args_and_result
def add(a, b):
    return a + b

add("red", "bull")

print(20*"_")

def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
    return wrapper

@catch_exceptions
def divide(a, b):
    return a / b

divide(10, 2)
divide(10, 0)