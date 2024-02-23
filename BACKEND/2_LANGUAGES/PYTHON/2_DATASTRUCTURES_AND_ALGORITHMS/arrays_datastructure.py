import array as arr


def preview(x):
    print(f'\n---- {x} ----')


print('|' + ' 1b |' * 10)

print('')

preview('ARRAYS')
# Наиболее распространенной и общеизвестной структурой данных является массив (array), который содержит непрерывную совокупность элементов данных, к которым можно получить доступ. В любом языке программирования массивы имеют несколько общих свойств: Содержимое массива хранится в непрерывной области памяти.






preview('HOW TO CREATE ARRAYS')
a = arr.array('i', [1, 2, 3])
print('The new created array is: ', end=' ')
for i in range(0, 3):
    print(a[i], end=' | ')
print()

b = arr.array('d', [2.5, 3.2, 3.3])
print('The new created array is: ', end=' ')
for i in range(0, 3):
    print(b[i], end=' ')



print()
preview('HOW TO ADD ELEMENT')
a = arr.array('i', [1, 2, 3])
print('array before insertion: ', end=' ')
for i in range(0, 3):
    print(a[i], end=' | ')
print()

a.insert(1, 4)
print('array after insertion: ', end=' ')
for i in (a):
    print(i, end=' | ')
print('')
b = arr.array('d', [2.5, 3.2, 3.3])
print('array before insertion: ', end=' ')
for i in range(0, 3):
    print(b[i], end=' | ')
print()

b.append(4.4)
print('array after insertion: ', end=' ')
for i in (b):
    print(i, end=' | ')
print()






#
# print('\nSlicing of an Array')
#
# l = list(range(10))
#
# a = arr.array('i', l)
# print('initial array: ')
# for i in (a):
#     print(i, end=' | ')
# print()
#
# sliced_array = a[3:8]
# print('\nslicing elements in a[3:8]: ')
# print(sliced_array)
#
# sliced_array = a[5:]
# print('\nslicing elements in a[5:]: ')
# print(sliced_array)

sliced_array = a[:]
print('\nslicing elements in a[:] (all elements): ')
print(sliced_array)
