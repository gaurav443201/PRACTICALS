# 3. Program to display power of a number without using formatting characters.
# 4. Program to display power of a number using formatting characters. 
# Since both are similar, I have combined them into one program.


num = int(input("Enter the number: "))
power = int(input("Enter the power: "))

result = num ** power

print("Result without using formatting characters: ", result)

print("Result using formatting characters: %d" % result)

print("Read the code to understand the difference between the two.")

"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U3_Practical3and4.py
Enter the number: 2
Enter the power: 3
Result without using formatting characters:  8
Result using formatting characters: 8
Read the code to understand the difference between the two.
"""
