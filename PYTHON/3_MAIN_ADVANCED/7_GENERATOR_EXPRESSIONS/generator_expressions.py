print('\n---- Generator ----')


def generator():
    t = 1
    print('RESULT:', t)
    yield t

    t += 1
    print('RESULT:', t)
    yield

    t += 1
    print('RESULT:', t)
    yield


call = generator()
next(call)
next(call)
next(call)

print('\n---- Generator expression allows creating a generator without a yield keyword ----')
generator = (number ** 2 for number in range(6))
for number in generator:
    print(number, end=' ')
print('')

print('\n---- Generate a list using generator expressions ----')
string = 'geek'
my_list = list(string[i] for i in range(len(string) - 1, -1, -1))
print(my_list)

