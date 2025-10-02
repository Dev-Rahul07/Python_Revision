
# Example of if-else statement
# here i did type casting into integer
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Example of for loop
# this for loop -- > we do when we know how many times we want to iterate
print("For loop example:")      
for i in range(5):  # it will print 0 to 4--> in range last value is excluded
    print(i)

# while loop example --> we do when we don't know how many times we want to iterate
print("While loop example:")            
count = 0
while count < 5:
    print(count)
    count += 1  # incrementing count by 1


# break statement example
# this helps to come out of the loop
print("Break statement example:")
for i in range(10):
    if i == 5:
        break  # exit the loop when i is 5
    print(i)        
    
# continue statement example
# this helps to skip the current iteration and move to the next iteration       
for i in range(10):
    if i  == 2:
        continue
    print(i)
    
# pass statement example
#this is keyword that used to make a empty block  as valid block

def fun():
    pass  # empty function  

