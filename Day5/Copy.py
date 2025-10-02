'''
in python  copy the content from one varible to other variable is called Copy opertion

there  is 3 copy -> genrel copy 
                -> shellow copy
                -> deep copy
                
                
'''
# Genrale copy  --> Here both varible is pointing to same memmory loacations
print('in case of general copy')
a = [1,2,3]
b = a

print(a)
print(b)
print(id(a))
print(id(b))


# shellow copy -> copy the content from one varible to other but in differnt memmory location location
print('in case of shellow copy')
import copy
x = [10,20,30,[1,2]]
y = copy.copy(x)
print(id(x))
print(id(y))
print(x is y )
print(x[3] is y[3])  #in case of nested collcetion it not work so we go with deep copy



#deep copy
print('in case of deep copy ..')
import copy 

z = copy.deepcopy(x)
print(z is x)
print(z[3] is x[3])

