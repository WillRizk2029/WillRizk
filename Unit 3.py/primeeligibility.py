age = int(input("What is your age? "))
if age >= 18:
    money = int(input("How much money do you have in your bank account? "))
    if money >= 139:
        purchase = input("Do you want to purchase Amazon Prime? ")
        if purchase == "yes":
            print("Thank you for purchasing Amazon Prime!")
    else:
        print("You do not have enough money to purchase Amazon Prime.")
else:
    consent = input("Do you have parental consent? ")
    if consent == "yes":
        money = int(input("How much money do you have in your bank account? "))
        if money >= 139:
            purchase = input("Do you want to purchase Amazon Prime? ")
            if purchase == "yes":
                print("Thank you for purchasing Amazon Prime!")
            else:
                print("Purchase cancelled.")
        else:
            print("You do not have enough money to purchase Amazon Prime.")
    else:
        print("You are not eligible to purchase Amazon Prime.")