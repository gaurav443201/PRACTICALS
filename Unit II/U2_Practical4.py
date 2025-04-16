# 4. Program to find whether the given year is a leap year or not 

# Taking the year as input

year = int(input("Enter the year : "))

# Checking whether the year is a leap year or not



if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")



"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U2_Practical4.py
Enter the year : 2024
2024 is a leap year
"""