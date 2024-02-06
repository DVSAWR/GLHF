print(float(10))
# 10.0

print(float(' -15  '))
# -15.0
print(float(' -15_125'))
# -15125.0
print(float('  -3.500 '))
# -3.5
print(float('.500  '))
# 0.5
print(float(' -1e-1'))
# -0.1
print(float('  1.e-5 '))
# 1e-05
print(float('  1.5e7 '))
# 15000000.0
print(float('  3.5657e+3 '))
# 3565.7
print(float('nan'))
# nan
print(float('-inf'))
# -inf
