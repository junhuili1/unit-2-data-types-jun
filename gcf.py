import math 

print("Welcome to the gcf calculator. Input your two numbers when asked.")
number1 = int(input("Enter the first number."))
number2 = int(input("Enter the second number."))

gcf = math.gcd(number1, number2)
print(f"The gcf of {number1} and {number2} is {gcf}.")