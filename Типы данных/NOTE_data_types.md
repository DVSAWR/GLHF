## Типы данных

| **Тип данных**         | **Значение**                                            | **Определение в Python** | **Вариант использования**                              | **Изменяемость типа данных** |
|------------------------|---------------------------------------------------------|--------------------------|--------------------------------------------------------|------------------------------|
| Целые числа            | -3, -2, -1, 0, 1, 2, 3                                  | int                      | a = int(input())                                       | Immutable                    |
| Вещественные числа     | -1.5, -1.1, 0.6, 1.7                                    | float                    | a = float(input())                                     | Immutable                    |
| Комплексные числа      | −5i, 3+2i                                               | complex                  | a = complex(input())                                   | Immutable                    |
| Булевы значения        | True, False                                             | bool, True, False        | flag = True                                            |                              |
| NoneType               | None                                                    | None                     | a = None                                               |                              |
| Строка                 | 'abracadabra'                                           | str                      | a = str(5)                                             | Immutable                    |
| Список                 | [1, 2, 3], ['a', 'b', 'c']                              | list                     | a = list(('a', 'b', 'c'))                              | Mutable                      |
| Кортеж                 | ('red', 'blue', 'green')                                | tuple                    | a = tuple(('red', 'blue', 'green'))                    | Immutable                    |
| Изменяемое множество   | {'black', 'blue', 'white'}, {1, 3, 9, 7}                | set                      | a = set(('black', 'blue', 'white'))                    | Mutable                      |
| Неизменяемое множество | {'red', 'blue', 'green'}, {2, 3, 9, 5}                  | frozenset                | a = frozenset((2, 5, 3, 9))                            | Immutable                    |
| Диапазон               | 0, 1, 2, 3, 4, 5                                        | range                    | a = range(6)                                           | Immutable                    |
| Словарь                | {'color': 'red', 'model': 'VC6', 'dimensions': '30x50'} | dict                     | a = dict(color='red', model='VC6', dimensions='30x50') | Mutable                      |
| Байты                  | b'\x00\x00\x00'                                         | bytes                    | a = bytes(3)                                           | Immutable                    |
| Байтовая строка        | (b'\x00\x00')                                           | bytearray                | a = bytearray(2)                                       | Mutable                      |
| Просмотр памяти        | 0x1477a5813a00                                          | memoryview               | a = memoryview<br>(bytes(15))                          |                              |


