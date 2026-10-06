adjective = input("enter an adjective:")
noun = input("enter a noun:")
verb = input("enter a verb:")
noun2 = input("enter second noun:")
noun3 = input("enter a third noun:")
print("Once upon a time, in a " + adjective + " " + noun + ", there lived a " + noun2 + " and a " + noun3 + " that was " + verb + ".")

def add_three (x, y, z):
    x = int(input("what is x?"))
    y = int(input("what is y?"))
    z = int(input("what is z?"))
    return x + y + z
print(add_three(1, 2, 3))

def data_three ():
    word = input("enter a word:")
    integer = int(input("enter an integer:"))
    fl = float(input("enter a float:"))
    print ("your word is " + word + ", your integer is " + str(integer) + ", and your float is " + str(fl) + ".")
print(data_three())