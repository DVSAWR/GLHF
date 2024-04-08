import random

print('\n---- Пример использования lambda функции ----')

square = lambda a: a * a
print(square(5))

add = lambda a, b: a + b
print(add(5, 5))


def square(a):
    return a * a


print(square(2))


def add(a, b):
    return a + b


print(add(2, 2))

print('\n---- Пример lambda функции внутри обычной функции ----')


def add(a):
    return lambda b: a + b


add_to_100 = add(2)
print(add_to_100)
print(add_to_100(8))

print('\n---- Использование lambda функции в filter() ----')

lst = []

for i in range(10):
    lst.append(random.randint(1, 10))

print(lst)

filtered_lst = list(filter(lambda item: item % 2 == 0, lst))
print(filtered_lst)

filtered_lst_2 = list(filter(lambda item: item > 5, lst))
print(filtered_lst_2)

print('\n---- Использование lambda функции в map() ----')

print(lst)

mapped_lst = list(map(lambda item: item + 100, lst))
print(mapped_lst)
mapped_lst_2 = list(map(lambda item: item * item, lst))
print(mapped_lst_2)

print('\n---- Использование lambda функции в reduce() ----')

from functools import reduce

print(lst)

print(reduce(lambda a, b: a + b, lst))
print(reduce(lambda a, b: a * b, lst))

print('\nrealpython.com examples')
print('---- lambda function ----')

import dis

add = lambda x, y: x + y
print(type(add))
dis.dis(add)
print(add)

print('\n---- standart function ----')


def QWE(x, y): return x + y


print(type(QWE))
dis.dis(QWE)
print(QWE)

print('\n---- Single Expression ----')

print((lambda x: x % 2 and 'ODD' or 'EVEN')(2))
print((lambda x: x % 2 and 'ODD' or 'EVEN')(3))

print('\n---- Arguments ----')

example = (lambda x, y, z: x + y + z)(1, 2, 3)
print(example)
example = (lambda x, y, z=3: x + y + z)(1, 2)
print(example)
example = (lambda x, y, z=3: x + y + z)(1, y=2)
print(example)
example = (lambda *args: sum(args))(1, 2, 3)
print(example)
example = (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
print(example)
example = (lambda x, y=0, z=0: x + y + z)(1, y=2, z=3)
print(example)

print('\n---- Decorators ----')


def my_decorator(function):
    def wrapper(*args):
        print(f'FUNCTION: {function.__name__} <- FROM DECORATOR')
        return function(args)

    return wrapper


@my_decorator
def my_function(x):
    print(f'ARGS: {x}')


my_function('qwe', 'qwe')

print('\n----')


def trace(function):
    def wrapper(*args, **kwargs):
        print(f'\t[TRACE] \n\tFUNC: {function.__name__}, \n\tARGS: {args}, \n\tKWARGS: {kwargs}')
        return function(*args, **kwargs)

    return wrapper


@trace
def add_two(x): return x + 2


print(add_two(3))

print(trace(lambda x: x ** 2)(3))

print(list(map(trace(lambda x: x * 2), range(3))))

print('\n---- Closure ----')
