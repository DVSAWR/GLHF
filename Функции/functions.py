def preview(x):
    print(f'\n---- {x} ----')


preview('abs()')

complex_number = (3 + 10j)
abs_complex_number = abs(complex_number)
print(f"Абсолютное значение {complex_number} это {abs_complex_number}")
print(complex(complex_number.real))
print(complex(complex_number.imag))

x = 42.42
abs_x = abs(x)
print(f"Абсолютное значение {x} это {abs_x}")
x = -42.42
abs_x = abs(x)
print(f"Абсолютное значение {x} это {abs_x}")

preview('all()')
print(all([True, True, True]))
print(all([True, False, True]))

num1 = [1, 2, 3, 4, 5, 6, 7]
num2 = [1, 2.0, 3.1, 4, 5, 6, 7.9]
print(all([type(x) is int for x in num1]))
print(all([type(x) is int for x in num2]))

preview('any()')
num1 = range(0, 20, 2)
num2 = range(0, 15, 2)
print(any([x > 15 for x in num1]))
print(any([x > 15 for x in num2]))


preview('ascii()')
line = 'My name is Даниил'
x = ascii(line)
print(x)



