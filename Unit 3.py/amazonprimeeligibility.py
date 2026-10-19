age = int(input("What is your age? "))
money = int(input("How much money do you have in your bank account? "))
purchase = input("Do you want to purchase Amazon Prime? ")
if age < 18:
    consent = input("Do you have parental consent? ")
if (age >= 18 and money >= 139 and purchase == "yes") or (consent == "yes" and money >= 139 and purchase == "yes"):
        print("Thank you for purchasing Amazon Prime!")
else:
    print("You are not eligible to purchase Amazon Prime.")