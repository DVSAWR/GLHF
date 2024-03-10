'''

E. Прибыльный стартап
Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
k
 друзей организовали стартап по производству укулеле для кошек. На сегодняшний день прибыль составила
n
 рублей. Вы, как главный бухгалтер компании, хотите в каждый из ближайших
d
 дней приписывать по одной цифре в конец числа, выражающего прибыль. При этом в каждый из дней прибыль должна делиться на
k
.
Формат ввода
В единственной строке входных данных через пробел записаны три числа:
n
,
k
,
d
 — изначальная прибыль, количество учредителей компании и количество дней, которое вы собираетесь следить за прибылью
(
1
≤
n
,
k
≤
1
0
9
,
1
≤
d
≤
1
0
5
)
. НЕ гарантируется, что
n
 делится на
k
.
Формат вывода
Выведите одно целое число
x
 — прибыль компании через
d
 дней. Первые цифры числа
x
 должны совпадать с числом
n
. Все префиксы числа
x
, которые длиннее числа
n
 на
1
,
2
,
…
,
d
 цифр, должны делиться на
k
. Если возможных ответов несколько, выведите любой из них. Если ответа не существует, выведите
−
1
.
Пример 1
Ввод	Вывод
21 108 1
216

'''

import time

# TEST:
# 3
# 5 7 2
# x+


# 2
# 4 -5
# +

# 8
# -311553829 469225525 -933496047 -592182543 -29674334 -268378634 -985852521 -225395842

# 100000
# 000..0011...111


length = 3
nums = [5, 7, 2]

# ANSWER НЕЧЕТНОЕ ЧИСЛО

lenght = 3
d = {k: v for k, v in zip(range(lenght), nums)}

print(lenght)
print(d)

answer = ''

for k, v in d.items():
    if v % 2:
        pass

print('\n-------------------------')

length = 3
nums = '5 0 2'

x, z = nums[-3:].split()

x = int(x)
z = int(z)

asnwer = ''

print(nums)
print('LAST 2 NUMBERS', x, z)

if (x * z) % 2 == 0:
    print('\nx')
    print(f'EVEN > {x * z}')
if (x + z) % 2 != 0:
    print('\n+')
    print(f'ODD > {x + z}')

print('------------??-------------')

# n = 3
# nums = '5 7 2'

# n = 2
# nums = '4 -5'

n = 8
nums = '-311553829 469225525 -933496047 -592182543 -29674334 -268378634 -985852521 -225395842'

print(n, '\n', nums)

asnwer = ''

if n == 2:
    q, w = map(int, nums.split())
    print(q, w)
    print(type(q), type(w))

    if (q * w) % 2 != 0:
        print(f'\n(q * w) % 2 = {(q * w) % 2}')
        print('\nx')
        print(f'EVEN > {q * w}')
        answer += 'x'

    elif (q + w) % 2 != 0:
        print(f'(q + w) % 2 = {(q + w) % 2}')
        print('\n+')
        print(f'ODD > {q + w}')
        answer += '+'

    print('\nANSWER:', answer)

else:
    print('n ELSE:')

    nums = list(nums.split())
    print(f'NUMS LIST: {nums}')

    q, w, e = map(int, nums[-3:])
    print(q, w, e)
    print(type(q), type(w), type(e))

    if (q * w + e) % 2 != 0:
        print(f'\n(q * w + e) % 2 = {(q * w + e) % 2}')
        print('\nx')
        print(f'EVEN > {q * w + e}')
        answer += ('+' * (n - 3)) + 'x+'
        print('\nANSWER:', answer)

    elif (q * w * e) % 2 != 0:
        print(f'\n(q * w + e) % 2 = {(q * w * e) % 2}')
        print('\nx')
        print(f'EVEN > {q * w * e}')
        answer += ('+' * (n - 3)) + 'xx'
        print('\nANSWER:', answer)

    elif (q + w + e) % 2 != 0:
        print(f'\n(q * w + e) % 2 = {(q + w + e) % 2}')
        print('\nx')
        print(f'EVEN > {q + w + e}')
        answer += ('+' * (n - 3)) + '+x'
        print('\nANSWER:', answer)

    elif (q + w * e) % 2 != 0:
        print(f'\n(q * w + e) % 2 = {(q + w * e) % 2}')
        print('\nx')
        print(f'EVEN > {q + w * e}')
        answer += ('+' * (n - 3)) + 'x+'
        print('\nANSWER:', answer)

print(answer)

print('\n----------------\n')

n = 8
nums = '-311553829 469225525 -933496047 -592182543 -29674334 -268378634 -985852521 -225395842'

snums = nums.split()

print(n, '\n', snums)

n = 8
nums = '-311553829 469225525 -933496047 -592182543 -29674334 -268378634 -985852521 -225395842'
# xxx+xxx

# n = 3
# nums = '5 7 2'

# n = 2
# nums = '4 -5'

n = 6
nums = '-76959846 -779700294 380306679 -340361999 58979764 -392237502'

# ANSWER НЕЧЕТНОЕ ЧИСЛО

d = {k: v for k, v in zip(range(n), map(int, nums.split()))}

