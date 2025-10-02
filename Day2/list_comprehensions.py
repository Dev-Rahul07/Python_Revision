# List Comprehension
nums = [1, 2, 3, 4, 5]
squared = [x**2 for x in nums]
even = [x for x in nums if x % 2 == 0]
print(squared)
print(even)
# Output: [1, 4, 9, 16, 25]
# Output: [2, 4]


# coonditional list comprehension
nums = [1, 2, 3, 4, 5]
result = [x**2 if x % 2 == 0 else x**3 for x in nums]
print(result)
# Output: [1, 4, 27, 16, 125]

# else part is optional in list comprehension       