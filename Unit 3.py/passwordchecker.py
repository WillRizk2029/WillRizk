def check_password():
    password = input("Enter your password: ")
    if password == "WR2010777":
        print("Access granted.")
    else:
        print("Access denied. Try again.")
    check_password()
check_password()