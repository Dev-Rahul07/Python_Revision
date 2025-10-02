class Person:   
    job = 'Nulla'  # class attribute ---> same for all object
    def __init__(self, name, age, city): 
        self.Name = name # object attribute
        self.Age = age
        self.City = city
    #  claass method
    @classmethod
    def change_job(cls, new_job):
        cls.job = new_job
        
    # instance method/object method
    def person_info(self):
        return f"Name is {self.Name}, Age is {self.Age}, City is {self.City}, Job is {self.job}"        
    
    # static method--> it is a method which is not related to class or object its act like supporting method
    @staticmethod
    def static_method_example():
        return "This is a static method."


# creating object
p1 = Person("Rahul", 24, "Pune")
p2 = Person("Sonu", 26, "Mumbai")
print(p1.person_info())
print(p2.person_info())
Person.change_job("Developer")
print(p1.person_info())

# we can call static method by using class name or object name
print(p2.static_method_example())
print(Person.static_method_example())
