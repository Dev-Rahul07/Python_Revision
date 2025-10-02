'''
What is JSON?

JSON = JavaScript Object Notation

Basically a way to store data as text

Looks like Python dictionaries or lists:

{
  "name": "Mini",
  "age": 22,
  "skills": ["Python", "HTML", "CSS"]
}



'''


# in python there is one module is json --> dump and load and dumps and loads

import json

data = {
    'name' :'rahul',
    'age' : 21,
    'degree' :'BCA'
    }
print(type(data))

# dump--> convert the data into json object
json_data = json.dumps(data)
print(type(json_data))

# loads
x = json.loads(json_data)
print(type(x))


# dump
with open('data.json','w') as f:
    json.dump(data,f)
    
# load
with open ('data.json','r') as f:
   y = json.load(f)
   
print(y)