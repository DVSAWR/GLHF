'''

Костя успешно прошел собеседование и попал на стажировку в отдел разработки сервиса «Музыка».
Конкретно ему поручили такое задание — научиться подбирать плейлист для группы друзей, родственников или коллег. При этом нужно подобрать такой плейлист, в который входят исключительно нравящиеся всем членам группы песни.
Костя очень хотел выполнить это задание быстро и качественно, но у него не получается. Помогите ему написать программу, которая составляет плейлист для группы людей.

Формат ввода
В первой строке расположено одно натуральное число
n
(
1
≤
n
≤
2
⋅
1
0
5
)
, где
n
 – количество человек в группе.
В следующих
2
⋅
n
 строках идет описание любимых плейлистов членов группы. По
2
 строки на каждого участника.
В первой из этих
2
-х строк расположено число
k
i
 — количество любимых треков
i
-го члена группы. В следующей строке расположено
k
i
 строк через пробел — названия любимых треков
i
-го участника группы.
Каждый трек в плейлисте задан в виде строки, все строки уникальны, сумма длин строк не превосходит
2
⋅
1
0
6
. Строки содержат большие и маленькие латинские буквы и цифры.

Формат вывода
Выведите количество, а затем сам список песен через пробел — список треков, которые нравятся каждому участнику группы. Ответ необходимо отсортировать в лексикографическом порядке!
Пример 1
Ввод	Вывод
1
2
GoGetIt Life
2
GoGetIt Life
Пример 2
Ввод	Вывод
2
2
Love Life
2
Life GoodDay
1
Life

'''

print('\n--------so-------')

# 2
# 2
# Love Life
# 2
# Life GoodDay

# 1
# Life


#
# n = 3
#
# music = []
#
# for i in range(n):
#     # k = int(input())
#     music += input().split()
#
# print(music)
#
# duplicate_songs = {}
#
# for i in music:
#     if i in duplicate_songs:
#         duplicate_songs[i] += 1
#     else:
#         duplicate_songs[i] = 1
#
#
# print(duplicate_songs)
#
# answer = []
# for k, v in duplicate_songs.items():
#     if v == n:
#         answer.append(k)
#
# print(len(answer))
# print(''.join(sorted(answer)))


print('-----DONE------')

n = int(input())

music = []

for i in range(n):
    k = int(input())
    music += input().split()

duplicate_songs = {}
for i in music:
    if i in duplicate_songs:
        duplicate_songs[i] += 1
    else:
        duplicate_songs[i] = 1

answer = []

for k, v in duplicate_songs.items():
    if v == n:
        answer.append(k)

print(len(answer))
print(' '.join(sorted(answer)))

# 1
# 2
# GoGetIt Life

print('---------yandex----------')

n = int(input())
k = int(input())
ans = set(input().split())

for i in range(n - 1):
    k = int(input())
    now = set(input().split())
    ans = ans & now

print(len(ans))
print(*sorted(ans))
