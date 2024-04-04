## DATASTRUCTURES, ALGORITHMS AND NOTATION

## BIG O NOTATION

| **BIG O NOTATION (order of growth)** | **COMPLEXITY** | **Description**                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| O(1)                                 | CONSTANT       | The complexity of an algorithm is said to be constant if the steps required to complete the execution of an algorithm remain constant, irrespective of the number of inputs. The constant complexity is denoted by O(c) where c can be any constant number.                                                                                                                       |
| O(log(n))                            | LOGARITHMIC    | A logarithmic algorithm halves the list every time it’s run.                                                                                                                                                                                                                                                                                                                      |
| O(n)                                 | LINEAR         | Linear time algorithms mean that every single element from the input is visited exactly once, O(n) times. As the size of the input, N, grows our algorithm’s run time scales exactly with the size of the input.                                                                                                                                                                  |
| O(nlog(n))                           | LOG LINEAR     | It falls between O(n) and O(n2). This is the fastest time possible for a comparison sort. We cannot get any faster unless we use some special property, like Radix sort. O(n log n) is the fastest comparison sort time.                                                                                                                                                          |
| O(n²)                                | QUADRATIC      | The complexity of an algorithm is said to be quadratic when the steps required to execute an algorithm are a quadratic function of the number of items in the input. Quadratic complexity is denoted as O(n²):                                                                                                                                                                    |
| O(n³)                                | CUBIC          | A triple nested loop is O(n3).                                                                                                                                                                                                                                                                                                                                                    |
| O(nˣ)                                | POLYNOMIAL     | O(n²), O(n³), ..., O(nⁿ⁺¹) Notice how polynomial time dwarfs the others? Polynomial time is a polynomial function of the input. A polynomial function looks like n2 or n3 and so on. If one loop through a list is O(n), 2 loops must be O(n2). For each loop, we go over the list once. For each item in that list, we go over the entire list once. Resulting in n2 operations. |
| O(2ⁿ)                                | EXPONENTIAL    | Exponential time is 2n, where 2 depends on the permutations involved.                                                                                                                                                                                                                                                                                                             |
| O(n!)                                | FACTORIAL      | This time complexity is often used as a joke, referring to Bogo Sort. I have yet to find a real-life (not-a-joke) algorithm that runs in O(n!) that isn’t an algorithm calculating O(6!) or the likes.                                                                                                                                                                            |

## LISTS

| **Operation**                                 | **Example**     | **Complexity** | **Note**                                              |
|-----------------------------------------------|-----------------|----------------|-------------------------------------------------------|
| Получение элемента	                           | l[i]            | 	O(1)          | 	                                                     |
| Сохранение элемента                           | 	l[i] = 0	      | O(1)           |                                                       |	
| Размер списка	                                | len(l)          | 	O(1)          | 	                                                     |
| Добавление элемента в конец списка	           | l.append(5)     | 	O(1)          |                                                       |	
| Удаление последнего элемента (pop)	           | l.pop()	        | O(1)           | 	То же, что и l.pop(-1)                               |
| Очищение списка                               | 	l.clear()      | 	O(1)          | То же, что и l = []                                   |
| Получение среза                               | 	l[a:b]         | 	O(b-a)	       | l[1:5] => O(1), l[:] => O(len(l) – 0) = O(N)          |
| Расширение                                    | 	l.extend(...)	 | O(len(...))    | 	Зависит от размера расширения                        |
| Создание                                      | 	list(...)      | 	O(len(...))   | 	Зависит от размера итерируемой структуры (...)       |
| Сравнение списков (==, !=)	                   | l1 == l2        | 	O(N)          | 	                                                     |
| Вставка                                       | 	l[a:b] = ...	  | O(N)	          |                                                       |
| Удаление элемента (del)                       | 	del l[i]	      | O(N)           | 	Зависит от i. O(N) – в худшем случае                 |
| Проверка наличия                              | 	x in/not in l  | 	O(N)          | 	Линейный поиск в списке                              |
| Копирование                                   | 	l.copy()	      | O(N)           | 	То же, что и l[:]                                    |
| Удаление значения (remove)                    | 	l.remove(...)  | 	O(N)	         |                                                       |
| Удаление элемента (pop)                       | 	l.pop(i)       | 	O(N)          | 	O(N-i). Для l.pop(0) => O(N)                         |
| Получение минимального/максимального значения | 	min(l)/max(l)  | 	O(N)          | 	Линейный поиск в списке                              |
| Разворачивание списка                         | 	l.reverse()    | 	O(N)	         |                                                       |
| Перебор	                                      | for v in l:	    | O(N)           | 	В худшем случае, без прерывания цикла (return/break) |
| Сортировка	                                   | l.sort()        | 	O(N Log N)	   |                                                       |
| Умножение                                     | 	k*l            | 	O(k N)        | 	5*l => O(N), len(l)*l => O(N2)                       |

## TUPLES

