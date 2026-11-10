import random
correct = False
number = random.randint(1, 100)
num_guesses = 0
guess = input("Guess a number between 1 and 100: ")
while not correct:
    if int(guess) > number:
        print("Too high! Try again.")
        guess = input("Guess a number between 1 and 100: ")
        num_guesses += 1
    elif int(guess) < number:
        print("Too low! Try again.")
        guess = input("Guess a number between 1 and 100: ")
        num_guesses += 1
    else:
        print("You guessed it!")
        correct = True
        print(f"It took you {num_guesses} guesses.")
        if num_guesses == 1:
           print("You are unreal tier!")
        elif num_guesses >= 2:
            print("You are champon tier!")
        elif num_guesses >= 3:
            print("You are elite tier!" )
        elif num_guesses >= 5:
            print("You are diamond tier!")
        elif num_guesses >= 7:
            print("You are platinum tier!")
        elif num_guesses >= 9:
            print("You are gold tier!")
        elif num_guesses >= 11:
            print("You are silver tier!")
        elif num_guesses >= 13:
            print("You are bronze tier!")
        else:
            print("You are wood tier!")
