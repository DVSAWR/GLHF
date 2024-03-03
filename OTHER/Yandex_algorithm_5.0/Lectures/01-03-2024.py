# RAM машина(упрощенно)
#01.03.2024
# сложность тестирование особые случаи
# линейный поиск
# множества и словари
# бинарный поиск


# чтение \ запись \ инициализация памяти стоит одну операцию
# арефметически и логические операции с одной ячейкой патмяти
#
# сложность алгоритма
#  сложность алгоритма порядок количесчтва действи в зависиомти от размера входных данных
#
# часто применяют О-нотацию - нестрогая оценка сверху
#
# for i = 1, n
#     for i = 1, n
# == O(n**2)
#
# Суть хотим понимать во сколько раз замлится наша программа при увеличении размера входных данных
#
#
# for i in range(n):
#     for j in range(n):
#         ans += i + j
#
# == COMPLEXITY O(n**2)
#
# for i in range(n):
#     for j in range(n):
#         i = i//1
#         j = j//5+j%5
#         ans = ans + i
#         ans = ans + j
#
# == COMPLEXITY O(n ** 2)


# dist = []
# n = int(input())
# for i in range(n):
#     dist.append(list(map(int, input().split())))
# for via in range(n):
#     for fr in range(n):
#         for to in range(n):
#             dist[fr][to] = min(matr[fr][to], matr[fr][via] + matr[via][to])
# for i in range(n):
#     if dist[i][i] < 0:
#         print(i)
#
#
# == COMPLEXITY O(n**3)

#
# Самый частый символ
# Дана строка (в кодировке UTF-8) найти самый часто встречающийся в ней символ
#
# Если таких символов несколько - найти любой

#
# s = input()
# ans = ''
# for i in range(len(s)):
#     nowcnt = 0
#     for j in range(len(s)):
#         if s[i] == s[j]:
#             nowcnt += 1
#     if nowcnt > anscnt:
#         ans = s[i]
#         anscnt = nowcnt
# print(ans)
#
# == COMPLEXITY O(n**2)
# == MEMORY O(n)

#
# s = input()
# ans = ''
# snscnt = 0
# for now in set(s):
#     nowcnt = 0
#     for j in range(len(s)):
#         if now == s[j]:
#             nowcnt += 1
#     if nowcnt > anscnt:
#         ans = now
#         anscnt = nowcnt
# print(ans)
#
# == COMPLEXITY O(nk)
# k - размер алфавита символов l <= n
# == MEMORY O(n)

#
# s = input()
# ans = ''
# anscnt = 0
# symcnt = {}
# for now in s:
#     if now not in symcnt:
#         symcnt[now] = 0
#     symcnt[now] += 1
#     if symcnt[now] > anscnt:
#         ans = now
#         anscnt = symcnt[now]
# print(ans)
#
# == COMPLEXITY  O(n)  ---(O(n + k))
# == MEMORY O(n)


# Потребление памяти не может быть больше времени


# ОСОБЫЕ СЛУЧАИ
# seq = list(map(int, input().split()))
# if len(seq) == 0:
#     print(0)
# else:
#     seqsum = seq[0]
#     for i in range(1, len(seq)):
#         seqsum += seq[i]
#
# Правильно (упрощенно)
# seq = list(map(int, input().split()))
# seqsum = 0
# for i in range(len(seq)):
#     seqsum += seq[i]
# print(seqsum)


#ТЕСТИРОВАНИЕ
# Тесты из условия(если есть)
# Общие случаи
# Особые случаи
#
# !! Советы по составлению тестов
# Если есть примеры реши их руками и сверь ответ Если не совпадает то либюо правльных ответов может бюытьб несколь либо ты непраильно понял задачу
#
# сначала составь несколько примеров и реши заджачу ркуами чтобы лучше понять условия чтобы потом было с чем сравнить
#
# проверь последовательность из одного элоемента и пустую последовательность
#
# "краевые эффекты" - проверь что программа работает корректо в начале и вконце последовательности сделай тиесты чтобы ответ находися на первом и на последжнем месте в последовательности
#
# составь покрытие всех ветвлений так, чтобы был тест который входит в каждый if else
#
# подбери тесты чтобы не было ни одного входа в цикл
#
# один тест - одна возможная ошибка

#
# ПРИМЕР СТРЕСС-ТЕСТИРОВАНИЯ
# from random import sample
#
# def mysort(a, n):
#     for i in range(n - 1):
#         for j in range(n - 1):
#             if a[j] > a[j + 1]:
#                 a[i], a[i + 1] = a[i + 1], a[i]
#
#
# while True:
#     a = sample(range(0, 10), 5)
#     b = a.copy()
#     mysort(a, len(a))
#     b.sort()
#     print('mysort:', a, 'standart sort:', b)
#     if a != b:
#         break
#


