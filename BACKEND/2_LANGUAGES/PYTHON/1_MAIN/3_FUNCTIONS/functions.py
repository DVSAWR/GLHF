import re


def preview(x):
    print(f'\n---- {x} ----')


preview('abs()')

complex_number = (3 + 10j)
abs_complex_number = abs(complex_number)
print(f"Абсолютное значение {complex_number} это {abs_complex_number}")
print(complex(complex_number.real))
print(complex(complex_number.imag))

x = 42.42
abs_x = abs(x)
print(f"Абсолютное значение {x} это {abs_x}")
x = -42.42
abs_x = abs(x)
print(f"Абсолютное значение {x} это {abs_x}")

preview('all()')
print(all([True, True, True]))
print(all([True, False, True]))

num1 = [1, 2, 3, 4, 5, 6, 7]
num2 = [1, 2.0, 3.1, 4, 5, 6, 7.9]
print(all([type(x) is int for x in num1]))
print(all([type(x) is int for x in num2]))

preview('any()')
num1 = range(0, 20, 2)
num2 = range(0, 15, 2)
print(any([x > 15 for x in num1]))
print(any([x > 15 for x in num2]))

preview('ascii()')
line = 'My name is Даниил'
x = ascii(line)
print(x)

preview('bin()')
# Преобразует целое число в двоичную строку
print('bin(123)=', bin(123))

preview('bool()')
# Позволяет проверить/узнать логическое значение объекта
print('bool(1) =', bool(1))
print('bool(0) =', bool(0))

preview('breakpoint()')
# Обозначает точку останова и выполняет функцию отладчика кода
print("x = 10 y = 'Hi' z = 'Hello' print(y) breakpoint() print(z) "
      "Когда мы запустим этот скрипт, встретив точку останова в коде "
      "интерпретатор затормозит процесс исполнения, открыв консоль "
      "отладчика PDB, что позволит нам детально разобраться в "
      "происходящем. Чтобы прервать PDB-сессию и продолжить выполнение "
      "скрипта, нажмите C и Enter.")

preview('bytearray()')
# Преобразует объект в изменяемый байтовый массив
print('bytearray(4) =', bytearray(4))
print('bytearray("Привет", encoding="utf-8" =', bytearray("Привет", encoding="utf-8"))

preview('bytes()')
# Преобразует объект в неизменяемую строку байтов
print('bytes(4) =', bytes(4))
print('bytes("Привет", encoding="utf-8" =', bytes("Привет", encoding="utf-8"))

preview('callable()')


# Проверяет, является ли объект вызываемым
class MyClass:
    def __call__(self, *args, **kwargs):
        print('called')


print('callable(MyClass()) =', callable(MyClass()))

print('callable(5) =', callable(5))

preview('chr()')
# Преобразует число в символ Юникода, обратная операция ord()
print("ord('q') =", ord('q'))
print("chr(113) =", chr(113))

lst = []
for i in range(49, 58):
    lst.append(chr(i))
print(lst)

preview('classmethod()')


# Позволяет преобразовать обычный метод в метод класса
class MyClassMethod():

    @classmethod
    def method(cls, arg):
        print(f'{cls.__name__}.method = {arg}')


print('class :')
MyClassMethod.method('qwe')

mcm_obj = MyClassMethod()
print('\nobject:')
mcm_obj.method('zxc')

preview('compile()')
# Позволяет скомпилировать блок кода для выполнения в exec()
x = compile('x = 1\nz = x + 5\nprint(z)', 'test', 'exec')
exec(x)
y = compile('print("4 + 5 =", 4 + 5)', 'test', 'eval')
eval(y)

preview('complex()')
# Создает/преобразовывает число/строку в комплексное число
print(complex())
print(complex(1.5))
print(complex('          1+2j'))

preview('delattr()')


# Позволяет удалить атрибут по имени указанного объекта
class MyObject:
    name = 'NAME'
    phone = '12345'


print(dir(MyObject)[-2:])
delattr(MyObject, 'phone')
print(dir(MyObject)[-2:])

preview('dict()')
# Создание словаря Python из ключевых аргументов/итерируемого объекта
x = dict(q=1, w=2, e=3)
print(x)

