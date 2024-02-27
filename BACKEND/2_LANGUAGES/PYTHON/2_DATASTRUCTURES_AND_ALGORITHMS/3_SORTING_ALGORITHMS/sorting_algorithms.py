from random import randint
from timeit import repeat


def preview(x):
    print(f'\n---- {x} ----')


preview('PRE')

array = [8, 2, 6, 4, 5]
print(array)
print(sorted(array))

ARRAY_LENGTH = 1000


def run_sorting_algorithm(algorithm, array):
    setup_code = f'from __main__ import {algorithm}'

    stmt = f'{algorithm}({array})'

    times = repeat(setup=setup_code, stmt=stmt, repeat=2, number=10)

    print(f'Algorithm: {algorithm}. Minimum execution time: {min(times)}')


def time_test(algorithm):
    random_array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print('\nGenerated array length:', len(random_array))
    run_sorting_algorithm(algorithm=f'{algorithm}', array=random_array)


preview('BUBBLE SORT')
array = [8, 2, 6, 4, 5]


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array


print(array)
print(bubble_sort(array))

time_test('bubble_sort')

preview('INSERTION SORT')
array = [8, 2, 6, 4, 5]


def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]

        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


print(array)
print(insertion_sort(array))

time_test('insertion_sort')

preview('MERGE SORT')
array = [8, 2, 6, 4, 5]


def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))


print(array)
print(merge_sort(array))

time_test('merge_sort')

preview('QUICKSORT')
array = [8, 2, 6, 4, 5]


def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


print(array)
print(quicksort(array))

time_test('quicksort')

preview('TIMSORT')
array = [8, 2, 6, 4, 5]


def modif_insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]

        j = i - 1

        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


def timsort(array):
    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
        modif_insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size = min_run

    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            merged_array = merge(left=array[start:midpoint + 1], right=array[midpoint + 1:end + 1])

            array[start:start + len(merged_array)] = merged_array

        size *= 2

    return array


print(array)
print(timsort(array))

time_test('timsort')




print('\n\n#ggwp')
