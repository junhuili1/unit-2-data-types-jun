print("Welcome to the gcf calculator. Input your two numbers when asked.")
number1 = int(input("Enter the first number."))
number2 = int(input("Enter the second number."))

factors1 = []
factors2 = []

for i in range(1, number1 + 1):
    if number1 % i == 0:
        factors1.append(i)

for i in range(1, number2 + 1):
    if number2 % i == 0:
        factors2.append(i)

