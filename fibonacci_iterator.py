from collections.abc import Iterator


class FibonacciIterator(Iterator):
    def __init__(self, stop=10):
        self.__stop = stop
        self.__number = 0
        self.__present_value = 0
        self.__following_value = 1

    @property
    def stop(self):
        return self.__stop

    @stop.setter
    def stop(self, stop):
        if type(stop) == int:
            self.__stop = stop
        else:
            print("Stop must be an integer!")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if type(number) == int:
            self.__number = number
        else:
            print("Number must be an integer!")

    @property
    def present_value(self):
        return self.__present_value

    @present_value.setter
    def present_value(self, present_value):
        if type(present_value) == int:
            self.__present_value = present_value
        else:
            print("Present value must be an integer!")

    @property
    def following_value(self):
        return self.__following_value

    @following_value.setter
    def following_value(self, following_value):
        if type(following_value) == int:
            self.__following_value = following_value
        else:
            print("Following value must be an integer!")

    def __next__(self):
        if self.number < self.stop:
            self.number += 1
            fib_number = self.present_value
            self.present_value, self.following_value = self.following_value, self.present_value + self.following_value
            return fib_number
        else:
            raise StopIteration


if __name__ == '__main__':
    print("The first 10 digits of Fibonacci:")
    for value in FibonacciIterator():
        print(value)
    print("The first 100 digits of Fibonacci:")
    for value in FibonacciIterator(100):
        print(value)
    print("The first 1000 digits of Fibonacci:")
    for value in FibonacciIterator(1000):
        print(value)
