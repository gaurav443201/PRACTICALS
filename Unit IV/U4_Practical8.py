# 8. Program that reads data from a file and calculates the percentage of vowels and consonants in the file.

# Function to check vowels
def is_vowel(char):
    return char.lower() in 'aeiou'

# Open and read the file
with open('practical8.txt', 'r') as file:
    text = file.read()

# Initialize counters
vowels = 0
consonants = 0

# Loop through each character
for char in text:
    if char.isalpha():  # Only consider letters
        if is_vowel(char):
            vowels += 1
        else:
            consonants += 1

# Calculate total letters
total_letters = vowels + consonants

# Avoid division by zero
if total_letters > 0:
    vowel_percentage = (vowels / total_letters) * 100
    consonant_percentage = (consonants / total_letters) * 100
else:
    vowel_percentage = consonant_percentage = 0

# Print the results
print("Total letters:", total_letters)
print("Vowels:", vowels, f"({vowel_percentage:.2f}%)")
print("Consonants:", consonants, f"({consonant_percentage:.2f}%)")


""" 
Output :
(base) student@ioe-l1lab-14:~$ python3 U4_Practical8.py
Total letters: 49
Vowels: 18 (36.73%)
Consonants: 31 (63.27%)
"""