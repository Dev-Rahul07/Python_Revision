# Dictionary comprehension
values = [1, 2, 3, 4, 5]
dict1 = {v: v**2 for v in values}
dict2 = {v: v**2 for v in values if v % 2 == 0}
dict3 = {v: v**2 if v % 2 == 0 else v**3 for v in values}
print(dict1)
print(dict2)
print(dict3)

# Tuple comprehension
t = tuple(v for v in range(1, 6))
print(t)

# Set comprehension
s = {v for v in range(1, 6)}
print(s)