| **Operation**                      | **Example**   | **Complexity** | **Note**      |
|------------------------------------|---------------|----------------|---------------|
| SAME AS LISTS WHERE DS NOT CHANGE! | SAME AS LISTS | SAME AS LISTS  | SAME AS LISTS | 

## SETS

| **Operation**               | **Example**     | **Complexity**     | **Note**                                              |
|-----------------------------|-----------------|--------------------|-------------------------------------------------------|
| Размер множества	           | len(s)          | 	O(1)              |                                                       |	
| Добавление элемента         | 	s.add(5)       | 	O(1)              |                                                       |	
| Проверка наличия значения	  | x in/not in s   | 	O(1)	             | Для списков и кортежей => O(N)                        |
| Удаление значения (remove)  | 	s.remove(..)	  | O(1)               | 	Для списков и кортежей => O(N)                       |
| Удаление значения (discard) | 	s.discard(..)	 | O(1)	              |                                                       |
| Удаление значения (pop)	    | s.pop()         | 	O(1)              | 	Удаляемое значение выбирается "рандомно"             |
| Очищение множества          | 	s.clear()	     | O(1)               | 	То же, что и s = set()                               |
| Создание	                   | set(...)        | 	O(len(...))       | 	Зависит от размера итерируемой структуры (...)       |
| Сравнение множеств (==, !=) | 	s != t	        | O(len(s))          | 	То же, что и len(t)                                  |
| Сравнение множеств (<=/<)	  | s <= t	         | O(len(s))	         | issubset                                              |
| Сравнение множеств (>=/>)	  | s >= t	         | O(len(t))          | 	issuperset s <= t == t >= s                          |
| Объединение (union)         | 	s \            | t	                 | O(len(s)+len(t))                                      |                                                       |	
| Пересечение (intersection)  | 	s & t	         | O(len(s)+len(t))   | 	                                                     |
| Разность (difference)       | 	s – t          | 	O(len(s)+len(t))	 |                                                       |
| Симметричная разность	      | s ^ t           | 	O(len(s)+len(t))	 |                                                       |
| Перебор множества	          | for v in s:     | 	O(N)              | 	В худшем случае, без прерывания цикла (return/break) |
| Копирование	                | s.copy()        | 	O(N)              |                                                       |

## FROZEN SETS

| **Operation**                    | **Example** | **Complexity** | **Note**    |
|----------------------------------|-------------|----------------|-------------|
| SAME AS SET WHERE DS NOT CHANGE! | SAME AS SET | SAME AS SET    | SAME AS SET | 

## DICTS

| **Operation**              | **Example**  | **Complexity**                      | **Note**                                                                    |
|----------------------------|--------------|-------------------------------------|-----------------------------------------------------------------------------|
| Получение элемента         | d[k]         | O(1)                                |                                                                             |	
| Сохранение элемента	       | d[k] = v     | 	O(1)                               |                                                                             |	
| Размер словаря             | 	len(d)      | 	O(1)	                              |                                                                             |
| Удаление элемента (del)	   | del d[k]     | 	O(1)	                              |                                                                             |
| get/setdefault             | 	d.get(k)	   | O(1)	                               |                                                                             |
| Удаление (pop)	            | d.pop(k)     | 	O(1)	                              |                                                                             |
| Удаление (popitem)         | 	d.popitem() | 	O(1)                               | 	Удаляемое значение выбирается "рандомно"                                   |
| Очищение словаря	d.clear() | 	O(1)        | 	То же, что и s = {} или s = dict() |
| Получение ключей	d.keys()  | 	O(1)	       | То же для d.values()                |
| Создание словаря	          | dict(...)    | 	O(len(...))	                       |
| Перебор элементов          | 	for k in d: | 	O(N)                               | 	Для всех типов: keys, values, items. В худшем случае, без прерывания цикла |

## COMPLEXITY CALCULATION EXAMPLE

| **Code**                                      | **Complexity** |
|-----------------------------------------------|----------------|
| def func(mylist : \[int]) ->bool:             |                |
| ....for i in range(len(mylist)):              | O(n)           |
| ........for j in range(i+1, len(mylist)):     | O(n)           |
| ............if mylist\[i] == mylist\[j]       | O(1)           |
| ................return False                  | O(1)           |
| ....return True                               | O(1)           |
| calculation: O(n) * O(n) * O(1) + O(1) + O(1) | O(n²)          |

