class A:
    def __init__(self,name):
        print("A's constructor called")
        self.name = name
        
        
class B(A):
    def __init__(self, name, age):
        print("B's constructor called")
        self.age = age
        super().__init__(name)  # calling parent class constructor
        
b= B("Rahul", 24)
print(b.name)
print(b.age)