rate = 0.06875
item = float(input("Enter the price of the item: "))
price = item
def calculate_tax():
    tax = price * rate
    print(f"{item} costs ${price} dollars before tax and ${price + tax} after tax")
calculate_tax()