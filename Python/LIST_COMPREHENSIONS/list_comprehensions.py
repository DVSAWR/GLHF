print('\n---- List methods ----')

my_list = [i for i in range(10)]
print(my_list)

my_list.append(5)
print(my_list)
print(my_list.count(5))
print(my_list.index(5))
print(my_list.index(5, 6))
my_list.reverse()
print(my_list)
my_list.sort()
print(my_list)
my_list.pop()
print(my_list)

print('\n---- Using Lists as Stacks ----')

stack = [1]
print(stack)
stack.append(2)
print(stack)
stack.append(3)
print(stack)
stack.pop()
print(stack)

print('\n---- Using Lists as Queues ----')

from collections import deque

queue = deque(['d', 'v'])
print(queue)
queue.append('s')
print(queue)
queue.append('a')
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)

print('\n---- List Comprehensions ----')

squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

squares = [i ** 2 for i in range(10)]
print(squares)

squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

print('')
equals = []
for x in [1, 2, 3]:
    for y in range(1, 4):
        if x != y:
            equals.append((x, y))
print(equals)

equals = [(x, y) for x in [1, 2, 3] for y in range(1, 4) if x != y]
print(equals)

print('')
my_list = [-4, -2, 0, 2, 4]
print(my_list)

print([i * 2 for i in my_list])
print([i for i in my_list if i >= 0])
print([abs(i) for i in my_list])

print('')
my_list = ['     qwe', '  qwe           ', 'q we    ']
print(my_list)
print([i.strip() for i in my_list])

print('')
print([(i, i ** 2) for i in range(5)])

print('')
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_list)
print([i for j in my_list for i in j])

print('---- List comprehensions can contain complex expressions and nested functions ----')
from math import pi

print([str(round(pi, i)) for i in range(1, 6)])

print('---- Nested List Comprehensions ----')
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
for i in matrix:
    print(i)
print('')

# 1
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print('1.', transposed)

# 2
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print('2.', transposed)

# 3
transposed = [[row[i] for row in matrix] for i in range(4)]
print('3.', transposed)

# 4
transposed = list(zip(*matrix))
print('4.', transposed)

print('---- The del statement ----')

my_list = [-1, 1, 66.25, 333, 333, 1234.5]
print(my_list)

del my_list[0]
print(my_list)

del my_list[:3]
print(my_list)

del my_list[:]
print(my_list)


print('---- Tuples and Sequences Comprehensions ----')
my_tuple = (i for i in range(5))
print(*my_tuple)

print('---- Sets Comprehensions ----')
my_set = {i for i in 'qqwerty' if i not in 'rty'}
print(my_set)

print('---- Dictionaries Comprehensions ----')
my_dict = {k: v for k, v in zip('taco', range(len('taco')))}
print(my_dict)

