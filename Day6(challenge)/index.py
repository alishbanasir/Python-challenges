# Task 6 Challenge: 
# Aisa Python program likhna hai jo user se ek integer number lega aur uska binary (0s aur 1s) me conversion karega, phir check karega ke ye palindrome hai ya nahi! 

user_input = int(input("Enter any Number: "))
binary_num = bin(user_input)[2:]
print(f"User Number: {user_input}")
print(f"Binary Number: {binary_num}")

if binary_num == binary_num[::-1]:
    print("It's a Palindrome")
else:
    print("It's not a Palindrome")
 