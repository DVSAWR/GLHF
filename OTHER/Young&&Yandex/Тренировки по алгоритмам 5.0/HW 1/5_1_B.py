# B. Футбольный комментатор
# Ограничение времени	2 секунды
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Раунд плей-офф между двумя командами состоит из двух матчей. Каждая команда проводит по одному матчу «дома» и «в гостях». Выигрывает команда, забившая большее число мячей. Если же число забитых мячей совпадает, выигрывает команд, забившая больше мячей «в гостях». Если и это число мячей совпадает, матч переходит в дополнительный тайм или серию пенальти.
#
# Вам дан счёт первого матча, а также счёт текущей игры (которая ещё не завершилась). Помогите комментатору сообщить, сколько голов необходимо забить первой команде, чтобы победить, не переводя игру в дополнительное время.
#
# Формат ввода
# В первой строке записан счёт первого мачта в формате G1:G2, где G1 "— число мячей, забитых первой командой, а G2 "— число мячей, забитых второй командой. Во второй строке записан счёт второго (текущего) матча в аналогичном формате. Все числа в записи счёта не превышают 5.
#
# В третьей строке записано число 1, если первую игру первая команда провела «дома», или 2, если «в гостях».
#
# Формат вывода
# Выведите единственное целое число "— необходимое количество мячей.
#
# Пример 1
# Ввод
# 0:0
# 0:0
# 1
# Вывод 1

# Пример 2
# Ввод	Вывод
# 0:2
# 0:3
# 1
# Вывод 5

# Пример 3
# Ввод
# 0:2
# 0:3
# 2
# Вывод 6
#

# первый матч
g1 = (0, 0)
# второй матч
g2 = (0, 0)
# поле (1 - дом --- 2 - в гостях)
f = 1

# g1 = tuple(map(int, input().split()))
g1 = (0, 2)
print(g1)

# g2 = tuple(map(int, input().split()))
g2 = (0, 3)
print(g2)

# f = int(input())
f = 1
print(f)

fcg1 = g1[0]
scg1 = g1[1]
print(fcg1, scg1)

fcg2 = g2[0]
scg2 = g2[1]
print(fcg2, scg2)

tfc = g1[0] + g2[0]
tsc = g1[1] + g2[1]
print(tfc, tsc)

if tfc > tsc:
    print('fc win')
if tfc < tsc:
    print('sc win')

if tfc == tsc:
    if f == 2:
        ...  # + 1 to need goals

print('------')
tfc = g1[0] + g2[0]
tsc = g1[1] + g2[1]
print(tfc, tsc)
f = 1
print(f)

print('------')
g1 = (5, 4)
print(g1)
g2 = (3, 4)
print(g2)
f = 2
print(f)

# TEST 5
# 2:2
# 1:1
# 2

# TEST 12
# 5:4
# 3:0
# 2

# TEST 15
# 2:3
# 5:4
# 2
# ans = 1

# TEST 20
# 5 2
# 0 5
# 1
# 3


fcscore = g1[0] + g2[0]
scscore = g1[1] + g2[1]

x = scscore - fcscore

if fcscore == scscore:
    if f == 1:
        x = 1
    if f == 2:
        x = 0

if f == 2 and scscore > fcscore:
    x += 1

if fcscore > scscore:
    x = 0

print(x)

print('------')

# g1 = list(map(int, input().split(':')))
# g2 = list(map(int, input().split(':')))
# f = int(input())
#

# if scscore > fcscore:
#     if f == 1:
#         print(scscore - fcscore)
#     if f == 2:
#         print(scscore - fcscore + 1)
#
#
# if fcscore > scscore:
#     print(0)
#
# if fcscore == scscore:
#     if g1[0] != g1[1] and g2[0] != g2[1]:
#         if f == 1:
#             print(0)
#         if f == 2:
#             print(1)
#     else:
#         if f == 1:
#             print(1)
#         if f == 2:
#             print(0)


g1 = [5, 2]
print(g1)
g2 = [0, 5]
print(g2)
f = 1
print(f)

print('------')


