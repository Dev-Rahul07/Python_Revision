# polymorphism - poly (many) + morph (form)
# the ability to take many forms
# one task is done by different  ways or many way
# polymorphism is an important feature of oops

# polymorphism with function
def add(a, b):
    return a + b

# using the function
print(add(2, 3)) #if we passing integers
print(add("Hello ", "World")) # if we passing strings
print(add([1, 2], [3, 4])) # if we passing lists

# polymorphism with class

# methiod overriding
# same capitall, language and type method but different implementation
class India:
    def capital(self):
        return "New Delhi is the capital of India."
    
    def language(self):
        return "Hindi is the most widely spoken language of India."
    
    def type(self):
        return "India is a developing country."
class USA:
    def capital(self):
        return "Washington, D.C. is the capital of USA."
    
    def language(self):
        return "English is the primary language of USA."
    
    def type(self):
        return "USA is a developed country."
# common interface
def func(obj):
    print(obj.capital())
    print(obj.language())
    print(obj.type())   
# creating object
ind = India()
us = USA()

func(ind)
func(us)        




# mehod overloading
class Math:
    def say(self,str):
        print(str)
    def say(self, str1, str2):
        print(str1 + " " + str2)
        
m = Math()
m.say("Hello", "World")  # this will work
# m.say("Hello")  # this will give error because the latest defined method will override
    