from queue import Queue
def preview(x):
    print(f'\n---- {x} ----')


preview('QUEUES')
# Очередь (Queue) — это особая структура данных, которая представляет упорядоченный список элементов, в котором добавление новых элементов осуществляется в конец, а удаление — из начала списка

# STRUCTURE
# ENQUEUE - LAST - QUEUE - FIRST - DEQUEUE


# COMPLEXITY

# ADD ELEMENT enqueue = O(1)
# DELETE ELEMENT = O(1)
# GET FIRST ELEMENT IN QUEUES = O(1)
# GET LAST ELEMENT IN QUEUES = O(1)

preview('QUEUE module implementation')
print()

q = Queue(maxsize=3)
print(q.qsize())
q.put('a')
q.put('b')
q.put('c')
print('\nFull:', q.full())
print('Is empty:', q.empty())
print('Size:', q.qsize())
print('Maxsize:', q.maxsize)


