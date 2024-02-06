b = bytes([46, 46, 46])
print(b)
# b'...'

list(b)
# [46, 46, 46]

b = bytes(range(40, 60, 2))
print(b)
# b'(*,.02468:'

print(list(b))
# [40, 42, 44, 46, 48, 50, 52, 54, 56, 58]
