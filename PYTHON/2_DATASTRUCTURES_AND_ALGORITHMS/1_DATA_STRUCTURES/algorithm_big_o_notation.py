import matplotlib.pyplot as plt
import time

def preview(x):
    print(f'\n---- {x} ----')


preview('O(1)')
# CONSTANT - The complexity of an algorithm is said to be constant if the steps required to complete the execution of an algorithm remain constant, irrespective of the number of inputs. The constant complexity is denoted by O(c) where c can be any constant number.

def contstant_algorithm(i):
    result = i[0] * i[0]
    print(result)

starttime = time.time()
contstant_algorithm([4, 5, 6, 8])
endtime = time.time() - starttime
print(endtime)


csteps = []
def constant(n):
    return 1

for i in range(1, 100):
    csteps.append(constant(i))

plt.plot(csteps)
plt.xlabel('INPUTS')
plt.ylabel('STEPS')



preview('O(log(n))')
# LOGARITHMIC - A logarithmic algorithm halves the list every time it’s run.



def binary_search(lst, item):
    first = 0
    last = len(lst)-1
    found = False
    count = 1

    while first <= last and not found:
        midpoint = (first + last)//2
        if lst[midpoint] == item:
            found = True
            print(midpoint)
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
                count += 1
            else:
                first = midpoint + 1
                count += 1
    return found, f'count: {count}'


a = list(range(101))
print(a)
print(binary_search(a, 24))


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print('incorrect input')
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))

lst = []
for i in range(11):
    lst.append(fibonacci(i))
print(lst)





preview('O(n)')
# LINEAR - Linear time algorithms mean that every single element from the input is visited exactly once, O(n) times. As the size of the input, N, grows our algorithm’s run time scales exactly with the size of the input.

def linear_algorithm(items):
    for i in items:
        print(i)

starttime = time.time()
linear_algorithm([4, 5, 6, 8])
endtime = time.time() - starttime
print(endtime)



lsteps = []
def linear(n):
    return n

for i in range(1, 100):
    lsteps.append(linear(i))

plt.plot(lsteps)



preview('O(nlog(n))')
# LOG LINEAR - It falls between O(n) and O(n2). This is the fastest time possible for a comparison sort. We cannot get any faster unless we use some special property, like Radix sort. O(n log n) is the fastest comparison sort time.




preview('O(n²)')
# QUADRATIC - The complexity of an algorithm is said to be quadratic when the steps required to execute an algorithm are a quadratic function of the number of items in the input. Quadratic complexity is denoted as O(n²):

def quadratic_algorithm(items):
    for i in items:
        for i2 in items:
            print(i, '-', i2)



starttime = time.time()
quadratic_algorithm([4, 5, 6, 8])
endtime = time.time() - starttime
print(endtime)



preview('O(n³)')
# CUBIC - A triple nested loop is O(n3).

preview('O(nˣ)')
# POLYNOMIAL - O(n²), O(n³), ..., O(nⁿ⁺¹) Notice how polynomial time dwarfs the others? Polynomial time is a polynomial function of the input. A polynomial function looks like n2 or n3 and so on. If one loop through a list is O(n), 2 loops must be O(n2). For each loop, we go over the list once. For each item in that list, we go over the entire list once. Resulting in n2 operations.


preview('O(2ⁿ)')
# EXPONENTIAL - Exponential time is 2n, where 2 depends on the permutations involved.



preview('O(n!)')
# FACTORIAL - This time complexity is often used as a joke, referring to Bogo Sort. I have yet to find a real-life (not-a-joke) algorithm that runs in O(n!) that isn’t an algorithm calculating O(6!) or the likes.



plt.legend(['constant', 'linear', 'quadratic'])
