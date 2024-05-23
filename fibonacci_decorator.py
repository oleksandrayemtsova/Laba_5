import time


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print("The beginning of the generation of Fibonacci numbers")
        result = func(*args, **kwargs)
        print("The end of the generation of Fibonacci numbers")
        return result
    return wrapper


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Time to complete the task: ", time.time() - start)
        return result
    return wrapper


@logging_decorator
@time_decorator
def decorator_fibonacci(value1, stop=10):
    following_value = 1
    for _ in range(stop):
        number_fib = value1
        value1 = following_value
        following_value = number_fib + following_value
        print(number_fib)
    return ""


if __name__ == '__main__':
    present_value = 0
    for value in decorator_fibonacci(present_value, 10):
        print(value)
    for value in decorator_fibonacci(present_value, 100):
        print(value)
    for value in decorator_fibonacci(present_value, 1000):
        print(value)