def score(fgfc, fgsc, sgfc, sgsc, f):
    tsfc = fgfc + sgfc
    tssc = fgsc + sgsc
    # print(f'{fgfc}:{fgsc}')
    # print(f'{sgfc}:{sgsc}')
    # print(f)
    # print(f'{tsfc}:{tssc}')

    if tsfc > tssc:
        print(0)

    if tsfc < tssc:
        if f == 1:
            if fgfc == 0:
                print(tssc - tsfc)
            else:
                tssc += 1
                print(tssc - tsfc)
        if f == 2:
            if fgfc == 0:
                tssc += 1
                print(tssc - tsfc)
            else:
                print(tssc - tsfc)

    if tsfc == tssc:

        if fgfc != fgsc and sgfc != sgsc:
            if f == 1:
                print(0)
            if f == 2:
                print(1)
        else:
            if f == 1:
                print(1)
            if f == 2:
                print(0)


score(5, 1, 0, 5, 2)

print('------')


def score(fgfc, fgsc, sgfc, sgsc, f):
    tsfc = fgfc + sgfc
    tssc = fgsc + sgsc

    print(f'{fgfc}:{fgsc}')
    print(f'{sgfc}:{sgsc}')
    print(f)
    print(f'{tsfc}:{tssc}')

    if tsfc > tssc:
        print(0)

    if tsfc < tssc:
        if f == 1:
            if fgfc == 0:
                print(tssc - tsfc)
            else:
                tssc += 1
                print(tssc - tsfc)
        if f == 2:
            if fgfc == 0:
                tssc += 1
                print(tssc - tsfc)
            else:
                print(tssc - tsfc)

    if tsfc == tssc:

        if fgfc != fgsc and sgfc != sgsc:
            if f == 1:
                print(0)
            if f == 2:
                print(1)
        else:
            if f == 1:
                print(1)
            if f == 2:
                print(0)


score(5, 2, 0, 5, 1)

# g1, gg1 = map(int, input().split(':'))
# g2, gg2 = map(int, input().split(':'))
# ff = int(input())
#
# print(g1, gg1, g2, gg2, ff)
# score(g1, gg1, g2, gg2, ff)

print('--------')

g1_c1, g1_c2, g2_c1, g2_c2, f = 4, 5, 3, 2, 1

tgs_c1 = g1_c1 + g2_c1
tgs_c2 = g1_c2 + g2_c2

print(f'{g1_c1}:{g1_c2}')
print(f'{g2_c1}:{g2_c2}')
print(f)
print(f'{tgs_c1}:{tgs_c2}')

if f == 1:
    if tgs_c2 > tgs_c1:
        print(tgs_c2 - tgs_c1)
    if tgs_c2 == tgs_c1:
        print(tgs_c2 - tgs_c1 + 1)
    if tgs_c2 < tgs_c1:
        print(0)
if f == 2:
    if tgs_c2 > tgs_c1:
        print(tgs_c2 - tgs_c1 + 1)
    if tgs_c2 == tgs_c1:
        print(tgs_c2 - tgs_c1)
    if tgs_c2 < tgs_c1:
        print(0)

print('--B--')
# if tgs_c1 < tgs_c2:
#     if f == 1:
#         print(tgs_c2 - tgs_c1)
#     if f == 2:
#         print(tgs_c2 - tgs_c1 + 1)
# if tgs_c1 > tgs_c2:
#     print(0)
# if tgs_c1 == tgs_c2:
#     if f == 2:
#         if g1_c1 > g1_c2:
#             print(0)
#         else:
#             print(1)
#     if f == 1:
#         if g2_c1 > g2_c2:
#             print(0)
#         else:
#             print(1)
g1_c1, g1_c2, g2_c1, g2_c2, f = 5, 2, 0, 5, 1

print(f'{g1_c1}:{g1_c2}')
print(f'{g2_c1}:{g2_c2}')
print(f)

main_result_c1 = g1_c1 + g2_c1
main_result_c2 = g1_c2 + g2_c2
print(f'{main_result_c1}:{main_result_c2} MAIN SCORE')

guest_result_c1 = 0
guest_result_c2 = 0

if f == 1:
    if g2_c1 == 0:
        guest_result_c1 += 1
    if g1_c2 != 0:
        guest_result_c2 += 1

if f == 2:
    if g1_c1 != 0:
        guest_result_c1 += 1
    if g2_c2 != 0:
        guest_result_c2 += 1

print(f'{guest_result_c1}:{guest_result_c2} GUEST SCORE')

if main_result_c1 > main_result_c2:
    print(0)

