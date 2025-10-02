

from Student import Student
class Teacher(Student):  # Single inheritance (Teacher inherits Student)
    def __init__(self, name, marks, subject):
        super().__init__(name, marks)  # Call Student constructor
        self.subject = subject

    def show_subject(self):
        print(f"{self.name} teaches {self.subject}")

# Test
t1 = Teacher("Anil", 90, "Math")
t1.display()       # From Student
t1.show_subject()  # Teacher method



class Sports:
    def __init__(self, sport):
        self.sport = sport

    def show_sport(self):
        print(f"Plays: {self.sport}")

# Teacher inherits both Student & Sports
class TeacherMulti(Student, Sports):
    def __init__(self, name, marks, subject, sport):
        Student.__init__(self, name, marks)
        Sports.__init__(self, sport)
        self.subject = subject

    def show_subject(self):
        print(f"{self.name} teaches {self.subject}")

# Test
t2 = TeacherMulti("Anil", 95, "Physics", "Cricket")
t2.display()       # From Student
t2.show_subject()  # Teacher method
t2.show_sport()    # From Sports
