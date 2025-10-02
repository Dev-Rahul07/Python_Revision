# inheritance-> when a class derives from another class
# it is proceess of inheriting properties and methods from another class
# prent class->child class



class Animal:  # parent class
    def speak(self):
        print("Animal speaks")  
        
class Dog(Animal):  # child class
    def bark(self):
        print("Dog barks")  

class Cat(Animal):  # child class
    def meow(self):
        print("Cat meows")  
        
dog = Dog()
dog.speak()  # inherited method from parent class   
dog.bark()   # method of child class
cat = Cat()
cat.speak()  # inherited method from parent class
cat.meow()   # method of child class


#  we have single inheritance, multiple inheritance, multilevel inheritance, hierarchical inheritance, hybrid inheritance
#  we can use super() method to access parent class methods and attributes
class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def display(self):
        print("Child class method")
        super().show()  # calling parent class method

c = Child()
c.display()


# single inheritance - when a class inherits from a single parent class
# multiple inheritance - when a class inherits from multiple parent classes
class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Painting")

class Child(Father, Mother):
    def show_skills(self):
        print("Child skills:")
        Father.skills(self)
        Mother.skills(self)

c = Child()
c.show_skills()
# multilevel inheritance - when a class inherits from a child class
class GrandParent:
    def legacy(self):
        print("GrandParent legacy")

class Parent(GrandParent):
    def inheritance(self):
        print("Parent inheritance")

class Child(Parent):
    def family(self):
        print("Child family")

c = Child()
c.legacy()
c.inheritance()
c.family()  

# hierarchical inheritance - when multiple classes inherit from a single parent class
class Parent:
    def family_name(self):
        print("Family name is Smith")   

class Child(Parent):
    def child_name(self):
        print("Child name is John")

c = Child()
c.family_name()
c.child_name()  

#  hybrid inheritance is a combination of two or more types of inheritance