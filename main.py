import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        before_time = time.time()
        function()
        after_time = time.time()
        print(f"{function.__name__} run speed: {after_time - before_time}")


def fast_function():
    for i in range(10000000):
        i * i


def slow_function():
    for i in range(100000000):
        i * i
