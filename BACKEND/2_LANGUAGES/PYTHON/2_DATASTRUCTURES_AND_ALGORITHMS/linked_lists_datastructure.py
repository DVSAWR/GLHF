def preview(x):
    print(f'\n---- {x} ----')


preview('LINKED LISTS')
# Связный список - это структура данных, в которой несколько значений хранятся линейно. Каждое значение содержит своё собственное значение узла, а также содержит данные вместе со ссылкой на следующий узел в списке. Ссылка - это указатель на другой объект узла или на null , если следующего узла нет
# NODE - element
# LINK - NODE.next
# HEAD - start of list
# TAIL - end of list
# LINK OF TAIL = None

# COMPLEXITY
# CREATING =
# ALGORITHMIC COMPLEXITY OF ADD AN ELEMENT = 0(1)
# ALGORITHMIC COMPLEXITY OF DELETING AN ELEMENT = 0(1)
# ALGORITHMIC COMPLEXITY OF TRAVERSING = 0(n)
# ALGORITHMIC COMPLEXITY OF ACCESSING AN ELEMENT = 0(n)


# LL TYPES
# 1. SINGLY LL (HEAD - NODE(data, next) - TAIL(next = None)
# 2. DOUBLY LL (HEAD(previous = None) - NODE(data, previous, next) - TAIL(next = None)
# 3. CIRCULAR LL (HEAD - NODE(data, next) - TAIL(next = HEAD)
# 4. DOUBLY CIRCULAR LL (HEAD(previous = TAIL) - NODE(data, previous, next) - TAIL(next = HEAD)




preview('HOW TO CREATE LINKED LISTS')


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('NONE')
        return ' -> '.join(nodes)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


print()
llist = LinkedList()
print(llist)



print('\nFirst Node:')
first_node = Node('a')
llist.head = first_node
print(llist)

print('\nSecond Node:')
second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node
print(llist)

preview('HOW TO TRAVERSE A LINKED LIST')


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('NONE')
        return ' -> '.join(nodes)


llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
print(llist)

for node in llist:
    print(node, end=' -> ')

print()
preview('HOW TO INSERT A NEW NODE')


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('NONE')
        return ' -> '.join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            # raise Exception('List is empty')
            print('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        # raise Exception(f'Node with data {target_node_data} not found')
        print(f'Node with data {target_node_data} not found')

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f'Node with data {target_node_data} not found')


print('\ninserting at the beginning')
print('add_firt(Node())')
llist = LinkedList()
print(llist)

llist.add_first(Node('b'))
print(llist)

llist.add_first(Node('a'))
print(llist)

print('\ninserting at the end')
print('add_last(Node())')

llist = LinkedList(['a', 'b', 'c'])
print(llist)

llist.add_last(Node('e'))
print(llist)

llist.add_last(Node('f'))
print(llist)

print('\ninserting between two nodes')
print('\nadd_after(Node())')

llist = LinkedList()
llist.add_after('a', Node('b'))

llist = LinkedList(['a', 'b', 'c'])
print(llist)

llist.add_after('c', Node('gg'))
print(llist)

llist.add_after('f', Node('g'))
print(llist)

print('\nadd_before(Node())')

llist = LinkedList()
# llist.add_before('a', Node('b'))
print(llist)

llist = LinkedList(['b', 'c'])
print(llist)
llist.add_before('b', Node('a'))
print(llist)

llist.add_before('b', Node('aa'))
llist.add_before('c', Node('bb'))
print(llist)

# llist.add_before('n', Node('m'))
print()

preview('HOW TO REMOVE A NODE')


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('NONE')
        return ' -> '.join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            # raise Exception('List is empty')
            print('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        # raise Exception(f'Node with data {target_node_data} not found')
        print(f'Node with data {target_node_data} not found')

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f'Node with data {target_node_data} not found')

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f'Node with data {target_node_data} not found')


llist = LinkedList()
# llist.remove_node('a')
print(llist)

llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
print(llist)
llist.remove_node('b')
print(llist)

llist.remove_node('c')
print(llist)

llist.remove_node('e')
print(llist)

# llist.remove_node('e')


preview('USING ADVANCED LINKED LISTS')
print()
preview('HOW TO USE DOUBLE LINKED LISTS')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


preview('HOW to USE CIRCULAR LINKED LISTS')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        node = self.data
        return node


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(' -> '.join(nodes))



circular_llist = CircularLinkedList()
circular_llist.print_list()

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d
d.next = a

circular_llist.head = a
circular_llist.print_list()
circular_llist.print_list(b)
circular_llist.print_list(c)
circular_llist.print_list(d)





