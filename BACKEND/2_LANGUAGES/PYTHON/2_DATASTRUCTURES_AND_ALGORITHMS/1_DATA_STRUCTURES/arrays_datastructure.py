import array
import array as arr


def preview(x):
    print(f'\n---- {x} ----')


print('|' + ' 1b |' * 10)

print('')

preview('ARRAYS')
# Наиболее распространенной и общеизвестной структурой данных является массив (array), который содержит непрерывную совокупность элементов данных, к которым можно получить доступ. В любом языке программирования массивы имеют несколько общих свойств: Содержимое массива хранится в непрерывной области памяти.

# ITEMS HAVE SAME TYPE IN ONE ARRAY (SAME SIZE OF ITEMS IN BYTES)
# SIZE OF MEMORY FIXED (SAME SIZE OF ITEMS IN BYTES)

# MEMORY LEAK IN MEMORY RESERVATION WHEN CREATE ARRAY

# STRUCTURE
# ARRAY
# 1 BYTE = 1 SLOT MEMORY



# COMPLEXITY
# ACCESSING AN ELEMENT AT INDEX = 0(1)
# INSERTING NEW AT INDEX = O(n)
# DELETING FROM INDEX = O(n)
# UPDATING AT INDEX = O(1)
# TRAVERSING THE ARRAY = O(n)
#



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

preview('HOW ACCESSING TO ELEMENTS')

a = arr.array('i', [1, 2, 3, 4, 5, 6])
print(a)
print('access element is: ', a[0])
print('access element is: ', a[3])

print()
b = arr.array('d', [2.5, 3.2, 3.3])
print(b)
print('access element is: ', b[1])
print('access element is: ', b[2])

print()
preview('HOW DELETE ELEMENT')

a = array.array('i', [1, 2, 3, 1, 5])
print('The new created array is: ')
for i in range(0, 5):
    print(a[i], end=" | ")

print('The popped element is: ', end=' ')

print(a.pop(2))

print('THe array after popping is: ', end=' ')
for i in range(0, 4):
    print(a[i], end=' | ')

print()
a.remove(1)
print('The array after removing is: ', end=' ')
for i in range(0, 3):
    print(a[i], end=' | ')


print()
preview('HOW SLICING ARRAY')



l = list(range(10))

a = arr.array('i', l)
print('initial array: ')
for i in (a):
    print(i, end=' | ')
print()

sliced_array = a[3:8]
print('\nslicing elements in a[3:8]: ')
print(sliced_array)

sliced_array = a[5:]
print('\nslicing elements in a[5:]: ')
print(sliced_array)

sliced_array = a[:]
print('\nslicing elements in a[:] (all elements): ')
print(sliced_array)


print()
preview('HOW SEARCHING ELEMENT IN ARRAY')

a = array.array('i', [1, 2, 3, 1, 2, 5])
for i in range(0, 6):
    print(a[i], end=' | ')

print('\n')
print('The index of 1st occurrence of 2 is: ', end=' ')
print(a.index(2))

print()
print('The index of 1st occurrence of 1 is: ', end=' ')
print(a.index(1))

print()
print('The index of 1st occurrence of 5 is: ', end=' ')
print(a.index(5))


print()
preview('UPDATING ELEMENTS IN ARRAY')

a = array.array('i', [1, 2, 3, 1, 2, 5])
for i in range(0, 6):
    print(a[i], end=' | ')

print('\n')

a[2] = 99
print('array after updating a[2] = 99: ', end=' ')
for i in range(0, 6):
    print(a[i], end=' | ')

