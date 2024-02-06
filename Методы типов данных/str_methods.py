def preview(x):
    print(f'\n---- str.{x} ----')


x = 'Что ТАКОЕ LOREM Ipsum?'
print(f'str = {x}')

preview('capitalize()')
print(x.capitalize())

preview('casefold()')
print(x.casefold())

preview('center()')
print(x.center(len(x)+20, ' '))

preview('count()')
print(x.count('O'))
print(x.count('O', 2))
print(x.count('O', 2, 5))

preview('encode()')
print(x.encode('utf-8'))
print(x.encode('ascii', errors='replace'))

preview('endswitch()')
print(x.endswith('?'))
print(x.endswith('Ipsum'))

y = ('m', '?')
for i in x[16:]:
    print('YES', i) if i.endswith(y) else print('NO', i)

preview('expandtabs()')
y = '01\t012\t0123\t01234'
print(y.expandtabs())
print(y.expandtabs(4))

preview('find()')
print(x.find('Что'))
print(x.find('Что', 3, 10))

preview('format()')
print('{0} {1} {1} {0}'.format('a', 'b'))
y = {'a': '0', 'b': '1'}
print('{a} {b} {b} {a}'.format(**y))

preview('format_map()')
...


