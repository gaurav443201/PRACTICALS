# 8. Program to enter a number and then calculate the sum of its digits.

number = input("Enter a number : ")

sum = 0

for digit in number :

    sum += int(digit)
    continue

print("The sum of the digits of the number is : ", sum)

"""
Output:
(base) student@ioe-l1lab-14:~$ python3 U2_Practical8.py
Enter a number : 123
The sum of the digits of the number is :  6
"""
