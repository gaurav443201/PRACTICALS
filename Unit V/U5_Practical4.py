#4. Program to differentiate between class and object variable

class Car:
    # Class variable (shared across all instances)
    wheels = 4

    def __init__(self, brand, color):
        # Object (instance) variables (unique to each object)
        self.brand = brand
        self.color = color

# Create two car objects
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# Modify object variable
car1.color = "Black"

# Modify class variable using class name
Car.wheels = 6

# Display information
print("Car 1 - Brand:", car1.brand, "| Color:", car1.color, "| Wheels:", car1.wheels)
print("Car 2 - Brand:", car2.brand, "| Color:", car2.color, "| Wheels:", car2.wheels)


"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U5_Practical4.py
Car 1 - Brand: Toyota | Color: Black | Wheels: 6
Car 2 - Brand: Honda | Color: Blue | Wheels: 6
"""