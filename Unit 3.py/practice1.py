def multiply ():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    try: print(float(num1) * float(num2))
    except:
        print ("Invalid Input. Try again.")
        multiply()
multiply()