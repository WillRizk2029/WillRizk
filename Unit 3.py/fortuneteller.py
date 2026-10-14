import random

print("I am the fortune teller. Give me a number, any number, and I will tell your future.")
fortune = random.randint(1, 100)
lucky_number = int(input("What is your lucky number?"))
if lucky_number == fortune:
    print("You are very lucky!")
else:
    print("Better luck next time.")
print(f"Your lucky number is {lucky_number}, and your fortune is: {fortune}")
years_into_future = int(input("How many years into the future would you like to see your fortune?"))
if years_into_future == fortune:
    print("You will go on great adventures!")
else:
    print("You will face challenges, but overcome them.")
spells = int(input("How many spells do you have?"))
print(f"In {years_into_future} years, you will have {spells * years_into_future} spells.")

