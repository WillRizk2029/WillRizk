print(input("What is the wind speed of the hurricane in mph? "))
mph = input("What is the wind speed of the hurricane in mph? ")
if mph == str:
    MPH = int(mph)
if int(MPH) >= 157:
    print("The hurricane is a category 5 hurricane.")
if int(MPH) < 157:
    print("The hurricane is a category 4 hurricane.")
if int(MPH) < 130:
    print("The hurricane is a category 3 hurricane.")
if int(MPH) < 111:
    print("The hurricane is a category 2 hurricane.")
if int(MPH) < 96:
    print("The hurricane is a category 1 hurricane.")
if int(MPH) < 74:
    print("The hurricane is a tropical storm.")