print(d)

answer = ''
x = d[0]
y = None

for k, v in d.items():

    if v == d[0]:
        x = d[0]
        print(f'X: {x}')
        print(f'x = d[0] ANSWER {k}: {answer}')

    else:
        if v == 0 and n > 100:
            answer += '+'

        if (x + v) % 2 != 0:
            x = x + v
            answer += '+'
            print(f'X: {x}')
            print(f'IF > ANSWER {k}: {answer}')

        elif (x * v) % 2 != 0:
            x = x * v
            answer += 'x'
            print(f'X: {x}')
            print(f'ELIF > ANSWER {k}: {answer}')

        else:
            x = x + v
            answer += '+'
            print(f'X: {x}')
            print(f'ELSE > ANSWER {k}: {answer}')

print('\nANSWER:', answer)
print(f'X: {x}')
print(f'X % 2 == 0: {x % 2 == 0}')

print('\n-----DONE ?----------')
# time_start = time.time()
#
# n = int(input())
# nums = input()
#
# d = {k: v for k, v in zip(range(n), map(int, nums.split()))}
#
# answer = ''
# x = None
#
# for k, v in d.items():
#
#     if v == d[0]:
#         x = d[0]
#
#     else:
#         if v == 0:
#             x += v
#             answer += '+'
#
#         elif v == 1 and d[k] != n - 2:
#             x += v
#             answer += '+'
#
#         elif (x + v) % 2 != 0:
#             x += v
#             answer += '+'
#
#         elif (x * v) % 2 != 0:
#             x *= v
#             answer += 'x'
#
#         else:
#             x = x + v
#             answer += '+'
#
# print(answer)
# time_end = time.time()
# time_total = time_end - time_start
# print(time_total)

# 25.830389976501465


print('------LIST ?-------')

n = 8
nums = '-311553829 469225525 -933496047 -592182543 -29674334 -268378634 -985852521 -225395842'
# xxx+xxx

# n = 3
# nums = '5 7 2'

# n = 2
# nums = '4 -5'

n = 6
nums = '-76959846 -779700294 380306679 -340361999 58979764 -392237502'

# n = int(input())
# nums = input()

n = 13
nums = '1 0 0 0 0 0 0 0 0 0 0 0 1'

# ANSWER НЕЧЕТНОЕ ЧИСЛО

d = list(map(int, nums.split()))

print(d)

answer = ''
x = d[0]
y = None

if 0 in d and n > 10:
    answer = 'x' * (n - 3)
    x = 0
    print(d[-3:])
    for v in d[-3:]:
        if (x + v) % 2 != 0:
            x = x + v
            answer += '+'
            print(f'\nX: {x}')
            print(f'IF > ANSWER: {answer}')

        elif (x * v) % 2 != 0:
            x = x * v
            answer += 'x'
            print(f'\nX: {x}')
            print(f'ELIF > ANSWER: {answer}')

        else:
            x = x + v
            answer += '+'
            print(f'\nX: {x}')
            print(f'ELSE > ANSWER: {answer}')
else:

    for k, v in enumerate(d):
        print(k, v)
        if v == d[0]:
            x = d[0]
            print(f'\nX: {x}')
            print(f'x = d[0] ANSWER {k}: {answer}')

        else:
            if (x + v) % 2 != 0:
                x = x + v
                answer += '+'
                print(f'\nX: {x}')
                print(f'IF > ANSWER {k}: {answer}')

            elif (x * v) % 2 != 0:
                x = x * v
                answer += 'x'
                print(f'\nX: {x}')
                print(f'ELIF > ANSWER {k}: {answer}')

            else:
                x = x + v
                answer += '+'
                print(f'\nX: {x}')
                print(f'ELSE > ANSWER {k}: {answer}')

print('\n\nANSWER:', answer)
print(f'\nX: {x}')
print(f'X % 2 == 0: {x % 2 == 0}')

print(n)
print(len(answer))

print('\n\n\n--------DONE ?-----------\n')

# n = 3
# nums = '5 7 2'

# n = 2
# nums = '4 -5'

n = 6
nums = '-76959846 -779700294 380306679 -340361999 58979764 -392237502'

# n = int(input())
# nums = input()

d = list(map(int, nums.split()))

print(d)

answer = ''
x = d[0]

if 0 in d and n > 10:
    answer = 'x' * (n - 4)
    x = 0
    print(d[-3:])
    for v in d[-3:]:
        if (x + v) % 2 != 0:
            x = x + v
            answer += '+'
            print(f'\nX: {x}')
            print(f'IF > ANSWER: {answer}')

        elif (x * v) % 2 != 0:
            x = x * v
            answer += 'x'
            print(f'\nX: {x}')
            print(f'ELIF > ANSWER: {answer}')

        else:
            x = x + v
            answer += '+'
            print(f'\nX: {x}')
            print(f'ELSE > ANSWER: {answer}')
