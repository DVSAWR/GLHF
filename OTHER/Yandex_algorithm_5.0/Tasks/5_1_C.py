'''

Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Петя - начинающий программист. Сегодня он написал код из
n
 строк.
К сожалению оказалось, что этот код трудно читать. Петя решил исправить это, добавив в различные места пробелы. А точнее, для
i
-й строки ему нужно добавить ровно
a
i
 пробелов.
Для добавления пробелов Петя выделяет строку и нажимает на одну из трёх клавиш: Space, Tab, и Backspace. При нажатии на Space в строку добавляется один пробел. При нажатии на Tab в строку добавляются четыре пробела. При нажатии на Backspace в строке удаляется один пробел.
Ему хочется узнать, какое наименьшее количество клавиш придётся нажать, чтобы добавить необходимое количество пробелов в каждую строку. Помогите ему!

Формат ввода
Первая строка входных данных содержит одно целое положительное число
n
(
1
≤
n
≤
1
0
5
)
 – количество строк в файле.
Каждая из следующих
n
 строк содержит одно целое неотрицательное число
a
i
(
0
≤
a
i
≤
1
0
9
)
 – количество пробелов, которые нужно добавить в
i
-ю строку файла.

Формат вывода
Выведите одно число – минимальное количество нажатий, чтобы добавить в каждой строке необходимое количество пробелов.
Пример
Ввод	
5
1
4
12
9
0
Вывод
8
Примечания
В примере можно:
1 раз нажать на Space в первой строке.
1 раз нажать на Tab на второй строке.
3 раза нажать на Tab в третьей строке.
2 раза нажать на Tab и один раз нажать на Space в четвёртой строке.
Ничего не нажимать в пятой строке.
В итоге получается
1
+
1
+
3
+
3
=
8
 нажатий. Можно доказать, что нельзя добавить необходимое количество пробелов за
7
 нажатий или меньше.

'''


def button_count(x):
    count = 0
    if x == 0:
        return count
    else:
        tab = x // 4
        count += tab

        if x % 4 == 0:
            return count
        elif x % 4 == 1:
            return count + 1
        else:
            return count + 2


print('-----')

line_num = 5
# lst = []
#
# for i in range(5):
#     lst.append(int(input('NUM: ')))
#
# print(lst)

lst = [1, 4, 12, 9, 0]
# 1 4 12 9 0
for i in lst:
    print(f'FOR NUM: {i} > FROM FUNC button_count(x) > {button_count(i)}')

ans = 0
for i in lst:
    ans += button_count(i)

print(f'{'\t' * 9}SUM: {ans}')

print('----DONE----')


def button_count_in_line(x):
    count = 0
    if x == 0:
        return count
    else:
        tab = x // 4
        count += tab

        if x % 4 == 0:
            return count
        elif x % 4 == 1:
            return count + 1
        else:
            return count + 2


lines = int(input())

buttons = 0

for i in range(lines):
    buttons = buttons + button_count_in_line(int(input()))

print(buttons)

