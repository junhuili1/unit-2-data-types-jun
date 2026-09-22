# sentence = input("Please input a sentence")
# wordAmount = len(sentence.split())
# print(wordAmount) 

# Mad Libs Project
# person1 = input("Enter a noun(person).")
# person2 = input("Enter another noun(person).")
# place = input("Enter a place.")
# noun1 = input("Enter a noun(thing).")
# adjective1 = input("Enter an adjective.")
# noun2 = input("Enter another noun(thing).")
# adjective2 = input("Enter another adjective.")
# noun3 = input("Enter a final noun(thing).")
# adjective3 = input("Enter a final adjective.")

# print(f"{person1} and {person2} are going to make a sandwich in {place}. First, they spread on {noun1}. Then, they add some {adjective1} {noun2} and some {adjective2} {noun3}. Their sandwiches are {adjective3}!")

def is_even(number):
    return number % 2 == 0

number = int(input("Enter a number"))
print(is_even(number))