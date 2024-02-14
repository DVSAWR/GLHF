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


