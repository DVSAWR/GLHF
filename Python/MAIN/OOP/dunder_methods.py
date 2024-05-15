from math import trunc, ceil, floor
from random import choice


def preview(x):
    print(f'\n---- `{x}` ----')


preview('__new__()')
# создание нового экземпляра класса


class SomeClass:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print('> __new__(cls, *args, **kwargs) >')
        return instance

    def __init__(self, val):
        self.val = val


a = SomeClass(7)
print(a.val)

print('\nrandom choice create class object')


class Pet():

    def __new__(cls, *args, **kwargs):
        other = choice([Dog, Cat, Shark])
        instance = super().__new__(other)
        print(f'Class {type(instance).__name__} object')
        return instance

    def __init__(self):
        print('Class Pet() not launch')


class Dog:
    def communicate(self):
        print('~~~ Woof\n')


class Cat:
    def communicate(self):
        print('~~~ Meow\n')


class Shark:
    def communicate(self):
        print('~~~ SH-a-a-a-aaa\n')


pet1 = Pet()
pet1.communicate()
print('Pet -', end=' ')
print(isinstance(pet1, Pet))
print('Dog -', end=' ')
print(isinstance(pet1, Dog))
print('Cat -', end=' ')
print(isinstance(pet1, Cat))
print('Shark -', end=' ')
print(isinstance(pet1, Shark))

print('\n')
pet2 = Pet()
pet2.communicate()
print('Pet -', end=' ')
print(isinstance(pet2, Pet))
print('Dog -', end=' ')
print(isinstance(pet2, Dog))
print('Cat -', end=' ')
print(isinstance(pet2, Cat))
print('Shark -', end=' ')
print(isinstance(pet2, Shark))

print('\n')
pet3 = Pet()
pet3.communicate()
print('Pet -', end=' ')
print(isinstance(pet3, Pet))
print('Dog -', end=' ')
print(isinstance(pet3, Dog))
print('Cat -', end=' ')
print(isinstance(pet3, Cat))
print('Shark -', end=' ')
print(isinstance(pet3, Shark))

print('\n')


class Something:

    def __new__(cls, *args, **kwargs):
        print(f'> construct: {args} | {kwargs}')

        instance = super().__new__(cls)

        instance.new_attribute = '> DONE'

        print('> almost done')

        return instance

    def __init__(self, *args, **kwargs):
        print(f'> initialize: {args} | {kwargs}')
        print(self.new_attribute)


myobject = Something('QWE', other=10)

print(myobject.new_attribute)

preview('__init__()')
# инициализация класса, присваивание начальных значений атрибутов класса


class Car:

    def __init__(self, color):
        self.color = color


myobject = Car('yellow')
print(myobject)
print(myobject.color)

preview('__del__()')
# деструктор, уничтожает экземпляр пользовательского типа


class MyClass:
    def __init__(self, name):
        print('> inside constructor')
        self.name = name
        print('> object initialized')

    def show(self):
        print(self.name)

    def __del__(self):
        print('> inside destructor')
        print('> object destroyed')


myobject = MyClass('QWE')
myobject.show()

del myobject
del MyClass

preview('__trunc__(self)')
# реализует поведение math.trunc() - округляет число до ближайщего целого числа к нулю



print(trunc(-5.23))
print(trunc(-5.999))


class MyClass:
    def __init__(self, num):
        self.num = num

    def __trunc__(self):
        return trunc(self.num)


print('')
myobject = MyClass(3.239)
print(myobject.num)
print(myobject.__trunc__)
print(myobject.__trunc__())
