# 1.Program to access class variable using class object
class Student:
    # Class variable
    school_name = "Greenwood High"

# Create an object of the class
student1 = Student()

# Access class variable using the object
print("Accessing class variable through object:", student1.school_name)

# You can also access it using the class name
print("Accessing class variable through class:", Student.school_name)



"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U5_Practica1.py
Accessing class variable through object: Greenwood High
Accessing class variable through class: Greenwood High
"""