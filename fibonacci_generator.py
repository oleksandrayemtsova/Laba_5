def fibonacci_generator(stop=10):
    present_value, following_value = 0, 1
    for _ in range(stop):
        number_fib = present_value
        present_value, following_value = following_value, present_value + following_value
        yield number_fib


if __name__ == '__main__':
    print("The first 10 digits of Fibonacci:")
    for number in fibonacci_generator():
        print(number)
    print("The first 100 digits of Fibonacci:")
    for number in fibonacci_generator(100):
        print(number)
    print("The first 1000 digits of Fibonacci:")
    for number in fibonacci_generator(1000):
        print(number)
