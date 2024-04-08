print('\n---- Декоратор ----')


def decorator(call):
    def wrapper(*args, **kwargs):
        r = call(*args, **kwargs)
        return r

    return wrapper


def call(a: int) -> str:
    return str(a)


decorated_call = decorator(call)
print(decorated_call(1) == '1')

print('---- Сокращение ----')


@decorator
def call(a: int) -> str:
    return str(a)


print(call(1) == '1')

print('---- Использование functools wraps ----')

from functools import wraps


# Эта функция копирует всю служебную метаинформацию о декорируемой функции в функцию-декоратор
# (название функции, докстринги, список входящих аргументов, их типы и тд).

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def call(a: int) -> str:
    return str(a)


decorated_call = decorator(call)
print(decorated_call(1) == '1')

print('---- Декоратор с параметрами ----')


def decorator_wrapper(arg1, arg2):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return real_decorator


@decorator_wrapper(1, 2)
def func(): ...


print('\ngeeksforgeeks.org examples')
print('---- Treating the functions as objects ----')


def shout(text: str):
    return text.upper()


print(shout('qwe'))

smth = shout
print(smth('qwe'))

print('---- Passing the function as an argument ----')


def shout(text: str):
    return text.upper()


def whisper(text: str):
    return text.lower()


def greet(function):
    greeting = function('Hello, I am Qwe')
    print(greeting)


greet(shout)
greet(whisper)

print('---- Returning functions from another function ----')


def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(10)
print(add_15(10))

print('---- Decorator can modify the behaviour ----')


def hello_decorator(function):
    def smth():
        print('\t> BEFORE FUNCTION EXECUTION')
        function()
        print('\t> AFTER FUNCTION EXECUTION')

    return smth


@hello_decorator
def call():
    print('my function')


# hello_decorator(call)
call()

print('---- The execution time of a function ----')

import time
import math


def calculate_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        time.sleep(1)

        function(*args, **kwargs)

        end_time = time.time()

        print(f'\tFUNCTION: {function.__name__} TIME: {end_time - start_time}')

    return wrapper


def my_function(number):
    print(math.factorial(number))


my_function(10)
my_function_with_decorator = calculate_time(my_function)
my_function_with_decorator(10)

print('---- Chaining Decorators ----')


def decorator_1(function):
    def wrapper():
        x = function()
        return x * x

    return wrapper


def decorator_2(function):
    def wrapper():
        x = function()
        return x + x

    return wrapper


@decorator_1
@decorator_2
def number_1():
    return 5


@decorator_2
@decorator_1
def number_2():
    return 5


print(number_1())
print(number_2())
