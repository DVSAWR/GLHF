print('\n---- Процедурное программирование ----')


def greet(name):
    print(f'Hello, {name}!')


name = 'QWE'
greet(name)

print('\n---- Объектно-ориентированное программирование (ООП) ----')

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must impliment this method')

class Dog(Animal):
    def speak(self):
        return '>>> Woof'

class Cat(Animal):
    def speak(self):
        return '>>> Meow'

dog = Dog('Belca')
print(dog.name)
print(dog.speak())


print('\n---- Императивное программирование ----')

numbers = [1, 2, 3, 4, 5]
add = 0
for i in numbers:
    add += i
print('SUM:', add)

print('\n---- Функциональное программирование ----')

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda i: i ** 2, numbers))
print(squares)
even_numbers = list(filter(lambda i: i % 2 == 0, numbers))
print(even_numbers)