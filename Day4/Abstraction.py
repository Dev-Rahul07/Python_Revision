from abc import ABC,abstractmethod
class Hello(ABC):
    pass
    
    @abstractmethod
    def sound(self):
        pass
    
class dog(Hello):
    def sound(self):
        return "bark"
        
class cat(Hello):
    def sound(self):
        return "mehow"
obj = dog()
obj1 = cat()
print(obj.sound())
print(obj1.sound())