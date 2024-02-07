def preview(x):
    print(f'\n---- str.{x} ----')


x = 'Что ТАКОЕ LOREM Ipsum?'
print(f'str = {x}')

preview('capitalize()')

print(x.capitalize())
# Переводит первый символ/букву строки в верхний регистр
preview('casefold()')

print(x.casefold())
# Сворачивает регистр строки
preview('center()')

print(x.center(len(x)+20, '_'))
# Производит выравнивание текста в строке по центру
preview('count()')

print(x.count('O'))
print(x.count('O', 2))
print(x.count('O', 2, 5))

preview('encode()')
# Преобразует текстовую строку в байтовую строку
print(x.encode('utf-8'))
print(x.encode('ascii', errors='replace'))

preview('endswitch()')
# Поиск строк с заданным суффиксом/окончанием
print(x.endswith('?'))
print(x.endswith('Ipsum'))

y = ('m', '?')
for i in x[16:]:
    print('YES', i) if i.endswith(y) else print('NO', i)

preview('expandtabs()')
# Производит замену табуляции пробелами
y = '01\t012\t0123\t01234'
print(y.expandtabs())
print(y.expandtabs(4))

preview('find()')
# Возвращает наименьший индекс совпадения подстроки в строке
print(x.find('Что'))
print(x.find('Что', 3, 10))

preview('format()')
# Возвращает копию строки, в которой каждое замещающее поле заменяется строковым значением соответствующего аргумента
print('{0} {1} {1} {0}'.format('a', 'b'))
y = {'a': '0', 'b': '1'}
print('{a} {b} {b} {a}'.format(**y))

preview('format_map()')
# Возвращает копию строки, в которой каждое замещающее поле заменяется строковым значением соответствующего аргумента
...

preview('index()')
# Возвращает индекс первого совпадения начала подстроки
print(x.index('Что'))
print(x.index('L'))

preview('isalnum()')
# Проверяет, что строка состоит только из цифр и буквенных символов
print(f'{x} = {x.isalnum()}')
print(f'{x[10:15]} = {x[10:15].isalnum()}')

preview('isalpha()')
# Проверяет, что строка состоит только из буквенных символов
print(f'{x} = {x.isalpha()}')
print(f'{x[10:15]} = {x[10:15].isalpha()}')

preview('isascii()')
# Проверяет, что все символы в строке являются символами ASCII
print(f'{x} = {x.isascii()}')
print(f'{x[10:15]} = {x[10:15].isascii()}')

preview('isdecimal()')
# Проверяет, что все символы строки являются десятичными
y = '0123456789'
print(f'{y} = {y.isdecimal()}')
y = '10.5'
print(f'{y} = {y.isdecimal()}')
y = '10 5'
print(f'{y} = {y.isdecimal()}')
y = 'LOREM'
print(f'{y} = {y.isdecimal()}')

preview('isdigit()')
# Проверяет, что все символы в строке это цифры
y = '0123456789'
print(f'{y} = {y.isdigit()}')
y = '0123456789 qwe??'
print(f'{y} = {y.isdigit()}')

preview('isidentifier()')
# Возвращает True, если строка str является допустимым идентификатором в соответствии с определением языка
y = 'isidentifier()'
print(f'{y} = {y.isidentifier()}')
y = 'isidentifier'
print(f'{y} = {y.isidentifier()}')
y = 'my-.func?'
print(f'{y} = {y.isidentifier()}')
y = 'my_func'
print(f'{y} = {y.isidentifier()}')

preview('islower()')
# Определяет, что все символы в строке имеют нижний регистр
print(f'{x} = {x.islower()}')
print(f'{x[-5:-1]} = {x[-5:-1].islower()}')

preview('isnumeric()')
# Определяет, что в строке находятся только числовые символы
y = '0123456789'
print(f'{y} = {y.isnumeric()}')
y = '0123456789 qwe??'
print(f'{y} = {y.isnumeric()}')
y = '⅓'
print(f'{y} = {y.isnumeric()}')

preview('isprintable()')
# Определяет, что все символы в строке доступны для печати/вывода
print(f'{x} = {x.isprintable()}')
print(''.isprintable())

preview('isspace()')
# Определяет, что строка состоит только из пробельных символов
y = 'Q1   2we'
print(f'{y} = {y.isspace()}')
y = '        '
print(f'{y} = {y.isspace()}')

preview('istitle')
# Проверяет, что первая буква каждого слова заглавная
print(f'{x.lower()} = {x.lower().istitle()}')
y = x.title()
print(f'{y} = {y.istitle()}')

preview('isupper()')
# Проверяет, что все символы строки находятся в верхнем регистре
print(f'{x} = {x.isupper()}')
y = x.upper()
print(f'{y} = {y.isupper()}')

preview('join()')
# Создает строку из списка строк
y = list(x[16:])
print(f'{y}')
z = ''.join(y)
print(z)
z = ' '.join(y)
print(z)
z = '\t'.join(y)
print(z)

preview('ljust()')
# Выравнивает текст в строке по левому краю
print(x.ljust(len(x)+20, '_'))

preview('lower()')
# Переводит строку в нижний регистр
print(x)
print(x.lower())

preview('lstrip()')
# Удаляет символы в начале строки. Обрезает начало строки
print(x.lstrip())
print(x.lstrip('Что '))
print(x.lstrip('Что ТАКОЕ'))

preview('maketrans()')
# Создает таблицу преобразования символов для метода str.translate()
y = {'q': '0', 'w': '1', 'e': '2'}
line = 'qwerty qwe rty'
print(line)
t = line.maketrans(y)
print(t)
print(line.translate(t))

y = 'qwe'
z = '012'
line = 'qwerty qwe rty'
print('')
print(line)
t = line.maketrans(y, z)
print(t)
print(line.translate(t))

preview('')