if main_result_c1 == main_result_c2:
    if guest_result_c1 == guest_result_c2:
        print(1)
    if guest_result_c1 > guest_result_c2:
        print(guest_result_c1)
    if guest_result_c1 < guest_result_c2:
        print(1)

if main_result_c1 < main_result_c2:
    if guest_result_c1 == guest_result_c2:
        print(main_result_c2 - main_result_c1)
    if guest_result_c1 > guest_result_c2:
        print(main_result_c2 - main_result_c1)
    if guest_result_c1 < guest_result_c2:
        print((main_result_c2 + guest_result_c2) - (main_result_c1 + guest_result_c1))

print('--------')
# TEST 25
# 1:2
# 2:3
# 1

# TEST 30
# 4:5
# 2:4
# 2


# g1_c1, g1_c2 = map(int, input().split(':'))
# g2_c1, g2_c2 = map(int, input().split(':'))
# f = int(input())

g1_c1, g1_c2, g2_c1, g2_c2, f = 4, 5, 2, 4, 1

main_result_c1 = g1_c1 + g2_c1
main_result_c2 = g1_c2 + g2_c2

guest_result_c1 = 0
guest_result_c2 = 0

if f == 2:
    guest_result_c1 = g1_c1
    guest_result_c2 = g2_c2
if f == 1:
    guest_result_c2 = g2_c2

print(f'{g1_c1}:{g1_c2}')
print(f'{g2_c1}:{g2_c2}')
print(f)
print(f'{main_result_c1}:{main_result_c2} MAIN SCORE')
print(f'{guest_result_c1}:{guest_result_c2} GUEST SCORE')

resault = 0

if main_result_c1 > main_result_c2:
    print(0)

if main_result_c1 < main_result_c2:
    resault = main_result_c2 - main_result_c1
    print(f'PRE RESULT {resault}')
    if resault + main_result_c1 == main_result_c2:
        if f == 1:
            guest_result_c1 = resault
            print(f'{guest_result_c1}:{guest_result_c2} NEW GUEST SCORE f1')
        if f == 2:
            guest_result_c1 = g1_c1
            print(f'{guest_result_c1}:{guest_result_c2} NEW GUEST SCORE f2')
    if guest_result_c1 > guest_result_c2:
        print(resault)
    if guest_result_c1 < guest_result_c2:
        print(resault)
    if guest_result_c1 == guest_result_c2:
        resault += 1
        print(resault)

if main_result_c1 == main_result_c2:
    resault = 0
    if guest_result_c1 > guest_result_c2:
        print(resault)
    if guest_result_c1 < guest_result_c2:
        resault += 1
        print(resault)
    if guest_result_c1 == guest_result_c2:
        resault += 1
        print(resault)

print('\n\n--------\n')

# g1_c1, g1_c2 = map(int, input().split(':'))
# g2_c1, g2_c2 = map(int, input().split(':'))
# f = int(input())

g1_c1, g1_c2, g2_c1, g2_c2, f = 0, 2, 0, 3, 2

main_result_c1 = g1_c1 + g2_c1
main_result_c2 = g1_c2 + g2_c2

guest_result_c1 = 0
guest_result_c2 = 0

if f == 2:
    guest_result_c1 = g1_c1
    guest_result_c2 = g2_c2
if f == 1:
    guest_result_c1 = g2_c1
    guest_result_c2 = g1_c2

print(f'{g1_c1}:{g1_c2}')
print(f'{g2_c1}:{g2_c2}')
print(f)
print(f'{main_result_c1}:{main_result_c2} MAIN SCORE')
print(f'{guest_result_c1}:{guest_result_c2} GUEST SCORE')

resault = main_result_c2 - main_result_c1
gresault = guest_result_c2 - guest_result_c1

print(f'RES {resault}')
print(f'GRES {gresault}')

print('\n------SUKA------')

g1_c1, g1_c2, g2_c1, g2_c2, f = 0, 2, 0, 3, 1

main_result_c1 = g1_c1 + g2_c1
main_result_c2 = g1_c2 + g2_c2

guest_result_c1 = 0
guest_result_c2 = 0

if f == 2:
    guest_result_c1 = g1_c1
    guest_result_c2 = g2_c2
if f == 1:
    guest_result_c1 = g2_c1
    guest_result_c2 = g1_c2

print(f'{g1_c1}:{g1_c2}')
print(f'{g2_c1}:{g2_c2}')
print(f)
print(f'{main_result_c1}:{main_result_c2} MAIN SCORE')
print(f'{guest_result_c1}:{guest_result_c2} GUEST SCORE')

