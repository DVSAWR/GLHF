'''


'''


print('----DONE CHAT GPT------')

n, m = map(int, input().split())
orc_count = list(map(int, input().split()))

prefix_sum = [0] * (n+1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + orc_count[i]

def find_starting_group(prefix_sum, s):
    left, right = 0, len(prefix_sum) - 1
    while left < right:
        mid = (left + right) // 2
        if prefix_sum[mid] < s:
            left = mid + 1
        else:
            right = mid
    return left if prefix_sum[left] >= s else -1

for _ in range(m):
    l, s = map(int, input().split())
    start_group = find_starting_group(prefix_sum, s)
    if start_group == -1 or start_group + l - 1 > n:
        print(-1)
    else:
        print(start_group)

# 5 2
# 1 3 5 7 9
# 2 4
# 1 3