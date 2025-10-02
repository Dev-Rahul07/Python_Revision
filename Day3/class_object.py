# oops -> it stans for object oriented programming system
# it is methodlogy or way of programming
# to implement real senario in programming we use oops


# class -> it is a blue print or template or design to create object
# object -> it is instance of class

class Person:
    # class attribute
    Name = "Rahul"
    Age = 24
    City = "Pune"
    
    # object attribute
    def __init__(self): 
        self.Name = "Sonu"
        self.Age = 26
        self.City = "Mumbai"
    
    
# creatinng object
p1 = Person()
p2 = Person()
print(p1.Name)
print(p2.Age)  
print(Person.Name)