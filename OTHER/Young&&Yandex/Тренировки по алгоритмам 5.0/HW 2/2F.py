'''

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Развлекательный телеканал транслирует шоу «Колесо Фортуны». В процессе игры участники шоу крутят большое колесо, разделенное на сектора. В каждом секторе этого колеса записано число. После того как колесо останавливается, специальная стрелка указывает на один из секторов. Число в этом секторе определяет выигрыш игрока.

Юный участник шоу заметил, что колесо в процессе вращения замедляется из-за того, что стрелка задевает за выступы на колесе, находящиеся между секторами. Если колесо вращается с угловой скоростью v градусов в секунду, и стрелка, переходя из сектора X к следующему сектору, задевает за очередной выступ, то текущая угловая скорость движения колеса уменьшается на k градусов в секунду. При этом если v ≤ k, то колесо не может преодолеть препятствие и останавливается. Стрелка в этом случае будет указывать на сектор X.

Юный участник шоу собирается вращать колесо. Зная порядок секторов на колесе, он хочет заставить колесо вращаться с такой начальной скоростью, чтобы после остановки колеса стрелка указала на как можно большее число. Колесо можно вращать в любом направлении и придавать ему начальную угловую скорость от a до b градусов в секунду.

Требуется написать программу, которая по заданному расположению чисел в секторах, минимальной и максимальной начальной угловой скорости вращения колеса и величине замедления колеса при переходе через границу секторов вычисляет максимальный выигрыш.

Формат ввода
Первая строка входного файла содержит целое число n — количество секторов колеса (3 ≤ n ≤ 100).

Вторая строка входного файла содержит n положительных целых чисел, каждое из которых не превышает 1000 — числа, записанные в секторах колеса. Числа приведены в порядке следования секторов по часовой стрелке. Изначально стрелка указывает на первое число.

Третья строка содержит три целых числа: a, b и k (1 ≤ a ≤ b ≤ 109, 1 ≤ k ≤ 109).

Формат вывода
В выходном файле должно содержаться одно целое число — максимальный выигрыш.

Пример 1
Ввод	Вывод
5
1 2 3 4 5
3 5 2
5
Пример 2
Ввод	Вывод
5
1 2 3 4 5
15 15 2
4
Пример 3
Ввод	Вывод
5
5 4 3 2 1
2 5 2
5
Примечания
В первом примере возможны следующие варианты: можно придать начальную скорость колесу равную 3 или 4, что приведет к тому, что стрелка преодолеет одну границу между секторами, или придать начальную скорость равную 5, что позволит стрелке преодолеть 2 границы между секторами. В первом варианте, если закрутить колесо в одну сторону, то выигрыш получится равным 2, а если закрутить его в противоположную сторону, то — 5. Во втором варианте, если закрутить колесо в одну сторону, то выигрыш будет равным 3, а если в другую сторону, то — 4.

Во втором примере возможна только одна начальная скорость вращения колеса — 15 градусов в секунду. В этом случае при вращении колеса стрелка преодолеет семь границ между секторами. Тогда если его закрутить в одном направлении, то выигрыш составит 4, а если в противоположном направлении, то — 3.

Наконец, в третьем примере оптимальная начальная скорость вращения колеса равна 2 градусам в секунду. В этом случае стрелка вообще не сможет преодолеть границу между секторами, и выигрыш будет равен 5.

'''

print('\n---------------so---------------\n')

# n = int(input())
# sectors = tuple(map(int, input().split()))
# a, b, k = map(int, input().split())

# n = 5
# sectors = [1, 2, 3, 4, 5]
# a, b, k = 3, 5, 2

# n = 5
# sectors = [1, 2, 3, 4, 5]
# a, b, k = 15, 15, 2

# n = 5
# sectors = [5, 4, 3, 2, 1]
# a, b, k = 2, 5, 2

n = 34
sectors = [56, 1000, 528, 720, 895, 209, 805, 65, 370, 923, 541, 431, 528, 778, 670, 761, 794, 49, 488, 171, 438, 325, 57, 717, 293, 847, 535, 306, 398, 757, 888, 56, 916, 999]
a, b, k = 391, 901, 26


spin_power = tuple(range(a, b + 1))


print(sectors)
print(spin_power)

max_value = min(sectors)
max_value2 = max(sectors)
y = None

