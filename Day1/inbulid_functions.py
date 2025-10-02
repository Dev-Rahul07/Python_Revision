l = [1,2,3]
print(l)
# append function--> it adds the element at the end of the list
l.append(4)
print(l)
# insert function--> it adds the element at the given index
# synetax--> list_name.insert(index, element)
l.insert(1,5)
print(l)
# remove function--> it removes the first occurrence of the element
l.remove(2)
print(l)
# pop function--> it removes the element at the given index and returns it
l.pop()
print(l)

print(l.pop(2))


# clear function--> it removes all the elements from the list
l.clear()
print(l)

# extend inbulid functions-->it insert a collectioon element at onece to the list
l.extend([5,6,7])
print(l)

print(l.count(10)) # it returns the count of the element in the list



# sort vs sorted

# sort function--> it sorts the list in ascending order and modifies the original list
l1 = [3,1,4,2]
l1.sort()
print(l1)



l2 = sorted(l1) # it returns a new sorted list and does not modify the original list
print(l2)   



# reverse function--> it reverses the list and modifies the original list
l2.reverse()
print(l2)






# Tuple inbulid functions
t = (1,2,3,4,5,1,2)
print(t)
print(t.count(1)) # it returns the count of the element in the tuple

print(t.index(3)) # it returns the index of the first occurrence of the element in the tuple


# dictionary inbulid functions
d = {"name": "Rahul", "age": 21, "city": "Pune"}
print(d)
print(d.get('age')) # it returns the value of the key
print(d.keys()) # it returns the keys of the dictionary
print(d.values()) # it returns the values of the dictionary
print(d.pop('city')) # it removes the key-value pair and returns the value of the key
print(d.popitem()) # it removes the last key-value pair and returns it as a tuple
print(d.copy()) # it returns a shallow copy of the dictionary
print(d.clear()) # it removes all the key-value pairs from the dictionary



# set
s = {1,2,3,4,5}
print(s)

s.add(6) # it adds the element to the set
print(s)    
s.remove(3) # it removes the element from the set
print(s)        

s.pop() # it removes and returns an arbitrary element from the set
print(s)    
s.clear() # it removes all the elements from the set
print(s)

# we can do set operations like union, intersection, difference 
s1 = {1,2,3}
s2 = {3,4,5}        
print(s1-s2) # it returns the difference of two sets



# string
str1 = "hello"
print(str1)
print(str1.upper()) # it converts the string to uppercase
print(str1.lower()) # it converts the string to lowercase   
print(str1.title()) # it converts the first character of each word to uppercase
print(str1.capitalize()) # it converts the first character of the string to uppercase

print(str1.find('e')) # it returns the index of the first occurrence of the substring
print(str1.replace('l', 'p')) # it replaces the substring with another substring
print(str1.split()) # it splits the string into a list of substrings based on the delimiter by default space
print('-'.join(['h','e','l','l','o'])) # it joins the list of strings into a single string with the delimiter   


s = "   hello   "
print(s.strip()) # it removes the leading and trailing whitespace
