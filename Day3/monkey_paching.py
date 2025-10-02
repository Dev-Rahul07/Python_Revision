# mehod overloading
class Math:
    def say(self,str):
        print(str)
    def say(self, str1, str2):
        print(str1 + " " + str2)
        
m = Math()
m.say("Hello", "World")  # this will work
# m.say("Hello")  # this will give error because the latest defined method will override
    
    
    
# monkey patching -> dynamic modifications of a class or module at runtime
# before calling fun store somewhere  the funcrution in another variable and then call that variable as a function


class Math:
    def say(self,str):
        print(str)

    x = say
    
    def say(self, str1, str2):
        print(str1 + " " + str2)
        
m = Math()
m.say("Helloji", "World")  # this will work
m.x("Helloji")  # this will give error because the latest defined method will override
    