from queue import LifoQueue

def preview(x):
    print(f'\n---- {x} ----')



preview('STACKS')
# стопка — структура данных, представляющая из себя упорядоченный набор элементов, в которой добавление новых элементов и удаление существующих производится с одного конца, называемого вершиной стека.

# STRUCTURE

# STACK
# TOP ELEMENT
# FIFO - FIRST IN FIRST OUT
# NEW ELEMENT ADD IN TOP OF STAK
#



# COMPLEXITY
# STAK IS EMPTY empty() = O(1)
# SIZE OF STACK size() = O(1)
# RETURN TOP ELEMENT top() / peek() = O(1)
# ADD NEW ELEMENT ON TOP push() = O(1)
# DELETE TOP ELEMENT = O(1)

preview('HOW TO CREATE STACK')
print()

stack = []
print(f'stack: {stack}')
stack.append('a')
print(stack)
stack.append('b')
print(stack)
stack.append('c')
print(stack)

print(f'stack: {stack}')

print('\nElements popped from stack: ')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements popped: ')
print(stack)


print()
preview('USING QUEUE MODULE')
print()

stack = LifoQueue(maxsize=3)
print(stack)
print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')

print('full:', stack.full())
print('size:', stack.qsize())

print('\nElement popped from the stack:')
print(stack.get())
print(stack.get())
print(stack.get())

print('\nEmpty: ', stack.empty())

print()
preview('USING A SINGLY LINKED LIST')
print()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node('HEAD')
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ''
        while cur:
            out += str(cur.value) + ' -> '
            cur = cur.next
        return out[:-2]

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            print('Exception: PEEKING FROM EMPTY STACK')
        return self.head.next.value


    def spush(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1


    def spop(self):
        if self.is_empty():
            print('Exception: POPPING FROM EMPTY STACK')
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


stack = Stack()

for i in range(1, 11):
    stack.spush(i)

print(f'Stack: {stack}')


for _ in range(1, 6):
    remove = stack.spop()
    print(f'pop: {remove}')

print(f'Stack: {stack}')
print(f'Is empty: {stack.is_empty()}')
print(f'Get size: {stack.get_size()}')

print(f'Peek of stack: {stack.peek()}')
print(f'pop: {stack.spop()}')
print(f'Peek of stack: {stack.peek()}')