# resault = main_result_c2 - main_result_c1
# gresault = guest_result_c2 - guest_result_c1


total_c1r = main_result_c1 + guest_result_c1
total_c2r = main_result_c2 + guest_result_c2
print(f'{total_c1r}:{total_c2r} TOTAL SCORE')

if f == 1:
    if main_result_c1 > main_result_c2:
        print('main_result_c1 > main_result_c2')
        print(0)

    if main_result_c1 == main_result_c2:
        print('main_result_c1 == main_result_c2')
        if guest_result_c1 == guest_result_c2:
            print('guest_result_c1 == guest_result_c2:')
            if guest_result_c1 + guest_result_c2 == 0:
                print('guest_result_c1 + guest_result_c2 == 0:')
                print(1)
            else:
                print(0)
        if guest_result_c1 > guest_result_c2:
            print(0)
        if guest_result_c1 < guest_result_c2:
            print(main_result_c2 - main_result_c1)

    if main_result_c1 < main_result_c2:
        print('main_result_c1 < main_result_c2')
        if guest_result_c1 < guest_result_c2:
            print('guest_result_c1 < guest_result_c2')
            if guest_result_c1 == 0:
                print('guest_result_c1 == 0 and guest_result_c2 != 0')
                print(main_result_c2 - main_result_c1 + 1)
            else:
                print(main_result_c2 - main_result_c1)
        if guest_result_c1 > guest_result_c2:
            print('guest_result_c1 > guest_result_c2')
            print(main_result_c2 - main_result_c1)
        if guest_result_c1 == guest_result_c2:
            print('guest_result_c1 == guest_result_c2')
            if guest_result_c1 + guest_result_c2 == 0:
                print('guest_result_c1 + guest_result_c2 == 0')
                print(main_result_c2 - main_result_c1)
            else:
                print(main_result_c2 - guest_result_c1)

print('---TEST---')

setup_str = '''


main_result_c1 = g1_c1 + g2_c1
main_result_c2 = g1_c2 + g2_c2

guest_result_c1 = 0
guest_result_c2 = 0

if f == 2:
    guest_result_c1 = g1_c1
    guest_result_c2 = g2_c2
if f == 1:
    guest_result_c1 = g2_c1
    guest_result_c2 = g1_c2

print(f'{g1_c1}:{g1_c2}')
print(f'{g2_c1}:{g2_c2}')
print(f)
print(f'{main_result_c1}:{main_result_c2} MAIN SCORE')
print(f'{guest_result_c1}:{guest_result_c2} GUEST SCORE')

# resault = main_result_c2 - main_result_c1
# gresault = guest_result_c2 - guest_result_c1


total_c1r = main_result_c1 + guest_result_c1
total_c2r = main_result_c2 + guest_result_c2
print(f'{total_c1r}:{total_c2r} TOTAL SCORE')


if f == 1:
    if main_result_c1 > main_result_c2:
        print('main_result_c1 > main_result_c2')
        print(0)

    if main_result_c1 == main_result_c2:
        print('main_result_c1 == main_result_c2')
        if guest_result_c1 == guest_result_c2:
            print('guest_result_c1 == guest_result_c2:')
            if guest_result_c1 + guest_result_c2 == 0:
                print('guest_result_c1 + guest_result_c2 == 0:')
                print(1)
            else:
                print(0)
        if guest_result_c1 > guest_result_c2:
            print(0)
        if guest_result_c1 < guest_result_c2:
            print(main_result_c2 - main_result_c1)

    if main_result_c1 < main_result_c2:
        print('main_result_c1 < main_result_c2')
        if guest_result_c1 < guest_result_c2:
            print('guest_result_c1 < guest_result_c2')
            if guest_result_c1 == 0 and guest_result_c2 != 0:
                print('guest_result_c1 == 0 and guest_result_c2 != 0')
                print(main_result_c2 - main_result_c1 + 1)
            else:
                print(main_result_c2 - main_result_c1)
        if guest_result_c1 > guest_result_c2:
            print('guest_result_c1 > guest_result_c2')
            print(main_result_c2 - main_result_c1)
        if guest_result_c1 == guest_result_c2:
            print('guest_result_c1 == guest_result_c2')
            if guest_result_c1 + guest_result_c2 == 0:
                print('guest_result_c1 + guest_result_c2 == 0')
                print(main_result_c2 - main_result_c1)
            else:
                print(main_result_c2 - guest_result_c1)

if f == 2:
    if main_result_c1 > main_result_c2:
        print('main_result_c1 > main_result_c2')
        print(0)

    if main_result_c1 == main_result_c2:
        print('main_result_c1 == main_result_c2')
        if guest_result_c1 == guest_result_c2:
            print('guest_result_c1 == guest_result_c2:')
            if guest_result_c1 + guest_result_c2 == 0:
                print('guest_result_c1 + guest_result_c2 == 0:')
                print(1)
            else:
                print(0)
        if guest_result_c1 > guest_result_c2:
            print(0)
        if guest_result_c1 < guest_result_c2:
            print(main_result_c2 - main_result_c1)

    if main_result_c1 < main_result_c2:
        print('main_result_c1 < main_result_c2')
        if guest_result_c1 < guest_result_c2:
            print('guest_result_c1 < guest_result_c2')
            if guest_result_c1 == 0 and guest_result_c2 != 0:
                print('guest_result_c1 == 0 and guest_result_c2 != 0')
                print(main_result_c2 - main_result_c1 + 1)
            else:
                print(main_result_c2 - main_result_c1)
        if guest_result_c1 > guest_result_c2:
            print('guest_result_c1 > guest_result_c2')
            print(main_result_c2 - main_result_c1)
        if guest_result_c1 == guest_result_c2:
            print('guest_result_c1 == guest_result_c2')
            if guest_result_c1 + guest_result_c2 == 0:
                print('guest_result_c1 + guest_result_c2 == 0')
                print(main_result_c2 - main_result_c1)
            else:
                print(main_result_c2 - guest_result_c1)


'''

