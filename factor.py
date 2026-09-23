number = int(input("Enter the number you want to find the factors of."))

factors = []

for i in range(1, number):
    if number % i == 0:
        factors.append(i)

for i in factors:
    print(i)