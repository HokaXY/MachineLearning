#1.1
# result = 4 - 2**3 + 5*2 - 3/2
# print(result)

#1.2
# # მომხმარებლის მიერ შეყვანილი კოდი
# decimal_number = int(input("შეიყვანეთ ათობითი რიცხვი: "))

# # # გადაიყვანს ორობითში და მოაშორებს პრეფიქს '0b'
# binary_representation = bin(decimal_number)[2:]

# # დაბეჭდავს ორობით რიცხვს/შედეგი
# print(f"ორობითში გადაყვანილი რიცხვია {decimal_number} is: {binary_representation}")

#1.3
# #პირველ რიგში მომხმარებელს ვთხოვთ შეიყვანოს ჩვენთვის აუცილებელი რიცხვები
# hoursPerMonth = float(input("შეიყვანეთ ყოველთვიური მუშაობის საათების რაოდენობა"))
# hourRate = float(input("შეიყვანეთ საათობრივი სახელფასო განაკვეთი"))

# #უნდა გამოვთვალოთ თვიური ანაზღაურება
# MonthlySalary = hoursPerMonth * hourRate

# print(f"თქვენი თვიური ანაზღაურებაა: {MonthlySalary: .2f}")

#1.4
# FirstNum = float(input("შეიყვანეთ პირველი რიცხვ"))
# SecondNum = float(input("შეიყვანეთ მეორე რიცხვ"))
# ThirdNum = float(input("შეიყვანეთ მესამე რიცხვ"))

# Average= (FirstNum + SecondNum + ThirdNum) / 3

# print (f"საშუალო არითმეტიკულია {Average}")

# 1.5
# userName = (input("შეიყვანეთ სახელი"))
# userAge = int(input("შეიყვანეთ ასაკი"))
# x = 100 - userAge
# print (f"{userName} ასი წლის გახდება{x} წელში და ამჟამად არის{userAge}")

# 1.6
# x = float(input("enter number"))
# if x>0: (
#     print ("number is positive")
# )
# if x<0: (
#     print ("number is negative")
# )

# 1.7

# x = int(input("input number"))
# if x % 10 == 0:(
#     print("რიცხვი ბოლოვდება ნულით")
# )
# else:(
#     print("რიცხვი არ ბოლოვდება ნულით")
# )

# 1.8

# x = int(input("შეიყვანეთ რიცხვი"))
# y = int(input("შეიყვანეთ რიცხვი"))
# if x > 10 and y > 10 : 
#     z = (x + y) / 2
#     print(f"საშუალო არითმეტიკულია{z:.2f}")
# else:
#     Z = x * y
#     print(f"ამ რიცხვების ნამრავლია{Z:.2f}")

# 1.9
# x = int(input("შეიყვანეთ რიცხვი"))
# lastDigit = x % 10
# print(f"რიცხვის ბოლო ციფრია {lastDigit}")

# 1.10
# year = int(input("შეიყვანეთ წელი"))

# if( year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} ნაკიანი წელია")
# else:
#     print(f"{year} არ არის ნაკიანი წელი")

# 1.11
# for number in range (20, 126):
#     if number % 5 == 0 :
#         print(number)

# 1.12
# for number in range (200, 24, -1 ):
#     if number % 8 == 0:
#         print(number)

# 1.13
# x = int(input("შეიყვანეთ პირველი რიცხვი"))
# y = int(input("შეიყვანეთ მეორე რიცხვი"))

# minXY = min(x,y)
# #საერრთო გამყოფების ლისტი
# commonDiv = []

# #ვიყენებთ ლუპს რომ ვიპოვოთ საერთო გამყოფები

# for divisor in range(1, minXY +1):
#     if x % divisor == 0 and y % divisor == 0:
#         commonDiv.append(divisor)
        
# print(f"საერთო გამყოფებია {commonDiv}")

# 1.14

# total = 0

# # vikenebt loops ati ricxvis shesayvanad
# for i in range(10):
#     number = float(input(f"sheikvanet ricxvi{i+1}:"))
#     total += number
#     average = total / 10
#     print (f"sashualo aritmetikulia: {average:.2f}")

# 1.15
# evenSum = 0 
# for number in range (1, 101):
#     if number % 2 == 0:
#         evenSum += number
# print(f"1-100 mde luwi ricxvebis jamia: {evenSum}")

# 1.16
# for number in range(1500, 2101):
#     if number % 7 == 0 and number % 5 == 0 :
#         print (number)

# 1.17
# sumOM = 0
# for number in range(1500, 2101):
#     if number % 7 == 0 and number % 5 == 0 :
#         sumOM += number
# print (f"{sumOM}")