x = dict(zip([i for i in range(4)], [i for i in range(4)]))
print(x)

x = 'qwe asd zxc'
d = {k: v for k, v in zip(x.split(), range(4))}
print(d)

preview('dir()')


# Возвращает список допустимых атрибутов объекта
class MyObject:
    name = 'NAME'
    phone = '12345'


print(dir(MyObject)[-2:])
delattr(MyObject, 'phone')
print(dir(MyObject))

preview('divmod()')
# Производит деление чисел с остатком
print(divmod(101, 25))

seconds = 50000
minutes, seconds = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)
print(f'\n h = {hours}, m = {minutes}, s = {seconds}')

preview('enumerate()')


# Счетчик элементов последовательности в циклах

def notenumerate(seq, start=0):
    n = start
    for element in seq:
        yield n, element
        n += 1


seq = list('qwe')
for i, v in enumerate(seq, 1):
    print(f'{i} = {v}')

print('')

for i, v in notenumerate(seq, 1):
    print(f'{i} = {v}')

print('')

seasons = 'Spring Summer Fall Winter'.split()
print(list(enumerate(seasons)))

preview('eval()')
# Позволяет выполнить строку-выражение с кодом на Python

eval('print("HELLO WORLD")')
eval('print("Q WE".split())')

preview('exec()')
# Позволяет динамически выполнить блок кода Python

x = ('x = {k: v for k, v in zip("qwe asd zxc".split(), range(3))}\n'
     'print(x)')
exec(x)

x = ('print(5+10**2)')
exec(x)

preview('filter()')
# Позволяет отфильтровать элементы последовательности по условию

lst = [0, 1, False, 2, '', 3, 'a', 's', 34, 1.22]
print(lst)
print('filter(None, lst) =', list(filter(None, lst)))

print(list(filter(lambda i: type(i) is int, lst)))


def morethensix(x):
    if x > 6:
        return True
    else:
        return False


print('')
lst = range(15)
print(lst)
print(list(filter(morethensix, lst)))

preview('float()')
# Преобразует число/строку с записью числа в вещественное число
print(float(4))
print(float('   3.22'))

preview('format()')
# Форматирует значение переменной для вывода на печать

print(format(5, '.1f'))
print(format(5, '*^10.2f'))
print(format(5000.413, '~>+15,.2f'))

preview('frozenset()')
# Преобразует строку или последовательность в неизменяемое множество

x = frozenset('abracadabra')
print(x)

preview('getattr()')


# Позволяет получить значение атрибута объекта по его имени


class MyObj:
    name = 'Qwe'
    phone = '123'
    country = 'RU'


print(MyObj.phone)

x = getattr(MyObj, 'phone')
print(x)

delattr(MyObj, 'phone')

x = getattr(MyObj, 'phone', 1)
print(x)

preview('globals()')
# Возвращает словарь переменных глобальной области видимости

x = globals()
print(x['__file__'])

XS = 0


def myfunc():
    x = globals()
    x['XS'] = 1


print(XS)

myfunc()
print(XS)

preview('hasattr()')


# Проверяет наличие атрибута объекта


class MyObj:
    name = 'Qwe'
    phone = '123'
    country = 'RU'


x = hasattr(MyObj, 'name')
y = hasattr(MyObj, 'name2')

print(x)
print(y)

preview('hash()')
# Получает и возвращает хэш-значение объекта

print(hash(1))
print(hash(1.0))
print(hash('1'))
print(hash((1, 2, 3)))

preview('help()')
print(help(hash))

print(lst[1])
print(x)

preview('hex()')
# Преобразовывает число в шестнадцатеричную строку

print(hex(1))
print(hex(255))

preview('id()')
# Возвращает уникальный идентификатор объекта в программе

x = 'qwe asd zxc'.split()
print(f'id({x}) = {id(x)}')
print('')

for i in x:
    print(f'id({i}) = {id(i)}')

preview('input()')
# Позволяет производить ввод данных в консоли


preview('int()')
# Позволяет преобразовать число или строку с числом в тип int

a = int(3.5486253092)
b = int('3     ')
d = int('0xff', base=16)

print(a, b, d)

preview('isinstance()')


