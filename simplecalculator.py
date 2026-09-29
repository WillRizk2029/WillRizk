def add(x, y):
   print (x + y)
   return x + y
def subtract(x, y):
    print (x - y)
    return x - y
def multiply(x, y):
    print (x * y)
    return x * y
def divide(x, y):
    print (x / y)
    return x / y
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
x2 = float(input("Enter third number: "))
y2 = float(input("Enter fourth number: "))
x3 = float(input("Enter fifth number: "))
y3 = float(input("Enter sixth number: "))
x4 = float(input("Enter seventh number: "))
y4 = float(input("Enter eighth number: "))
sum_1 = add(x, y)
sum_2 = subtract(x2, y2)
sum_3 = divide(x3, y3)
sum_4 = multiply(x4, y4)

print (sum_1)
print (sum_2)
print (sum_3)
print (sum_4)