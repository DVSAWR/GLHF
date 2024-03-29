'''


'''

print('----DONE------')

from itertools import accumulate

n, m = map(int, input().split())

a = list(map(int, input().split()))

summa = list(accumulate([0] + a))

for _ in range(m):
    leng, s = map(int, input().split())

    l = 0
    r = n - leng + 1
    while l < r - 1:
        mid = (l + r) // 2
        if summa[mid + leng] - summa[mid] > s:
            r = mid
        else:
            l = mid

    if summa[l + leng] - summa[l] == s:
        print(l + 1)
    else:
        print(-1)

print('------yandex------')

n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))

prefsum = [0] * (n + 1)
for i in range(1, n + 1):
    prefsum[i] = prefsum[i - 1] + a[i]

ans = []

for i in range(q):
    orccnt, orcsum = map(int, input().split())
    l = 1
    r = n + 1 - orccnt
    while l < r:
        m = (l + r) // 2
        if prefsum[m + orccnt - 1] - prefsum[m - 1] >= orcsum:
            r = m
        else:
            l = m + 1
    if prefsum[l + orccnt - 1] - prefsum[l - 1] == orcsum:
        ans.append(l)
    else:
        ans.append(-1)

print(*ans)
