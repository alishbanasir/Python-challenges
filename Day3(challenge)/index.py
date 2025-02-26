#Day 3 Challenge: Aisa Python program likho jo user se ek number le aur check kare ke wo prime number hai ya nahi!

user_number = int(input("Enter any number: "))
if user_number > 1:
    for i in range(2, user_number):  
        if user_number % i == 0:
            print("No, it's not a prime number!")
            break
    else:
        print("Yes, it's a prime number!")  
else:
    print("No, it's not a prime number!")  
