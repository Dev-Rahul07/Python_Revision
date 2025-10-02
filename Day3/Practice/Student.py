
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student: {self.name}, Marks: {self.marks}")

# Test
s1 = Student("Rahul", 85)
s1.display()  # Student: Rahul, Marks: 85
