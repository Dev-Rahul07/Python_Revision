import sqlite3 #here importing the sqlite database


con = sqlite3.connect('my_db.db')   # for making conncetion

var = con.cursor()  # for pointing the  db


var.execute('''CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT
);'''
) #here we can write the sql code for excution
var.execute('''INSERT INTO students (name, course) VALUES  ("Rahul", "BCA"),('Mohit','Btech')''')
var.execute('''INSERT INTO students (name, course) VALUES  ("Mini", "BCA")''')
x = var.execute('''select * from students ''')

con.commit() # save the changes


for val in x:
    print(val)
    
    
    
var.close()    # close the db