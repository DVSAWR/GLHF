'''


'''


print('----DONE CHAT GPT------')

def binary_search(prefix_sum, target):
    low = 0
    high = len(prefix_sum)
    while low < high:
        mid = (low + high) // 2
        if prefix_sum[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

n, m = map(int, input().split())
orcs = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + orcs[i]

for _ in range(m):
    l, s = map(int, input().split())
    result = binary_search(prefix_sum, prefix_sum[l-1] + s) - 1
    if result < n and prefix_sum[result] - prefix_sum[l-1] >= s:
        print(result)
    else:
        print("-1")

# 5 2
# 1 3 5 7 9
# 2 4
# 1 3