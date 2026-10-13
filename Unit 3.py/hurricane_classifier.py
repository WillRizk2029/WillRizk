print(input("What is the wind speed of the hurricane in mph? "))
mph = input("What is the wind speed of the hurricane in mph? ")
if mph == str:
    MPH = int(mph)
try:
    if int(MPH) >= 157:
        print("The hurricane is a category 5 hurricane.")
except:
    print("Invalid input. Please enter a valid number.")
try:  
    if int(MPH) < 157:
        print("The hurricane is a category 4 hurricane.")
except:
    print("Invalid input. Please enter a valid number.")
try:
    if int(MPH) < 130:
        print("The hurricane is a category 3 hurricane.")
except:
    print("Invalid input. Please enter a valid number.")
try:
    if int(MPH) < 111:
        print("The hurricane is a category 2 hurricane.")
except:
    print("Invalid input. Please enter a valid number.")
try: 
    if int(MPH) < 96:
        print("The hurricane is a category 1 hurricane.")
except:
    print("Invalid input. Please enter a valid number.")
try: 
    if int(MPH) < 74:
        print("The hurricane is a tropical storm.")
except:
    print("Invalid input. Please enter a valid number.")