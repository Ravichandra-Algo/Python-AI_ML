# Assignment:
# Write a  program that continuously asks the user for a number and prints the times table for the entered number up to 12. The program will terminate when the user enters 0.

# Example:
# Enter a number to print its times table (0 to quit): 5
# Times Table for 5:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30


# while True:
#     inp = int(input("Enter a number to print its times table (0 to quit): "))
#     if inp == 0:
#         break
#     print(f"Times Table for {5}:")
#     for num in range(1, inp + 1):
#         print(f"{inp} x {num} = {inp * num}")


# ----------------------------------------------------------------

# 1. Write a program to check whether a number is odd or even.
# Input: Enter a number: 4
# Output: 4 is Even

# while True:
#     inp = int(input("Enter a number: "))
#     if inp%2 == 0:
#         print(f"{inp} is Even")
#     else:
#         print(f"{inp} is Odd")

# 2. Write a program to find the largest of three numbers using conditionals.
# input
# Enter first number: 10
# Enter second number: 25
# Enter third number: 15
# Output: The largest number is 25

# while True:
#     inp1 = int(input("Enter first number: "))
#     inp2 = int(input("Enter second number: "))
#     inp3 = int(input("Enter third number: "))
#     if inp1 > inp2 and inp1 > inp3:
#         print(f"The largest number is {inp1}")
#     elif inp2> inp3 and inp2 > inp1:
#         print(f"The largest number is {inp2}")
#     else:
#         print(f"The largest number is {inp3}")


# 3. Write a program to print the times table of a given number up to 12.
# I/p: Enter a number: 66 x 1 = 6
# O/p:
# 6 x 2 = 12
# ...
# 6 x 12 = 72
# while True:
#     inp = int(input("Enter a number to print its times table: "))
#     for num in range(1, 13):
#         print(f"{inp} x {num} = {inp * num}")

# 4.Write a program to print all numbers between two given numbers (inclusive) using a for loop
# Enter the starting number: 3
# Enter the ending number: 7
# Output:
# 3
# 4
# 5
# 6
# 7

# while True:
#     inp1 = int(input("Enter the starting number: "))
#     inp2 = int(input("Enter the ending number: "))
#     for i in range(inp1, inp2 + 1):
#         print(i)

# 5.Write a program to check if a number is divisible by 3 and 5.
# Input: Enter a number: 15
# output: 15 is divisible by both 3 and 5
# while True:
#     inp = int(input("Enter a number: "))
#     if inp%3==0 and inp%5==0:
#         print(f"{inp} is divisible by both 3 and 5")
#     elif inp%3 ==0:
#         print(f"{inp} is divisible by 3")
#     elif inp%5 == 0:
#         print(f"{inp} is divisible by 5")
#     else:
#         print(f"{inp} is not divisible by 3 and 5")

# 6.Write a program to calculate the sum of the first N natural numbers using a while loop
#  input: Enter a number: 5
# output: The sum of first 5 natural numbers is 15
# while True:
#     inp1 = int(input("Enter the starting number: "))
#     result = 0
#     if inp1 >= 1:
#         for i in range(1, inp1 + 1):
#             result += i
#         print(f"The sum of first {inp1} natural numbers is {result}")
#     else:
#          print(f"Please enter the positive numbers")


# 7. Write a program to count the number of digits in a given number using a while loop.
# Enter a number: 12345
# output: Number of digits: 5
# while True:
#     inp = input("Enter a number: ")
#     print(f"Number of digits: {len(inp)}")

# Write a program to print numbers from 1 to n.
# Print “Fizz” if the number is divisible by 3.
# Print “Buzz” if the number is divisible by 5.
# Print “FizzBuzz” if divisible by both.
# input: Enter a number: 15
# output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# while True:
#     inp = int(input("Enter a number: "))
#     for i in range(1, inp + 1):
#         if i%3 == 0 and i%5==0:
#             print("FizzBuzz")
#         elif i%3 == 0:
#             print("Fizz")
#         elif i%5 == 0:
#              print("Buzz")
#         else:
#             print(i)


# 8. Write a program to reverse a given number using a while loop.
# Input: Enter a number: 1234
# output: Reversed number: 4321
# while True:
#     inp = input("Enter a number: ")
#     result = inp[::-1]
#     print(f"Reversed number: {result}")


# 9.Write a program to print all even numbers between 1 and a given number.
# Enter a number: 10
# 2
# 4
# 6
# 8
# 10
# while True:
#     inp = int(input("Enter a number: "))
#     for i in range(1, inp + 1):
#         if i%2 == 0:
#             print(i)


# 10.Write a program to calculate the factorial of a given number using a for loop.
# Input: Enter a number: 5
# Factorial of 5 is 120
# while True:
#     inp = int(input("Enter a number: "))
#     factorial =1
#     if(inp == 0):
#         print('factorial of 0 is not possible')
#     elif(inp == 1):
#         print(f'factorial of {inp} is {factorial}')
#     else:
#         for i in range(1, inp + 1):
#             factorial *= i
#         print(f"Factorial of {inp} is {factorial}")


# 11. Write a program to check if a given number is a palindrome
# Enter a number: 121
# 121 is a palindrome
# while True:
#     inp = input("Enter a number: ")
#     number_str = str(inp)
#     if number_str == number_str[::-1]:
#         print(f'{inp} is a palindrome')
#     else:
#         print(f'{inp} is not a palindrome')


# 12. Write a program to print all prime numbers between 1 and a given number.
# Input:Enter a number: 10
# 2
# 3
# 5
# 7
# def isPrime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True


# while True:
#     inp = int(input("Enter a number: "))
#     for i in range(1, inp+1):
#         if isPrime(i):
#             print(i)


# Write a program to calculate the sum of the digits of a given number.
# Input: Enter a number: 123
# Sum of digits: 6
# while True:
#     inp = input("Enter a number: ")
#     result =0
#     for i in inp:
#         result += int(i)
#     print(f"Sum of digits: {result}")


# Write a program to let the user guess a number between 1 and 10. The program should stop if the correct number is guessed.
# Input (Example Run):
# Guess the number (1-10): 5  
# Wrong! Try again.  
# Guess the number (1-10): 7  
# Correct! You guessed it.'
import random
while True:
    inp = int(input("Enter a number: "))
    correctNumber = random.randint(1, 10)
    if(inp > 10 or inp < 1):
        print("Please enter a number between 1 and 10")
    elif correctNumber == inp:
        print(f"Correct! You guessed it.")
        break
    else:
        print("Wrong! Try again")
