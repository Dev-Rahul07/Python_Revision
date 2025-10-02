# we have some operators in python like arithmetic operators, comparison operators, logical operators, bitwise operators, assignment operators, identity operators, membership operators
# arithmetic operators
a = 10
b = 3
print(a + b) # 13
print(a - b) # 7    
print(a * b) # 30
# in division we have two types of division
print(a / b) # 3.3333333333333335 #True division
print(a // b) # 3   #Floor division
# modulus operator
print(a % b) # 1
# exponent operator
print(a ** b) # 1000            
# comparison operators  
print(a == b) # False
print(a != b) # True    
print(a > b)  # True
print(a < b)  # False
print(a >= b) # True
print(a <= b) # False   
# logical operators
x = True
y = False
print(x and y) # False
print(x or y)  # True
print(not x)   # False  

# bitwise operators
p = 5  # 0101 in binary
q = 3  # 0011 in binary
print(p & q) # 1  (AND)
print(p | q) # 7  (OR)
print(p ^ q) # 6  (XOR)
print(~p)    # -6 (NOT)
print(p << 1) # 10 (LEFT SHIFT)
print(p >> 1) # 2  (RIGHT SHIFT)    
# assignment operators
c = 10
c += 5  # c = c + 5
print(c) # 15               

# identity operators --> is and is not --> they compare the memory locations of two objects
m = [1, 2, 3]               
n = m
print(m is n)      # True
print(m is not n)  # False

# membership operators --> in and not in --> they check if a value is present in a sequence (like list, tuple, string)
lst = [1, 2, 3, 4, 5]
print(3 in lst)      # True
print(6 not in lst)  # True


