print(())
# ()
print(tuple())
# ()
print(105,)
# (105,)
print(1, 'a', 3, 'b')
# (1, 'a', 3, 'b')

# Преобразование строки str в кортеж тип tuple
print(tuple('abc'))
# ('a',' b',' c')

# Преобразование списка list в кортеж тип tuple
print(tuple([1, 2, 3]))
# (1, 2, 3)

# Преобразование множества set в кортеж тип tuple
print(tuple({1, 2, 3}))
# (1, 2, 3)

# Преобразование генератора в кортеж тип tuple
print(tuple(range(5)))
# (0, 1, 2, 3, 4)
