# Description: A program that executes numbers from 1 - 100. Values that are divisible by 5 display the word "Fizz", numbers that are divisible by 8 display the word "Buzz", and numbers that are divisible by both 5 and 8 display the word "FizzBizz".
# Author: Sarah Murphy
# Date: June 16, 2024

for Number in range(1, 101):
    if Number % 5 == 0 and Number % 8 == 0:
        print("FizzBizz")
    elif Number % 5 == 0:
        print("Fizz")
    elif Number % 8 == 0:
        print("Buzz")
    else:
        print(Number)
