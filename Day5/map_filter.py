# map is function that accept one lambda function 

# map() is used to apply a function to every item in a list (or any iterable) and return a new list (or iterable) with the results.


# syntex 

'''
fun = map(lamdba,list/itterrable)


'''


lst = [1,2,3,4,5]
fun = lambda val:val**2
x = map(fun,lst)

print(list(x))


# filter
'''
ilter() is used to filter elements from a list based on some condition.
'''

lst = [1,2,3,4,5]
fun = lambda val:val%2==0
x = filter(fun,lst)
print(list(x))

