'''
Dunder = “double underscore” → methods that start and end with __

Example: __init__, __str__, __add__

They are special methods Python uses to give objects special behaviors.
'''


'''
class Person:
    def __init__(self, name):
        self.name = name  # __init__ is called automatically

p = Person("Rahul")

'''



# operator overloading using dunder method


class Addition:
    def __init__(self, a):
        self.a = a
        
    def __add__(self, b):  # overloading + operator
        return self.a + b.a

    def __len__(self):
        return self.a

obj1 = Addition(5)
obj2 = Addition(10)

result = obj1 + obj2  # Calls obj1.__add__(obj2)
print(result)  # Output: 15

print(len(obj1))  # Calls obj1.__len__()
print(len(obj2))  # Calls obj2.__len__()