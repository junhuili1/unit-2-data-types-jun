number = int(input("Enter the number you want to find the factors of."))

factors = []

for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)

print(f"The factors of {number} are: {factors}")