import itertools

digits = [0, 1, 2, 3, 4, 5]
lst = list(itertools.combinations_with_replacement(digits, 4))
print(lst)

digits = [0, 1, 2, 3, 4, 5]
lst = list(itertools.combinations(digits, 4))
print(lst)
print(len(lst))

g1_c1 = 0
g1_c2 = 0
g2_c1 = 0
g2_c2 = 0
f = 2

count = 1

# for v in lst:  # я получил кортежи
#     g1_c1 = v[0]
#     g1_c2 = v[1]
#     g2_c1 = v[2]
#     g2_c2 = v[3]
#
#     print(f'\nTEST N:{count} args:{v}')
#     count += 1
#
#     exec(setup_str)


# print(g1_c1, g1_c2, g2_c1, g2_c2, f)


print('\n------')

# ATRS ********************************************************************************

g1_c1, g1_c2, g2_c1, g2_c2, f = 0, 2, 0, 3, 1

main_result_c1 = g1_c1 + g2_c1
main_result_c2 = g1_c2 + g2_c2

guest_result_c1 = 0
guest_result_c2 = 0

if f == 2:
    guest_result_c1 = g1_c1
    guest_result_c2 = g2_c2
if f == 1:
    guest_result_c1 = g2_c1
    guest_result_c2 = g1_c2

print(f'{g1_c1}:{g1_c2}')
print(f'{g2_c1}:{g2_c2}')
print(f)
print(f'{main_result_c1}:{main_result_c2} MAIN SCORE')
print(f'{guest_result_c1}:{guest_result_c2} GUEST SCORE')

# resault = main_result_c2 - main_result_c1
# gresault = guest_result_c2 - guest_result_c1


total_c1r = main_result_c1 + guest_result_c1
total_c2r = main_result_c2 + guest_result_c2
print(f'{total_c1r}:{total_c2r} TOTAL SCORE')

if main_result_c1 > main_result_c2:
    print(0)

if main_result_c1 == main_result_c2:
    if guest_result_c1 < guest_result_c2:
        pass

    if guest_result_c1 == guest_result_c2:
        if main_result_c1 + main_result_c2 == 0:
            print(main_result_c2 - main_result_c1 + 1)
        else:
            if f == 1:
                print(main_result_c2 - main_result_c1 + 1)
            if f == 2:
                print(0)

    if guest_result_c1 > guest_result_c2:
        print(0)

