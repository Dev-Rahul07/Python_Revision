
# for loop has inbulid itertor


'''for val in range(10):
    print(val)'''
    
    
    
'''
we can make our iterator by iter and next keyword'''


lst = [1,2,3,4,5,6,7,8]
var = iter(lst)  # iter(lst) creates an iterator from your list.var is now an iterator object.
print(next(var))   #In Python 3, the method is __next__() or you can use the built-in function next().
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))

