num_apples = input ("Enter the number of apples you have: ")
num_people = input ("Enter the number of people waiting: ")
def serve (num_people, num_apples):
    print(f"serve {num_people} glass of apple juice at {num_apples} per glass")
def portion (num_people, num_apples):
    return num_apples/num_people
print("The number of apples per person is: ", portion(int(num_people), int(num_apples)))