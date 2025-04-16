# 6. Program to illustrating the difference between public and private variable.

class Employee:
    def __init__(self, name, salary):
        self.name = name            # Public variable
        self.__salary = salary      # Private variable (with double underscore)

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.__salary)  # Accessing private variable within the class

# Create object
emp = Employee("John", 50000)

# Access public variable
print("Accessing public variable:", emp.name)

# Try to access private variable directly (will cause error)
try:
    print("Accessing private variable directly:", emp.__salary)
except AttributeError as e:
    print("Error:", e)

# Correct way to access private variable (via method or name mangling)
emp.display()
print("Accessing private variable using name mangling:", emp._Employee__salary)



"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U5_Practical6.py
Accessing public variable: John
Error: 'Employee' object has no attribute '__salary'
Name: John
Salary: 50000
Accessing private variable using name mangling: 50000
"""