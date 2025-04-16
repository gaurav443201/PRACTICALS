# 3. Program to illustrating the use of __int__() method


class Distance:
    def __init__(self, kilometers):
        self.kilometers = kilometers

    # Define how the object converts to an integer
    def __int__(self):
        # Convert kilometers to meters and return as integer
        return int(self.kilometers * 1000)

# Create an object of the class
d1 = Distance(5.5)  # 5.5 kilometers

# Convert object to integer
meters = int(d1)

print("Distance in meters:", meters)


"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U5_Practical3.py
Distance in meters: 5500
"""