#1.18
# sumOM= 0
# number = 1500

# while sumOM <= 20000 and number <= 2100:
#     if number % 7 == 0 and number % 5 == 0:
#         sumOM += number
#     number += 1

# print(f"{sumOM}")

# 1.19- 
# countOM = 0
# for number in range(1500, 2101):
#     if number % 5 == 0:
#         countOM += 1
# print(f"{countOM}")

# 1.20
# for number in range(15, 151):
    
#     if number in (50, 75, 80):
#         continue
    
#     if number % 5 == 0:
#         print(number)

# 1.21
# x = int(input("შეიყვანეთ დადებითი რიცხვი"))
# y = int(input("შეიყვანეთ მეორე დადებითი რიცხვი"))

# import math
# gcd = math.gcd(x, y)
# print(f"{gcd}")

# 1.22
# from math import lcm
# x = int(input("შეიყვანეთ დადებითი რიცხვი"))
# y = int(input("შეიყვანეთ მეორე დადებითი რიცხვი"))

# lcmResult = lcm(x, y)
# print(f"{lcmResult}")

# 1.23
# largestOdd = None

# for i in range(1, 11):
#     number = int(input(f"sheikvanet ricxvi{i}:"))
    
#     if number % 2 != 0 and (largestOdd is None or number > largestOdd):
#         largestOdd = number
# if largestOdd is not None:
#     print(f"udidesi luwi ricxvia {largestOdd}")
# else:
#     print("luwi ricxvi ver moidzebna")

# 1.24
# number = int(input("დადებითი მთელი რიცხვი "))

# divisors = []

# for i in range(1, number + 1):
#     if number % i == 0:
#         divisors.append(i)

# print(f"The divisors of {number} are: {divisors}")

#1.25
# x = int(input("შეიყვანეთ დადებითი რიცხვი"))

# if x < 2:
#     print("რიცხვი არ არის მარტივი")
# else:
#     isPrime = True
    
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             isPrime = False
#             break
        
#     if isPrime:
#         print(f"{x} მარტივი რიცხვია")
#     else:
#         print(f"{x} არ არის მარტივი რიცხვი")

# 1.26

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# print("მარტივი რიცხვები 2 დან 1000 მდე:")
# for number in range(2, 1001):
#     if is_prime(number):
#         print(number)

# 1.27
# fibonacci1 = 1
# fibonacci2 = 1

# print(fibonacci1)
# print(fibonacci2)

# while True:
#     next_fibonacci = fibonacci1 + fibonacci2
#     if next_fibonacci <= 100:
#         print(next_fibonacci)
#         fibonacci1, fibonacci2 = fibonacci2, next_fibonacci
#     else:
#         break

# 1.28
# number = int(input("Enter a number: "))

# num_str = str(number)
# num_digits = len(num_str)

# print(f"The number of digits in {number} is: {num_digits}")

# 1.29
# number = int(input("Enter a number: "))

# digit_sum = 0

# while number > 0:
#     digit = number % 10  # Get the last digit
#     digit_sum += digit   # Add the digit to the sum
#     number //= 10        # Remove the last digit

# print(f"The sum of the digits is: {digit_sum}")

# 1.30

# # Input a number from the user
# number = int(input("Enter a number: "))

# # Initialize a variable to store the reversed number
# reversed_number = 0

# # Reverse the number
# while number > 0:
#     # Get the last digit of the number
#     digit = number % 10
    
#     # Add the digit to the reversed number (shift left and add)
#     reversed_number = reversed_number * 10 + digit
    
#     # Remove the last digit from the original number
#     number //= 10

# # Print the reversed number
# print(f"The reversed number is: {reversed_number}")

# 1.31
# # Input a number from the user
# number = int(input("Enter a number: "))

# # Convert the number to a string
# num_str = str(number)

# # Check if the string representation of the number is a palindrome
# if num_str == num_str[::-1]:
#     print(f"{number} is a palindrome.")
# else:
#     print(f"{number} is not a palindrome.")

# 1.32
# Input a number from the user
# number = int(input("Enter a non-negative integer: "))

# # Check if the input is a non-negative integer
# if number < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     # Initialize a variable to store the factorial (initially set to 1)
#     factorial = 1
    
#     # Calculate the factorial
#     for i in range(1, number + 1):
#         factorial *= i
    
#     # Print the factorial
#     print(f"The factorial of {number} is: {factorial}")

# 1.33
# Define the number of rows for the pattern
# num_rows = 4

# # Print the pattern
# for i in range(1, num_rows + 1):
#     print("* " * i)

# for i in range(num_rows - 1, 0, -1):
#     print("* " * i)
