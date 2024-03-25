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
