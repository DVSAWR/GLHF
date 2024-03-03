import random

# A. Покраска деревьев
#
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
#
# Вася и Маша участвуют в субботнике и красят стволы деревьев в белый цвет. Деревья растут вдоль
# улицы через равные промежутки в 1 метр. Одно из деревьев обозначено числом ноль, деревья по одну
# сторону занумерованы положительными числами 1,2 и т.д., а в другую — отрицательными − 1,−2 и т.д.
# Ведро с краской для Васи установили возле дерева P, а для Маши — возле дерева Q. Ведра с краской очень
# тяжелые и Вася с Машей не могут их переставить, поэтому они окунают кисть в ведро и уже с
# этой кистью идут красить дерево. Краска на кисти из ведра Васи засыхает, когда он удаляется
# от ведра более чем на V метров, а из ведра Маши — на M метров. Определите, сколько
# деревьев может быть покрашено.


# P, V = input().split()
# Q, M = input().split()
# P = int(P)
# V = int(V)
# Q = int(Q)
# M = int(M)


P = 0
V = 7
Q = 12
M = 5


# print('list 1\t', list(range(P - V, P + V + 1)))
# print('list 2\t', list(range(Q - M, Q + M + 1)))
# ptrees = set(list(range(P - V, P + V + 1)) + list(range(Q - M, Q + M + 1)))
# print('set\t\t', ptrees)


def ptrees(P, V, Q, M):
    x = len(set(list(range(P - V, P + V + 1)) + list(range(Q - M, Q + M + 1))))
    return x


print(ptrees(P, V, Q, M))


print('----')

P = -3
V = 1
Q = 3
M = 1

v_left = P - V
v_right = P + V
v_count = 2 * V + 1
print(v_left, v_right, v_count)

m_left = Q - M
m_right = Q + M
m_count = 2 * M + 1
print(m_left, m_right, m_count)


t_count = v_count + m_count
print(t_count)
t_count2 = 2 * (V + M + 1)  # QWE
print(t_count2)

print('----')
s_left = min(v_left, m_left)
s_right = max(v_right, m_right)
s_count = s_right - s_left + 1


print(s_left, s_right)
print(s_count)

s_count2 = max(v_right, m_right) - min(v_left, m_left) + 1
print(s_count2)
s_count2 = max(P + V, Q + M) - min(P - V, Q - M) + 1
print(s_count2)



print('-------DONE---------')

P, V = input('ENTER: ').split()
Q, M = input('ENTER: ').split()

P = int(P)
V = int(V)
Q = int(Q)
M = int(M)

if P + V < Q - M or Q + M < P - V:
    print(2 * (V + M + 1))
else:
    print(max(P + V, Q + M) - min(P - V, Q - M) + 1)
