#2. Program to access class members using class object


class Student:
    # Class variable (shared by all instances)
    school_name = "Greenwood High"

    # Constructor to initialize instance variable
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # Method (class member)
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"School: {Student.school_name}")  # Access class variable using class name

# Create an object of the class
student1 = Student("Gaurav", "10th")

# Accessing class members using object
print("Accessing class variable through object:", student1.school_name)
print("\nAccessing method through object:")
student1.display_info()

"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U5_Practical2.py
Accessing class variable through object: Greenwood High

Accessing method through object:
Name: Gaurav
Grade: 10th
School: Greenwood High
"""