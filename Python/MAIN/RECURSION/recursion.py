from timeit import timeit
from functools import reduce

def preview(x):
    print(f'\n---- {x} ----')


preview('RECURSION')
print()


def print_recursion(test):
    if (test < 1):
        return
    else:
        print(test, end=' ')
        print_recursion(test - 1)
        print(test, end=' ')
        return


test = 3
print_recursion(test)

print('\n')


def fib(n):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


n = 5
for i in range(0, n):
    print(fib(i), end=' ')

preview('REAL Python.com')
print('')

preview('count down to zero')


def countdown(n):
    print(n)
    if n == 0:
        print('Treminate recursion')
        return
    else:
        countdown(n - 1)


countdown(5)
print('')


def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)


countdown(5)
print('')


def countdown(n):
    while n >= 0:
        print(n)
        n -= 1


countdown(5)
print('')

preview('calculate factorial')


# n! = 1 * 2 * ... * n


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


print(factorial(4), '\n')


def factorial_print(n):
    print(f'factorial(n) called with n = {n}')
    return_value = 1 if n <= 1 else n * factorial_print(n - 1)
    print(f'-> factorial({n}) returns {return_value}')
    return return_value

print(factorial_print(5))

print('')
preview('SPEED COMPARSION')
n = 1000000
print(f'for {n} times')

setup_string = '''
print('Recursive:', end=' ')
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
'''

print(timeit('factorial(4)', setup=setup_string, number=n))

setup_string = '''
print('Itreative:', end=' ')
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value
'''

print(timeit('factorial(4)', setup=setup_string, number=n))

setup_string = '''
from functools import reduce
print('reduce():', end=' ')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
'''

print(timeit('factorial(4)', setup=setup_string, number=n))

setup_string = '''
from math import factorial
print('math factorial():', end=' ')
'''

print(timeit('factorial(4)', setup=setup_string, number=n))






