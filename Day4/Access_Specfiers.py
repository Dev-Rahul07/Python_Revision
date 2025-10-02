# like other programming language here also 3 Access Specfiers
# public,protecd,private
# this private varible is also know s name mangling



# name magaling basically means--->is way to make a  class atribute a private ....

class my_class:
    x = 10 #public
    _y = 20  #protacted ---> this is act like  public
    __z = 100 # private
    
    def getter(self):
        return self.__z
    
    
    
obj = my_class()
print(obj.x)
print(obj._y)
# print(obj.__z)

# for accessing private we can use obj._classname__privatevarible name or getter setter method


print(obj._my_class__z)
print(obj.getter())