#5. Program to illustrating the use of __del__() method.


class Person:
    def __init__(self, name):
        self.name = name
        print(f"Hello, my name is {self.name}.")

    def __del__(self):
        print(f"Goodbye from {self.name}. Object is being deleted.")

# Creating an object
p1 = Person("Alice")

# Deleting the object manually
del p1

# Adding a delay to show that __del__() was called
print("Program ended.")

"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U5_Practical5.py
Hello, my name is Alice.
Goodbye from Alice. Object is being deleted.
Program ended.
"""