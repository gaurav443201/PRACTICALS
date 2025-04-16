# 2. Program to determine whether a person is eligible to vote or not 


# Taking the age of the person as input

age = int(input("Enter the age of the person : "))

# Checking whether the person is eligible to vote or not

if age>=18:
    print("The person is eligible to vote")
else:
    print("The person is not eligible to vote")


"""
Output:
(base) student@ioe-l1lab-14:~$ python3 U2_Practical2.py
Enter the age of the person : 21
The person is eligible to vote
"""