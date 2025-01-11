# Ch. 1


def binary_search(mylist, item) -> None:
    """
    Bla bla bla.
    """
    low = 0
    high = len(mylist) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = mylist[mid]
        if guess == item:
            return f"{item} IN {mylist} INDEX: {mid}"
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(True)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 3))
