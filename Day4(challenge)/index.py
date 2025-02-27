#Day 4 Challenge:
# Write a Python program that converts numbers into words! 

from num2words import num2words
user_any_number = int(input("Enter any Number: "))
converted_words = num2words(user_any_number)
print("converted Into words:", converted_words.capitalize())  