# Позволяет проверить принадлежность экземпляра к классу

class Base:
    def __init__(self):
        self.name = 'name'


class SubBase(Base):
    def __init__(self):
        super().__init__()


myobj = Base()
mysubobj = SubBase()

print(isinstance(myobj, Base))
print(isinstance(myobj, SubBase))
print('')
print(isinstance(mysubobj, Base))
print(isinstance(mysubobj, SubBase))
print('')
print(issubclass(type(mysubobj), Base))

preview('issubclass()')


# Позволяет проверить является ли класс унаследованым

class A:
    ...


class B(A):
    ...


class C:
    ...


print(issubclass(B, A))
print(issubclass(A, B))
print('')
print(issubclass(B, (A, C)))

preview('iter()')
# Создает итератор из последовательности

x = iter('qwe asd zxc'.split())
print(next(x))
print(next(x))
print(next(x))

print('')


class MyIterClass(object):
    def __init__(self):
        self.index = 0
        self.items = [1, 2, 3, 4]

    def __call__(self, *args, **kwargs):
        value = self.items[self.index]
        self.index += 1
        return value


x = iter(MyIterClass(), 4)

print(next(x))
print(next(x))
print(next(x))

preview('len()')
# Количество элементов в последовательности или коллекции


print(len('qwe asd zxc'.split()))
print(len('qwe asd zxc'))

mylist = 'qwe asd zxc'.split()

for i in range(len(mylist)):
    print(f'{i} = {mylist[i]}')

print('')

for i, item in enumerate(mylist):
    print(f'{i} = {item}')

preview('list()')
# Создает пустой список или преобразовывает последовательность в список

mylist = 'qwe asd zxc'.split()
myset = set(mylist)
mytuple = tuple(mylist)
mydict = {k: v for k, v in zip(mylist, range(len(mylist)))}

print(mylist, myset, mytuple, mydict)
print(list(mylist), list(myset), list(mytuple), list(mydict))

preview('locals()')
# Возвращает словарь с переменные и их значениями локальной области видимости
x = 1


def myfunc(one=1):
    two = 2
    print(locals())


three = 3

myfunc()

preview('map()')
# Применяет определенную функцию к каждому элементу в последовательности


x = [1, 2, 3]
y = [3, 3, 3]

print(list(map(pow, x, y)))


def myfunc(a, b, c):
    return a * b * c


x = list(map(myfunc, [1, 2, 3], [1, 2, 3], [1, 2, 3]))
print(x)


def textclean(word):
    return re.sub(r"[`!?.:;,'\"()-]", '', word.strip())


print('')
text = ('QWE?? Qwe) `!qWe :qwE ""qwe')
word = text.split()
print(word)
word = map(textclean, word)
print(word)
text = ' '.join(word)
print(text)

preview('max()')
# Находит максимальное значение элемента в последовательности

x = ['1', '2', '33', '4']
print(max(x))
print(max(x, key=lambda i: int(i)))
print(max([1, 2, 3, 4, 10], [10, 20], key=sum))

x = list('abcdifgh')
print(max(x))

print('')

print(max(5, 2, 3))
print(max([1.2, 1.3, 1.5, 2, 5.52]))
x = (1.2, 1.3, 1.5, 2, 5.52)
print(max(5, 2, 3, *x))

preview('memoryview()')
# Создает ссылку на объект в памяти

x = memoryview(b'abcd')
print(x[0])
print(x[1])
print(x[2])
print(x)
print(x[1:-2])

preview('min()')
# Возвращает минимальное значение элемента последовательности

x = ['1', '2', '33', '4']
print(min(x))
print(min(x, key=lambda i: int(i)))
print(min([1, 2, 3, 4, 10], [10, 20], key=sum))

x = list('abcdifgh')
print(min(x))

print('')

print(min(5, 2, 3))
print(min([1.2, 1.3, 1.5, 2, 5.52]))
x = (1.2, 1.3, 1.5, 2, 5.52)
print(min(5, 2, 3, *x))

preview('next()')
# Позволяет получить следующий элемент итератора

