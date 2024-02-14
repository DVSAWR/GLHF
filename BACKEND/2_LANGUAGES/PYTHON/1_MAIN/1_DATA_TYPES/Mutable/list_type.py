list()
# []
print([])
# []
print([1, 'a', 10, 'b', '105'])
# [1, 'a', 10, 'b', '105']

list('abc')
# ['a',' b',' c']

list((1, 2, 3))
# [1, 2, 3]

list({1, 2, 3})
# [1, 2, 3]

list(range(5))
# [0, 1, 2, 3, 4]

x = ['55', '11', '25', '15', '9']
int_list = [int(i) for i in x]
print(int_list)
# [11, 15, 25, 55, 9]


# SMTH
y = []
print(y)
for i in x:
    y.append(i)
print(y)



