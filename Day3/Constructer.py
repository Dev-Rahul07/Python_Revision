# constructor-> it is a special method which is used to initialize the object of the class
# it is called automatically when we create the object of the class
# it is defined by using __init__() method


class Person:
    def __init__(self, name, age, city): 
        self.Name = name
        self.Age = age
        self.City = city
        
object = Person("Rahul", 24, "Pune")
print(object.Name)