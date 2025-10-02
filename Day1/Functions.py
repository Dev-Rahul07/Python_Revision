# here c is default parameter -- 
def add_numbers(a, b,c = 20):
    return a + b + c    
def multiply_numbers(a, b,c = 20):
    return a * b * c
def subtract_numbers(a, b,c = 20):
    return a - b - c

def calc(a,b,c):
    print(add_numbers(a,b,c))
    print(multiply_numbers(a,b,c))
    print(subtract_numbers(a,b,c))




calc(10,5,0)