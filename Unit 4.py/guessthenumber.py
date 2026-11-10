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
        if num_guesses > 1 and num_guesses < 4:
            print("You are champon tier!")
        if num_guesses > 3 and num_guesses < 6:
            print("You are elite tier!" )
        if num_guesses > 5 and num_guesses < 8:
            print("You are diamond tier!")
        if num_guesses > 9 and num_guesses < 10:
            print("You are platinum tier!")
        if num_guesses > 9 and num_guesses < 12:
            print("You are gold tier!")
        if num_guesses > 11 and num_guesses < 14:
            print("You are silver tier!")
        if num_guesses > 13 and num_guesses < 16:
            print("You are bronze tier!")
        if num_guesses > 15:
            print("You are wood tier!")