for i in spin_power:
    print('PRINT i >>> ', i)
    if i % 2 != 0:
        x = i // k

        if x >= n:
            x %= n

            print(x, '< X AFTER x %= n')

        print(f'{i} = {x} > right spin sector {sectors[x]} > left spin sector {sectors[-x]}')

        max_sector = max(sectors[x], sectors[-x])

        if max_sector == max_value2:
            max_value = max_sector
            print('>> BREAK !!')
            break

        elif max_sector > max_value:
            max_value = max_sector

    if i % 2 == 0:
        x = (i - 1) // k
        print(i // k)
        print(x, '< FIRST x EVEN')

        if x >= n:
            x %= n

            print(x, '< x AFTER x %= n')

        print(f'{i} = {x} > right spin sector {sectors[x]} > left spin sector {sectors[-x]}')

        max_sector = max(sectors[x], sectors[-x])

        if max_sector == max_value2:
            max_value = max_sector
            print('>> BREAK !!')
            break

        elif max_sector > max_value:
            max_value = max_sector


print('\nANSWER:', max_value)



print('\n-------????-------')


n = 34
sectors = [56, 1000, 528, 720, 895, 209, 805, 65, 370, 923, 541, 431, 528, 778, 670, 761, 794, 49, 488, 171, 438, 325, 57, 717, 293, 847, 535, 306, 398, 757, 888, 56, 916, 999]
a, b, k = 391, 901, 26


# n = 5
# sectors = [1, 2, 3, 4, 5]
# a, b, k = 3, 5, 2
# #
# n = 5
# sectors = [1, 2, 3, 4, 5]
# a, b, k = 15, 15, 2
# #
# n = 5
# sectors = [5, 4, 3, 2, 1]
# a, b, k = 2, 5, 2


spin_power = tuple(range(a, b + 1))

print('SECTORS:', sectors)
print('')
print(spin_power)
print('')

max_sector = max(sectors)

spin_power_2 = [0]


for i in spin_power:
    if i % 2 != 0:
        x = i // k
        if x >= n:
            x %= n

        max_value = max(sectors[x], sectors[-x])

        if max_value == spin_power_2[-1]:
            continue

        if max_value == max_sector:
            spin_power_2.append(max_value)
            break

        spin_power_2.append(max_value)

    if i % 2 == 0:
        x = (i - 1) // k
        if x >= n:
            x %= n

        max_value = max(sectors[x], sectors[-x])
        if max_value == spin_power_2[-1]:
            continue

        if max_value == max_sector:
            spin_power_2.append(max_value)
            break

        spin_power_2.append(max_value)


print(spin_power_2)


print('')
print(max(spin_power_2))


print('\nC++')
# #include <cstdio>
# #include <vector>
# #include <algorithm>
# #include <cassert>
#
# int main(){
#   int n;
#   scanf("%d", &n);
#   std::vector<int> win(n);
#   for (int i = 0; i < n; i++) {
#       scanf("%d", &win[i]);
#   }
#   int minSpeed, maxSpeed, speedDec;
#   scanf("%d %d %d", &minSpeed, &maxSpeed, &speedDec);
#   int minShift = (minSpeede - 1) / speedDec;
#   int toVisit = std::min(n, (maxSpeed - 1) / speedDec + 1 - minShift);
#   assert(toVisit > 0);
#   int max = 0;
#   for (int di = -1; di <= 1; di += 2) {
#       int pos = di * minShift;
#       pos %= n;
#       pos += n;
#       pos %= n;
#       max = std::max(max, win[pos]);
#       for (int i = 0; i < toVisit; i++){
#           pos += di;
#           pos %= n;
#           pos += n;
#           pos %= n;
#       }
#   }
#   asert(max > 0);
#   printf("%d", max)
#   return 0;
# }

print('\nconvert C++')

import sys

n = 34
win = [56, 1000, 528, 720, 895, 209, 805, 65, 370, 923, 541, 431, 528, 778, 670, 761, 794, 49, 488, 171, 438, 325, 57, 717, 293, 847, 535, 306, 398, 757, 888, 56, 916, 999]
minSpeed, maxSpeed, speedDec = 391, 901, 26

minShift = (minSpeed - 1) // speedDec
toVisit = min(n, (maxSpeed - 1) // speedDec + 1 - minShift)

assert toVisit > 0

max_val = 0

for di in [-1, 1]:
    pos = di * minShift
    pos %= n
    pos += n
    pos %= n
    max_val = max(max_val, win[pos])
    for i in range(toVisit):
        pos += di
        pos %= n
        pos += n
        pos %= n

assert max_val > 0
print(max_val)