if main_result_c1 < main_result_c2:
    if guest_result_c1 < guest_result_c2:
        if f == 1:
            print(main_result_c2 - main_result_c1 + 1)
        if f == 2:
            print(main_result_c2 - main_result_c1)

    if guest_result_c1 == guest_result_c2:
        print(main_result_c2 - main_result_c1)

    if guest_result_c1 > guest_result_c2:
        print(main_result_c2 - main_result_c1 + 1)

# можно попробовать сравнивать гостевые голы


print('\n----:(------\n')

g1_c1, g1_c2, g2_c1, g2_c2, f = 4, 5, 2, 4, 2

#
# g1_c1, g1_c2 = map(int, input().split(':'))
# g2_c1, g2_c2 = map(int, input().split(':'))
# f = int(input())


main_result_c1 = g1_c1 + g2_c1
main_result_c2 = g1_c2 + g2_c2

guest_result_c1 = 0
guest_result_c2 = 0

if f == 2:
    guest_result_c1 = g1_c1
    guest_result_c2 = g2_c2
if f == 1:
    guest_result_c1 = g2_c1
    guest_result_c2 = g1_c2

print(f'{g1_c1}:{g1_c2}')
print(f'{g2_c1}:{g2_c2}')
print(f)
print(f'{main_result_c1}:{main_result_c2} MAIN SCORE')
print(f'{guest_result_c1}:{guest_result_c2} GUEST SCORE')

total_c1r = main_result_c1 + guest_result_c1
total_c2r = main_result_c2 + guest_result_c2
print(f'{total_c1r}:{total_c2r} TOTAL SCORE')

if main_result_c1 > main_result_c2:
    print(0)

if main_result_c1 < main_result_c2:
    x = main_result_c2 - main_result_c1
    guest_result_c1 = x
    print(f'{guest_result_c1}:{guest_result_c2} NEW - GUEST SCORE')
    if guest_result_c1 > guest_result_c2:
        if f == 1:
            print(x)
        if f == 2:
            print(x + 1)
    if guest_result_c1 == guest_result_c2:
        if f == 1:
            print(x)
        if f == 2:
            print(x + 1)

if main_result_c1 == main_result_c2:
    if guest_result_c1 == guest_result_c2:
        print(1)
    if guest_result_c1 > guest_result_c2:
        print(0)
    if guest_result_c1 < guest_result_c2:
        print(1)

# g1_c1, g1_c2 = map(int, input().split(':'))
# g2_c1, g2_c2 = map(int, input().split(':'))
# f = int(input())


print('\n---SEREJA---')

# G1, G2 = map(int, input().split(':'))
# F1, F2 = map(int, input().split(':'))
# HOME_GUESTS = int(input())

G1 = 2  # Количество забитых мячей 1-й командой в первом матче
G2 = 2  # Количество забитых мячей 2-й командой в превом матче
F1 = 1  # Количество забитых мячей 1-й командой во втором матче
F2 = 1  # Количество забитых мячей 2-й командой во втором матче
HOME_GUESTS = 2  # Первая встреча 1-й команды была: 1 - ДОМА, 2 - В ГОСТЯХ

print(f'{G1}:{G2}')
print(f'{F1}:{F2}')
print(HOME_GUESTS)

X = None  # Количество мячей которое необходимо забить первой команде, чтобы победить
a = None  # Количество голов, которое необходимо забить первой команде, чтобы сравнять счет по итогу двух матчей

if (G1 + F1) > (G2 + F2):  # Если первая команда выигрывает по итогу 2 матчей
    X = 0  # то ей не надо забивать
else:  # Если по итогу 2 матчей первая команда проигрывает или играет вничью то
    a = (G2 + F2) - (G1 + F1)  # тогда считаем количество голов необходимых первой команде,
    # чтобы сравнять счет по итогу двух матчей
    if HOME_GUESTS == 1:  # Если первая игра у первой команды был ДОМА то
        if (F1 + a) > G2:  # Если при итоговой ничье первая команда забила больше голов В ГОСТЯХ
            X = a  # берем а (количество голов необходимых первой команде, чтобы сравнять счет по итогу двух матчей)
        else:
            X = a + 1  # иначе нужно забить на 1 гол больше
    if HOME_GUESTS == 2:  # Если первая игру у первой команды В ГОСТЯХ
        if G1 > F2:  # Если при итоговой ничье первая команда забила в гостях больше голов
            X = a  # берем а
        else:
            X = a + 1  # иначе нужно забить на 1 гол больше

print(X)