| **Code**                                                                                                                                                                    | **Complexity** |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| def func(mylist : \[int] -> bool:                                                                                                                                           | O(n)           |
| ....copy = list(mylist)                                                                                                                                                     | O(n log n)     |
| ....copy.sort()                                                                                                                                                             | O(n)           |
| ....for i in range(len(mylist)-1):                                                                                                                                          | O(1)           |
| ........if copy\[i] == copy\[i+1]:                                                                                                                                          | O(1)           |
| ............return False                                                                                                                                                    | O(1)           |
| ....return True                                                                                                                                                             | O(1)           |
| calculation: O(n) + O(n log n) + O(n) * O(1) * O(1) + O(1) + O(1) = O(n + n log n + O(n\ * 1\ * 1) + 1 + 1) = O(n + n log n + n + 1 + 1) = O(n log n + 2n + 2) = O(n log n) | On(n log n)    |

## DATA STRUCTURES

[DATA STRUCTURES YOUTUBE](https://www.youtube.com/watch?v=odW9FU8jPRQ&list=PLkZYeFmDuaN2-KUIv-mvbjfKszIGJ4FaY&index=3&ab_channel=theroadmap)

| **DATA STRUCTURE TYPE** | **Description**                                                                                                                                                                                                                                                                                          | **urls**                                                                        |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| `ARRAY`                 | `МАССИВ` - структура данных, хранящая набор значений (элементов массива), идентифицируемых по индексу или набору индексов, принимающих целые (или приводимые к целым) значения из некоторого заданного непрерывного диапазона. Содержимое массива хранится в непрерывной области памяти.                 | [INFO](https://www.geeksforgeeks.org/python-arrays/)                            |
| `LINKED LIST`           | `СВЯЗАННЫЙ СПИСОК` - структура данных, в которой несколько значений хранятся линейно. Каждое значение содержит своё собственное значение узла, а также содержит данные вместе со ссылкой на следующий узел в списке. Ссылка - это указатель на другой объект узла или на null , если следующего узла нет | [INFO](https://realpython.com/linked-lists-python/#how-to-create-a-linked-list) |
| `SKIP LIST`             | `СПИСОК С ПРОПУСКАМИ` - структура данных, основанная на нескольких параллельных отсортированных связных списках с эффективностью, сравнимой с двоичным деревом (порядка O(log n) среднее время для большинства операций).                                                                                | [INFO](https://www.geeksforgeeks.org/skip-list-set-3-searching-deletion/amp/)   |
| `STACK`                 | `СТОПКА` - структура данных, представляющая из себя упорядоченный набор элементов, в которой добавление новых элементов и удаление существующих производится с одного конца, называемого вершиной стека - LIFO (LAST IN FIRST OUT).                                                                      | [INFO](https://www.geeksforgeeks.org/queue-in-python/)                          |
| `QUEUE`                 | `ОЧЕРЕДЬ` - структура данных, которая представляет упорядоченный список элементов, в котором добавление новых элементов осуществляется в конец, а удаление — из начала списка - FIFO (FIRST IN FIRST OUT)                                                                                                | [INFO](https://www.geeksforgeeks.org/queue-in-python/)                          |
| `HASH TABLE`            | `ХЭШ ТАБЛИЦА` - структура данных, которая позволяет эффективно хранить и получать информацию. Она основана на принципе хэширования, который позволяет быстро находить нужные элементы по их ключам.                                                                                                      | [INFO](https://www.edureka.co/blog/hash-tables-and-hashmaps-in-python/)         |
| `TREE`                  | `ДЕРЕВО` - структура данных эмулирующая древовидную структуру в виде набора связанных узлов. Является связным графом, не содержащим циклы. Большинство источников также добавляет условие на то, что рёбра графа не должны быть ориентированными.                                                        | [INFO](https://blog.boot.dev/computer-science/binary-search-tree-in-python/)    |
| `HEAP`                  | -                                                                                                                                                                                                                                                                                                        |                                                                                 |
| `GRAPH`                 | -                                                                                                                                                                                                                                                                                                        |                                                                                 |                                                                                 |                                                                                 |                    

## DATA STRUCTIRES COMPLEXITY

| **DATA STRUCTURE** | **INDEXING** | **SEARCH** | **INSERTION** | **DELETION** |
|--------------------|--------------|------------|---------------|--------------|
| BASIC ARRAY        | O(1)         | O(n)       | -             | -            |
| DINAMIC ARRAY      | O(1)         | O(n)       | O(n)          | O(n)         |
| SINGLE LINKED LIST | O(n)         | O(n)       | O(1)          | O(1)         |
| DOUBLE LINKED LIST | O(n)         | O(n)       | O(1)          | O(1)         |
| SKIP LIST          | O(log n)     | O(log n)   | O(log n)      | O(log n)     |
| HASH TABLE         | -            | O(1)       | O(1)          | O(1)         |
| BINARY SEARCH TREE | O(log n)     | O(log n)   | O(log n)      | O(log n)     |
| CARTESIAN TREE     | -            | O(log n)   | O(log n)      | O(log n)     |
| B-TREE             | O(log n)     | O(log n)   | O(log n)      | O(log n)     |
| RED-BLACK TREE     | O(log n)     | O(log n)   | O(log n)      | O(log n)     |
| SPLAY TREE         | -            | O(log n)   | O(log n)      | O(log n)     |
| AVL TREE           | O(log n)     | O(log n)   | O(log n)      | O(log n)     |





