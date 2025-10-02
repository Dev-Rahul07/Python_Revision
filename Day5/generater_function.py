'''GeneratorFun --> any functionn that have yield keybord that  consider as genrater function and yeild keyword pouse the excution and store in some other place and after excution it return the vaule in one short and we need to type cast that '''

def fun(lst):
    for val in lst:
        yield val
        
        
print(list(fun([1,2,3,4,5])))



# Fibonacci using  generator function
def fibo():
    a,b = 0,1
    for i in range(1,10):
        yield a
        a,b = a+b,a
        
        
        
print(tuple(fibo()))
        
    