myiter = iter('qwe asd zxc'.split())
print(next(myiter, '- end of iter()'))
print(next(myiter, '- end of iter()'))
print(next(myiter, '- end of iter()'))
print(next(myiter, '- end of iter()'))
print(next(myiter, 'end of iter()'))

preview('object()')
# Является базой для всех классов

obj = object()
print(obj)
print(dir(obj)[0:4], '= dir(obj)[0:4]')

preview('oct()')
# Преобразует число в восьмеричную строку
print(oct(1))
print(oct(4))
print(oct(8))
print(oct(16))

preview('open()')
# Открывает файл для чтения или записи файлового потока

f = open('open.txt', 'r')
print(f)

print('')
lst = ''
for i in f:
    lst += i

print(lst)
f.close()

print('')
with open('open.txt', 'a') as f:
    f.write('new line from functions.py\n')

preview('ord()')
# Возвращает число символа Unicode

print(ord('a'))
print(ord('_'))
print(ord('\u2020'))
print(ord('\n'))
print(ord('\t'))

preview('pow()')
# Возведения числа в степень

print(pow(2, 2))
print(pow(2, 3))
print(pow(2, -2))
print(pow(2, -3.5))

preview('print()')
# Выводит переданные объекты в текстовый поток

print('print("Hello world")')

preview('property()')


# Легкое создание дескрипторов данных в Python

class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property")


c = C()
c.x = 'new value'
y = c.x
print(y)


class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def delx(self):
        del self._x


c = C()
c.x = 'new value x.setter'
print(c.x)


class Volt:
    def __init__(self):
        self._voltage = 10000

    @property
    def voltage(self):
        return self._voltage


v = Volt()
x = v.voltage
print(x)

preview('range()')
# Позволяет создавать последовательности чисел с заданным шагом

print(list(range(10)))
print(list(range(1, 11)))
print(list(range(0, 30, 5)))
print(list(range(0, -10, -1)))

lst = []
for i in range(0, 17, 2):
    n = round(i / 10, 2)
    lst.append(n)

print(lst)

preview('repr()')


# Позволяет получить описание объекта

class MyClass:
    name = 'QWE'


x = MyClass()
print(repr(x))


class MyClass:
    name = 'QWE'

    def __repr__(self):
        return repr(self.name)


x = MyClass()
print(repr(x))

preview('reversed()')
# Возвращает элементы последовательности в обратном порядке

x = list(range(10))

print(x)
print(list(reversed(x)))

print('')
x = 'FRWL'

for i in reversed(x):
    print(i, end='')
print('')
print(x)

preview('round()')
# Позволяет округлить число до заданной точности

print(3.141592)
print(round(3.141592))
print(round(3.141592, 1))
print(round(3.141592, 2))
print(round(3.141592, 3))
print(round(3.141592, 4))

preview('set()')
# Создает множество или преобразовывает последовательность в множество

x = 'qwe Qwe qwe Q'
print(x)
print(set(x))
print(set(x.split()))
print(set(range(10)))

x = ('QWE', 1, 1, 2, (3.14, 3.15), 1)

print(set(x))

preview('setattr()')


# Устанавливает атрибут объекта по имени


class MyClass:
    name = 'Qwe'
    number = '123'


setattr(MyClass, 'number', '999')
setattr(MyClass, 'newattr', '1')

x = MyClass()
s = getattr(x, 'number', '999')
c = x.newattr

print(x)
print(s, c)

preview('slice()')
# Шаблон среза, который можно применить к последовательности

x = 'slice'
y = x[::-1]
print(x, y, sep=' === ')

x = 'slice'
y = x[slice(None, None, -1)]
print(x, y, sep=' === ')

preview('sorted()')
# Выполняет сортировку последовательности по возростанию/убыванию

line = 'ASD asd ZXC zxc'
x = sorted(line.split())
print(x)
x = sorted(line.split(), key=str.lower)
print(x)

print('')
student = [
    ('name', 'A', 15),
    ('name', 'B', 13),
    ('name', 'C', 14),
]

x = sorted(student, key=lambda student: student[2])
print(x)
x = sorted(student, key=lambda student: student[1])
print(x)

print('')

class MyClass:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student = [
    MyClass('name', 'A', 15),
    MyClass('name', 'A', 13),
    MyClass('name', 'B', 14),
]

