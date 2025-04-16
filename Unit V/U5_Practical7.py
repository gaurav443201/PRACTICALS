'''7. The program should subtract the DOB from todays date to find out whether a person is eligible
to vote or not '''

from datetime import datetime

# Input: Date of Birth in YYYY-MM-DD format
dob_input = input("Enter your Date of Birth (YYYY-MM-DD): ")

# Convert input string to a datetime object
dob = datetime.strptime(dob_input, "%Y-%m-%d")

# Get today's date
today = datetime.today()

# Calculate age
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

# Display results
print("You are", age, "years old.")

# Check voting eligibility
if age >= 18:
    print("You are eligible to vote ")
else:
    print("You are NOT eligible to vote ")



"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U5_Practical7.py
Enter your Date of Birth (YYYY-MM-DD): 2007-04-10
You are 18 years old.
You are eligible to vote 

"""