else:

    for k, v in enumerate(d):
        print(k, v)
        if v == d[0]:
            x = d[0]
            print(f'\nX: {x}')
            print(f'x = d[0] ANSWER {k}: {answer}')

        else:
            if (x + v) % 2 != 0:
                x = x + v
                answer += '+'
                print(f'\nX: {x}')
                print(f'IF > ANSWER {k}: {answer}')

            elif (x * v) % 2 != 0:
                x = x * v
                answer += 'x'
                print(f'\nX: {x}')
                print(f'ELIF > ANSWER {k}: {answer}')

            else:
                x = x + v
                answer += '+'
                print(f'\nX: {x}')
                print(f'ELSE > ANSWER {k}: {answer}')

print('\n\nANSWER:', answer)
print(n)
print(f'ANSWER LEN {len(answer)}')
print(f'\nX: {x}')
print(f'X % 2 == 0: {x % 2 == 0}')

print('\n\n\n--------DONE ?-----------\n')

# n = int(input())
# nums = input()

# n = 3
# nums = '5 7 2'

# n = 2
# nums = '4 -5'

n = 6
nums = '-76959846 -779700294 380306679 -340361999 58979764 -392237502'

# d = list(nums.split())
d = list(map(int, nums.split()))
print(d)

answer = ''
x = d[0]

if 0 in d and n > 10:
    answer = 'x' * (n - 4)
    x = 0
    for v in d[-3:]:
        if (x + v) % 2 != 0:
            x = x + v
            answer += '+'
        elif (x * v) % 2 != 0:
            x = x * v
            answer += 'x'
        else:
            x = x + v
            answer += '+'

for i in d[5:20]:
    if i % 2 != 0:
        x = d.index(i)


else:
    for v in d:
        if v == d[0]:
            x = d[0]
        else:
            if (x + v) % 2 != 0:
                x = x + v
                answer += '+'
            elif (x * v) % 2 != 0:
                x = x * v
                answer += 'x'
            else:
                x = x + v
                answer += '+'

print(answer)

print('\n\n\n------DONE ??-------\n')

# n = 3
# nums = '5 7 2'

# n = 2
# nums = '4 -5'

# n = 6
# nums = '-76959846 -779700294 380306679 -340361999 58979764 -392237502'

n = 112
nums = '934413450 -957753032 -47996878 416963766 -911982310 -911110608 -506958757 144074642 680827101 -203188344 370782033 203626375 -963004384 -782912288 -362998804 913080090 717297523 889618066 -952404592 659199761 123018664 190298102 466641860 -710892072 106944290 718271672 238101965 -506446387 144992919 340919771 -607194303 -849854995 174453227 -788028891 987623482 -740917081 -512465139 -573842122 628763678 892240457 -88835707 -932127010 341619016 443013869 576518596 -929158501 397581843 559477394 -63383506 -13234087 217255607 -731650428 -148157818 846356438 820352024 386771993 126149197 644853997 952655327 -919501547 -430096983 783064729 -979559563 61805723 -518285156 837041870 296623772 128773805 192908639 29651375 457806699 -807413503 110710563 -262266466 -292405344 -145309950 492234193 395554889 889060554 549771258 214597171 247791141 -454818660 197837624 -25719589 577227831 661150092 -223829760 788086687 287607645 860594023 -114426162 823950382 258236252 -463823516 -481873994 382852191 -278533194 662881919 -667438613 -178064504 -80324364 -17104160 186709960 192598029 544650360 -264911894 -198312419 766162381 -452340259 -943035273 -881429417'


d = list(map(int, nums.split()))


print(d)

answer = ''

first_odd_index = None

print(x)

for i in d:
    if i % 2 != 0 and d.index(i) > 5:
        first_odd_index = d.index(i) + 1
        break

print(first_odd_index)
print(d[:first_odd_index + 1])

if first_odd_index is not None:
    new_d = d[:first_odd_index]
    print(d)
else:
    new_d = d

for v in new_d:
    if v == new_d[0]:
        x = new_d[0]
    else:
        if (x + v) % 2 != 0:
            x = x + v
            answer += '+'
        elif (x * v) % 2 != 0:
            x = x * v
            answer += 'x'
        else:
            x = x + v
            answer += '+'



print('\n\nANSWER:', answer)
print(n)
print(f'ANSWER LEN {len(answer)}')
print(f'\nX: {x}')
print(f'X % 2 == 0: {x % 2 == 0}')


print('\n\n\n--------DONE SEREJA--------\n')

n = 6
nums = '-76959846 -779700294 380306679 -340361999 58979764 -392237502'

d = list(map(int, nums.split()))

print(d)

answer = ''

# odd even

first_odd_index = None

for i in d:
    if i % 2 != 0:
        first_odd_index = d.index(i)
        break

# 4 типа условвий - сережа


for i in range(n - 1):

    if int(d[i]) % 2 == 0 and int(d[i + 1]) % 2 == 0:
        answer += '+'

    if int(d[i]) % 2 == 0 and int(d[i + 1]) % 2 != 0:
        answer += 'x'

    if int(d[i]) % 2 != 0 and int(d[i + 1]) % 2 == 0:
        answer += 'x'

    if int(d[i]) % 2 != 0 and int(d[i + 1]) % 2 != 0:
        answer += 'x'





