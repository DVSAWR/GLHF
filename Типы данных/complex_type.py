x = 5
y = 3
z = complex(x, y)

print("The real part of complex number is : ", end="")
print(z.real)

print("The imaginary part of complex number is : ", end="")
print(z.imag)

print(type(z))

print(complex())
# 0j
print(complex(1))
# (1+0j)
print(complex(1.5))
# (1.5+0j)
print(complex(3, 5))
# (3+5j)
print(complex(1, 2e-2))
# (1+0.02j)

print(complex(' 1+2j '))
# (1+2j)
print(complex('   0.1+2.0j'))
# (0.1+2j)
print(complex(' .1+2.j     '))
# (0.1+2j)
print(complex('    1e3+2e-3j'))
# (1000+0.002j)