x = sorted(student, key=lambda student: student.age)
print(x)
x = sorted(student, key=lambda student: student.grade)
print(x)


preview('staticmethod()')
# Преобразует метод класса в статический метод этого класса

class MyClass:
    def method(self):
        return 'instance method calles', self

    @staticmethod
    def mysstaticmethod():
        return 'static method called'


obj = MyClass()
print(obj.method())
print(obj.mysstaticmethod())


print('')


class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year


    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('.'))
        rdate = cls(day, month, year)
        return rdate

    @staticmethod
    def is_date_valid(date_as_string):
        if date_as_string.count('.') == 2:
            day, month, year = map(int, date_as_string.split('.'))
            return day <= 31 and month <= 12 and year <= 2099


    def string_to_db(self):
        return f'{self.year}-{self.month}-{self.day}'




dates = [
    '30.12.2020',
    '30-12-2020',
    '01.01.2021',
    '12.31.2020',
]

for i in dates:
    if Date.is_date_valid(i):
        date = Date.from_string(i)
        string_to_db = date.string_to_db()
        print(string_to_db)
    else:
        print(f'wrong date format')


preview('str()')
# Получает строковую версию объекта

x = 10

print(f'{x} = {type(x)}')
print(f'{str(x)} = {type(str(x))}')


preview('sum()')
# Вычисляет сумму всех элементов в последовательности

x = ('01.01.1960qev QWE')
print(list(x))
lst = []
for i in list(x):
    if i.isdigit():
        lst.append(int(i))
    else:
        continue
print(lst)
print(sum(lst))

print(list(range(10)))
print(sum(range(10)))


preview('super()')
# Обеспечивает доступ к оригиналам наследованных методов

class A:
    def method(self):
        print('method class A')


class B(A):
    def method(self):
        super().method()
        print('method class B')


x = B()
print('x.method()')
x.method()


preview('tuple()')
# Создает кортеж или преобразует последовательность в кортеж

print(tuple('QWE'))
print(tuple(range(0, 25, 4)))
print(tuple({'Q': 1, 'F': 2}))


preview('type()')
# Возвращает тип объекта и является собственным метаклассом языка Python

print(type('1'))
print(type(1))
print(type(1.0))
print(type(complex(1)))
print(type([1, 0]))
print(type((1, 0)))
print(type({1: 0}))
print(type({1, 2, 3}))
print(type(bytes(1)))
print(type(bytearray([1, 2, 3])))


preview('vars()')
# Возвращает словарь пространства имен объекта

class MyObject:
    name = 'Q'
    phone = '13'
    country = 'RU'
    age = '9'

x = vars(MyObject)
for i, v in x.items():
    print(i, '=', v)


preview('zip()')
# Объединяет элементы последовательностей в список кортежей

x = zip([1, 2, 3], ['Q', 'W', 'E'])
print(x)

for i in x:
    print(i)


print(list(zip(range(3), range(100))))

print('strict=True == zip(len==len)')


x = list(range(3))
y = list(range(3))
print(list(zip(x, y)))

x2, y2 = zip(*zip(x, y))
print(x2)
print(y2)
print(list(zip(x2, y2)))


print('')
nums = list(range(4))
nums2 = list(range(4, 8))
names = 'zero one two three'.split()

print(nums, nums2, names)

for i in range(len(nums)):
    a, b, c = nums[i], nums2[i], names[i]
    print(f'{a} - {b} - {c}')

print('\nzip')

for a, b, c in zip(nums, nums2, names):
    print(f'{a} - {b} - {c}')


print('')

print(dict(zip(names, nums)))

print('')
x = {k: v for k, v in zip(names, nums)}
y = {k: v for v, k in zip(names, nums)}

print(x, '\n', y)

print('')
x = {'zero': 0, 'one': 1, 'two': 2, 'three': 3}
y = tuple(x.items())

print(x, '\n', y)

rd = {k: v for v, k in y}
print(f'\n{x}\n{rd}')

print('')
d = {k: v for k, v in zip('QWE ASD ZXC'.split(), range(3))}
print(d)
rd = {k: v for v, k in tuple(d.items())}
print(rd)

print(tuple(d.items()))

