'''
1️⃣ What is a decorator?

A decorator is basically a function that takes another function and extends its behavior without changing the original function code.

Think of it as adding toppings to a pizza 🍕.

''''''


# simple eg
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, Mini!")

say_hello()


# passing task
def my_decorator(func):
    def wrapper(*args ,**kwargs):
        print("Before the function")
        result  = func(*args,**kwargs)
        return  result
        print("After the function")
    return wrapper

@my_decorator
def say_hello(a,b):
    print("Hello, Mini!")
    return a+b

print(say_hello(10,30))


'''
# login

def Dec(fun):
    def wrapper(*args, **kwargs):
        print('login..')
        fun(*args,**kwargs)
        print('logout')
    return wrapper

@Dec
def fun(str):
    print(str)

fun('stalkin')
fun('job search')
fun('date')



