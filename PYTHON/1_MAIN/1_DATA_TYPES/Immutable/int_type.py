print(int(' -3 ', base=10))
# -3

print(int(' +5 '))
# 5
print(int(' -15_125'))
# -15125

print(int(3.23))
# 3
print(int(1.))
# 1
print(int(3.14e-10))
# 0

print(int(0o177))
# 127
print(int('  0o177 ', base=8))
# 127

print(int(0x9ff))
# 2559
print(int(' 0x9ff  ', base=16))
# 2559

print(int(0b101010))
# 42
print(int('0b101010', base=2))
# 42
