# fibomachecci series

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
'''def fib(n):
    a ,b = 0,1
    for i in range(n):
        print(a)
        a,b = b,a+b
        
fib(10) 
'''

"""# Prime number
def is_prime(num):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    return is_prime

print(is_prime(29))
print(is_prime(15))"""


'''# revserse a  String

def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

print(reverse_string("Hello"))'''
'''
# factorial of a number
def fact(n):
    fact = 1
    for i in range(n,0,-1):
        fact *= i
    return fact

print(fact(5))'''