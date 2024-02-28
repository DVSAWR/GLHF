def preview(x):
    print(f'\n---- {x} ----')


preview('CREATING EMPTY CLASS')


class Dog:
    ...


print(Dog)

preview('CREATING AN OBJECT')
myobject = Dog()
print(myobject)

preview('__init__ METHOD')


class Dog:
    attr1 = 'Mammal'

    def __init__(self, name: str):
        self.name = name


Rodger = Dog('Rodger')
Tommy = Dog('Tommy')

print(Rodger)
print(f'Rodger.attr1 = {Rodger.attr1}')
print(f'Rodger.name = {Rodger.name}')

print(Tommy)
print(f'Tommy.attr1 = {Tommy.attr1}')
print(f'Tommy.name = {Tommy.name}')

preview('Creating Classes and objects with methods')


class Dog:
    attr1 = 'Mammal'

    def __init__(self, name: str):
        self.name = name

    def bark(self):
        print(f'* {self.name} bark *')


Rodger = Dog('Rodger')
Tommy = Dog('Tommy')
Rodger.bark()
Tommy.bark()

preview('INHERITANCE - НАСЛЕДОВАНИЕ')


class Person(object):

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(f'- {self.name}')
        print(f'- {self.idnumber}')

    def details(self):
        print(f'- {self.name}')
        print(f'- {self.idnumber}')


class Employee(Person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, idnumber)

    def details(self):
        print(f'- {self.name}')
        print(f'- {self.idnumber}')
        print(f'- {self.salary}')
        print(f'- {self.post}')


a = Employee('Rahul', 886012, 200000, 'Intern')

print('def display from Person():')
a.display()
print('\ndef details from Employee():')
a.details()


preview('POLYMORPHISM - ПОЛИМОРФИЗМ')


class Bird:
    def intro(self):
        print('Bird intro')

    def flight(self):
        print('Most of the birds can fly but some cannot')


class Sparrow(Bird):
    def flight(self):
        print('Sparrows can fly')


class Ostrich(Bird):
    def flight(self):
        print('Ostrich cannot fly')



obj_bird = Bird()
obj_spr = Sparrow()
obj_ostr = Ostrich()

print('\nobj_bird:', obj_bird)
obj_bird.intro()
obj_bird.flight()

print('\nobj_spr:', obj_spr)
obj_spr.intro()
obj_spr.flight()

print('\nobj_ostr:', obj_ostr)
obj_ostr.intro()
obj_ostr.flight()



preview('ENCAPSULATION - ИНКАПУСЛЯЦИЯ')


class Base:

    def __init__(self):
        self.x = '> self.x'
        self.__y = '> self.__y'


class Derived(Base):

    def __init__(self):
        Base.__init__(self)
        print(self.__y)



myobject = Base()
print(myobject)
print(myobject.x)

# RAISE AN ATTRIBUT EERROR
# print(myobject.y)
# myobject2 = Derived()
# print(myobject2.x)


preview('DATA ABSTRACTION - Абстракция данных')


class MyClass:
    __hiddenVariable = 0

    def add(self, increment):
        self.__hiddenVariable += increment
        print(f'__hiddenVariable: {self.__hiddenVariable}')


myobject = MyClass()
print('myobject.add(1) >>> ', end=' ')
myobject.add(1)
print('myobject.add(5) >>> ', end=' ')
myobject.add(5)

# AttributeError: 'MyClass' object has no attribute '__hiddenVariable'
# print(myobject.__hiddenVariable)

print(vars(myobject))



preview('CLASSES')
