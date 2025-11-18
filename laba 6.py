from functools import wraps

def count_calls(func):
    count = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функція {func.__name__} викликана {count} разів")
        return func(*args, **kwargs)
    return wrapper

@count_calls
def say_hello():
    print("Привіт!")

say_hello()
say_hello()
say_hello()
say_hello()
say_hello()