'''

Задано две строки, нужно проверить, является ли одна анаграммой другой. Анаграммой называется строка, полученная из другой перестановкой букв.

Формат ввода
Строки состоят из строчных латинских букв, их длина не превосходит 100000. Каждая записана в отдельной строке.

Формат вывода
Выведите "YES" если одна из строк является анаграммой другой и "NO" в противном случае.

Пример 1
Ввод	Вывод
dusty
study
YES
Пример 2
Ввод	Вывод
rat
bat
NO

'''

print('-----DONE-----')

first = input()
second = input()

# print(sorted(list(first)))
# print(sorted(list(second)))

if sorted(list(first)) == sorted(list(second)):
    print('YES')
else:
    print('NO')


# dusty
# study
#
# rat
# bat
# zirkanrlepcmvyjbpgpizexomgzmymouadzywuitkhicnqtrszvrwukcvoknymyiqfdvkdubisfvzidwplywyzjssymazynkubqv
# lcegwwmrebgvtbggnztiaayfatbpiphwwwlkhdahnsxnafiglugnukuxhjxguywtizxbsfqjedtzovtyxbhyzzhzmyrzeydpfosv