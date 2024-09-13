# -*- coding: utf-8 -*-
"""Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

# Program to check if a character is a vowel or consonant

# Take input from the user
char = input("Enter a single character: ").lower()

# Check if the input is a letter
if char.isalpha() and len(char) == 1:
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input! Please enter a single alphabetic character.")