def start_adventure():
    print("Welcome to PASTELSPACE!")
    player_name = input("What's your name? ")
    print(f"Hello, {player_name}! Your adventure begins now.")
    print("You are standing outside a small cottage, in your town. It is raining. You see a small creature, with many eyes, four legs, a small nose, and a tail. It comes up to you and makes a noise similar to the sound of a motor. It rubs against you, then runs off ahead of you. ")
    print("Do you follow the creature? (yes/no)")
    follow = input().lower()
    if follow == "yes":
        print("You follow the creature. You can hear it's tiny paws padding on the wet grass, the sound of the rain, and your own small footsteps. You don't notice that you have followed the creature into the Awakened Forest. Suddenly, the creature stops. You see a slightly larger creature, the same as the one you've been following. It's belly is swollen, but it otherwise looks thin and weak. ")
        print("The creature looks at you pleadingly with its many eyes, and makes a small whimpering noise. Do you help the creature, or abandon it? ")
        help = input().lower()
        if help == "help":
            print("You decide to help the creature. You take them back to your cottage.")
            print("Do you let the creatures stay with you in your home, or do you release them?")
            care = input(). lower()    
            if care == "yes":
                print("The creatures seem very appreciative. You decide to go to the local sage, Cye, to find more information about the creatures.")
                print("Cye tells you the creatures are called pyrys. They are very calm creatures usually, consume only meat, and like people! When provoked, they may grow anywhere from 7 to 26 feet taller. They're often only 10 inches tall, 20 inches long, and usually weigh 8 to 12 pounds for a healthy adult. He says it's a good thing you took care of both pyrys, because they could have taken out their anger on the village. He suggests you name the two of them. ")
                print("You return home and decide to name both pyrys and make collars for them.")
                print("What do you name the first pyrys?")
                name_1 = input(). lower()
                print("What do you name the second pyrys?")
                Name_2 = input(). lower()
                print(f"What color collar do you make for {name_1}? ")
                color_1 = input(). lower()
                print(f"What color collar do you make for {Name_2}? ")
                color_2 = input(). lower()
                print(f"When you give {name_1} their {color_1} collar and {Name_2} their {color_2} collar, they seem very greatful.")
                print(f"{name_1} seems like they want to play. What do you give them? ")
                print(f"After searching through your home, you find a ball of old yarn, a dice, and a feather wand. Which do you use to play with {name_1}?")
                play = input(). lower()
                if play == "old yarn":
                    print(f"{name_1} plays with the old yarn for at most 5 minutes, then the yarn ball ends up completely shredded. Now you can't crochet a blanket like you planned.")
                if play == "a dice":
                    print(f"{name_1} bats at the dice, then ignores it.")
                if play == "a feather wand":
                    print(f"{name_1} is very happy to play with you and the feather wand. They play with you for hours, eventually they curl up on the pillows you set out for {name_1} and {Name_2} and nap.")
                    print(f"{name_1} and {Name_2} seem very hungry. What do you feed them? Your options are some turp (a fish), some grass, or a snack you found that you don't know the age of.")
                    food = input(). lower()
                    if food == "turp":
                        print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                    if food == "grass":
                        print("WHAT IS WRONG WITH YOU??? Cye told you that pyrys are carnivorous, eating grass will make them very sick. They reject the grass. ")
                        print("What do you feed the pyrys? Turp or the old snack?")
                        food_2 = input(). lower()
                        if food_2 == "turp":
                            print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                        if food_2 == "old snack":
                            print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it.")
                            sure_1 = input(). lower()
                            if sure_1 == "yes":
                                print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                            if sure_1 == "no":
                                print("Good choice. Feed the pyrys something else.")
                                print("You feed the pyrys turp. They eat it all, and seem much happier with you!")
                    if food == "old snack":
                       print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it.")
                       sure = input(). lower()
                       if sure == "yes":
                        print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                        if sure == "no":
                            print("Good choice. Feed the pyrys something else.")
                            print(f"What do you feed {name_1} and {Name_2}? Turp or grass?")
                            food_3 = input(). lower()
                            if food_3 == "turp":
                                print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                            if food_3 == "grass":
                                print("Dude. You had ONE job. TRY AGAIN.")
                                print("You FINALLY feed these poor pyrys turp. They eat all of it, and seem happier with you.")
                                print(f"Finally, it's time for you to go to bed. {name_1} and {Name_2} curl up in bed with you, despite having the option of the pillows you set out for them.")
                                print("Congrats! You finished this adventure.") 
    else:
        print("You go back to bed. you don't wake up.")
        start_adventure
        if follow == "yes":
            print("You follow the creature. You can hear it's tiny paws padding on the wet grass, the sound of the rain, and your own small footsteps. You don't notice that you have followed the creature into the Awakened Forest. Suddenly, the creature stops. You see a slightly larger creature, the same as the one you've been following. It's belly is swollen, but it otherwise looks thin and weak. ")
            print("The creature looks at you pleadingly with its many eyes, and makes a small whimpering noise. Do you help the creature, or abandon it? ")
            help = input().lower()
            if help == "help":
                print("You decide to help the creature. You take them back to your cottage.")
                print("Do you let the creatures stay with you in your home, or do you release them?")
                care = input(). lower()    
                if care == "yes":
                    print("The creatures seem very appreciative. You decide to go to the local sage, Cye, to find more information about the creatures.")
                    print("Cye tells you the creatures are called pyrys. They are very calm creatures usually, consume only meat, and like people! When provoked, they may grow anywhere from 7 to 26 feet taller. They're often only 10 inches tall, 20 inches long, and usually weigh 8 to 12 pounds for a healthy adult. He says it's a good thing you took care of both pyrys, because they could have taken out their anger on the village. He suggests you name the two of them. ")
                    print("You return home and decide to name both pyrys and make collars for them.")
                    print("What do you name the first pyrys?")
                    name_1 = input(). lower()
                    print("What do you name the second pyrys?")
                    Name_2 = input(). lower()
                    print(f"What color collar do you make for {name_1}? ")
                    color_1 = input(). lower()
                    print(f"What color collar do you make for {Name_2}? ")
                    color_2 = input(). lower()
                    print(f"When you give {name_1} their {color_1} collar and {Name_2} their {color_2} collar, they seem very greatful.")
                    print(f"{name_1} seems like they want to play. What do you give them? ")
                    print(f"After searching through your home, you find a ball of old yarn, a dice, and a feather wand. Which do you use to play with {name_1}?")
                    play = input(). lower()
                    if play == "old yarn":
                        print(f"{name_1} plays with the old yarn for at most 5 minutes, then the yarn ball ends up completely shredded. Now you can't crochet a blanket like you planned.")
                    if play == "a dice":
                        print(f"{name_1} bats at the dice, then ignores it.")
                    if play == "a feather wand":
                        print(f"{name_1} is very happy to play with you and the feather wand. They play with you for hours, eventually they curl up on the pillows you set out for {name_1} and {Name_2} and nap.")
                        print(f"{name_1} and {Name_2} seem very hungry. What do you feed them? Your options are some turp (a fish), some grass, or a snack you found that you don't know the age of.")
                        food = input(). lower()
                        if food == "turp":
                            print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                        if food == "grass":
                            print("WHAT IS WRONG WITH YOU??? Cye told you that pyrys are carnivorous, eating grass will make them very sick. They reject the grass. ")
                            print("What do you feed the pyrys? Turp or the old snack?")
                            food_2 = input(). lower()
                            if food_2 == "turp":
                                print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                            if food_2 == "old snack":
                                print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it.")
                                sure_1 = input(). lower()
                                if sure_1 == "yes":
                                    print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                if sure_1 == "no":
                                    print("Good choice. Feed the pyrys something else.")
                                    print("You feed the pyrys turp. They eat it all, and seem much happier with you!")
                        if food == "old snack":
                            print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it.")
                            sure = input(). lower()
                            if sure == "yes":
                                print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                            if sure == "no":
                                print("Good choice. Feed the pyrys something else.")
                                print(f"What do you feed {name_1} and {Name_2}? Turp or grass?")
                                food_3 = input(). lower()
                                if food_3 == "turp":
                                    print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                if food_3 == "grass":
                                    print("Dude. You had ONE job. TRY AGAIN.")
                                    print("You FINALLY feed these poor pyrys turp. They eat all of it, and seem happier with you.")
                                    print(f"Finally, it's time for you to go to bed. {name_1} and {Name_2} curl up in bed with you, despite having the option of the pillows you set out for them.")
                                    print("Congrats! You finished this adventure.")  
            else:
                print("You decide to abandon the creature. As you walk away, you hear its whimpering fade into the distance. You suddenly feel your heart race, and the forest grows darker. You see the creature you first saw, but this time much larger, with red eyes, claws, and very sharp teeth. It seems to want revenge for not saving it's friend. ")
                print("Do you apologize to the creature and go back to help it's friend?")
                sorry = input(). lower()
                if sorry == "yes":
                    print("The creature calms down, and decreases in size. You pet the small creature. It's fur is very soft, like a warm blanket. You return to the other creature, feed it, and tend to it's wounds. You realize that this creature you've just helped is likely pregnant. " )
                    print("Do you let the creatures stay with you in your home, or do you release them?")
                    care = input(). lower()    
                    if care == "yes":
                        print("The creatures seem very appreciative. You decide to go to the local sage, Cye, to find more information about the creatures.")
                        print("Cye tells you the creatures are called pyrys. They are very calm creatures usually, consume only meat, and like people! When provoked, they may grow anywhere from 7 to 26 feet taller. They're often only 10 inches tall, 20 inches long, and usually weigh 8 to 12 pounds for a healthy adult. He says it's a good thing you took care of both pyrys, because they could have taken out their anger on the village. He suggests you name the two of them. ")
                        print("You return home and decide to name both pyrys and make collars for them.")
                        print("What do you name the first pyrys?")
                        name_1 = input(). lower()
                        print("What do you name the second pyrys?")
                        Name_2 = input(). lower()
                        print(f"What color collar do you make for {name_1}? ")
                        color_1 = input(). lower()
                        print(f"What color collar do you make for {Name_2}? ")
                        color_2 = input(). lower()
                        print(f"When you give {name_1} their {color_1} collar and {Name_2} their {color_2} collar, they seem very greatful.")
                        print(f"{name_1} seems like they want to play. What do you give them? ")
                        print(f"After searching through your home, you find a ball of old yarn, a dice, and a feather wand. Which do you use to play with {name_1}?")
                        play = input(). lower()
                        if play == "old yarn":
                            print(f"{name_1} plays with the old yarn for at most 5 minutes, then the yarn ball ends up completely shredded. Now you can't crochet a blanket like you planned.")
                        if play == "a dice":
                            print(f"{name_1} bats at the dice, then ignores it.")
                        if play == "a feather wand":
                            print(f"{name_1} is very happy to play with you and the feather wand. They play with you for hours, eventually they curl up on the pillows you set out for {name_1} and {Name_2} and nap.")
                            print(f"{name_1} and {Name_2} seem very hungry. What do you feed them? Your options are some turp (a fish), some grass, or a snack you found that you don't know the age of.")
                            food = input(). lower()
                            if food == "turp":
                                print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                            if food == "grass":
                                print("WHAT IS WRONG WITH YOU??? Cye told you that pyrys are carnivorous, eating grass will make them very sick. They reject the grass. ")
                                print("What do you feed the pyrys? Turp or the old snack?")
                                food_2 = input(). lower()
                                if food_2 == "turp":
                                    print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                if food_2 == "old snack":
                                    print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it.")
                                    sure_1 = input(). lower()
                                    if sure_1 == "yes":
                                        print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                    if sure_1 == "no":
                                        print("Good choice. Feed the pyrys something else.")
                                        print("You feed the pyrys turp. They eat it all, and seem much happier with you!")
                            if food == "old snack":
                                print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it.")
                                sure = input(). lower()
                                if sure == "yes":
                                    print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                if sure == "no":
                                    print("Good choice. Feed the pyrys something else.")
                                    print(f"What do you feed {name_1} and {Name_2}? Turp or grass?")
                                    food_3 = input(). lower()
                                    if food_3 == "turp":
                                        print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                    if food_3 == "grass":
                                        print("Dude. You had ONE job. TRY AGAIN.")
                                        print("You FINALLY feed these poor pyrys turp. They eat all of it, and seem happier with you.")
                                        print(f"Finally, it's time for you to go to bed. {name_1} and {Name_2} curl up in bed with you, despite having the option of the pillows you set out for them.")
                                        print(f"Congrats! You finished this adventure, {player_name}!")
                else:
                    print("You get eaten. Try again.")
                    print("Do you apologize to the creature and go back to help it's friend?")
                    sorry = input(). lower()
                    if sorry == "yes":
                        print("The creature calms down, and decreases in size. You pet the small creature. It's fur is very soft, like a warm blanket. You return to the other creature, feed it, and tend to it's wounds. You realize that this creature you've just helped is likely pregnant. " )
                        print("Do you let the creatures stay with you in your home, or do you release them?")
                        care = input(). lower()    
                        if care == "yes":
                            print("The creatures seem very appreciative. You decide to go to the local sage, Cye, to find more information about the creatures.")
                            print("Cye tells you the creatures are called pyrys. They are very calm creatures usually, consume only meat, and like people! When provoked, they may grow anywhere from 7 to 26 feet taller. They're often only 10 inches tall, 20 inches long, and usually weigh 8 to 12 pounds for a healthy adult. He says it's a good thing you took care of both pyrys, because they could have taken out their anger on the village. He suggests you name the two of them. ")
                            print("You return home and decide to name both pyrys and make collars for them.")
                            print("What do you name the first pyrys?")
                            name_1 = input(). lower()
                            print("What do you name the second pyrys?")
                            Name_2 = input(). lower()
                            print(f"What color collar do you make for {name_1}? ")
                            color_1 = input(). lower()
                            print(f"What color collar do you make for {Name_2}? ")
                            color_2 = input(). lower()
                            print(f"When you give {name_1} their {color_1} collar and {Name_2} their {color_2} collar, they seem very greatful.")
                            print(f"{name_1} seems like they want to play. What do you give them? ")
                            print(f"After searching through your home, you find a ball of old yarn, a dice, and a feather wand. Which do you use to play with {name_1}?")
                            play = input(). lower()
                            if play == "old yarn":
                                print(f"{name_1} plays with the old yarn for at most 5 minutes, then the yarn ball ends up completely shredded. Now you can't crochet a blanket like you planned.")
                            if play == "a dice":
                                print(f"{name_1} bats at the dice, then ignores it.")
                            if play == "a feather wand":
                                print(f"{name_1} is very happy to play with you and the feather wand. They play with you for hours, eventually they curl up on the pillows you set out for {name_1} and {Name_2} and nap.")
                                print(f"{name_1} and {Name_2} seem very hungry. What do you feed them? Your options are some turp (a fish), some grass, or a snack you found that you don't know the age of.")
                                food = input(). lower()
                                if food == "turp":
                                    print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                if food == "grass":
                                    print("WHAT IS WRONG WITH YOU??? Cye told you that pyrys are carnivorous, eating grass will make them very sick. They reject the grass. ")
                                    print("What do you feed the pyrys? Turp or the old snack?")
                                    food_2 = input(). lower()
                                    if food_2 == "turp":
                                        print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                    if food_2 == "old snack":
                                        print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it.")
                                        sure_1 = input(). lower()
                                        if sure_1 == "yes":
                                            print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                        if sure_1 == "no":
                                            print("Good choice. Feed the pyrys something else.")
                                            print("You feed the pyrys turp. They eat it all, and seem much happier with you!")
                                if food == "old snack":
                                    print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it.")
                                    sure = input(). lower()
                                    if sure == "yes":
                                        print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                    if sure == "no":
                                        print("Good choice. Feed the pyrys something else.")
                                        print(f"What do you feed {name_1} and {Name_2}? Turp or grass?")
                                        food_3 = input(). lower()
                                        if food_3 == "turp":
                                            print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                        if food_3 == "grass":
                                            print("Dude. You had ONE job. TRY AGAIN.")
                                            print("You FINALLY feed these poor pyrys turp. They eat all of it, and seem happier with you.")
                                            print(f"Finally, it's time for you to go to bed. {name_1} and {Name_2} curl up in bed with you, despite having the option of the pillows you set out for them.")
                                            print(f"Congrats! You finished this adventure, {player_name}!")
                    else:
                        print("The creatures seem sad. They leave you be though.")
                        print("Do you let the creatures stay with you in your home, or do you release them?")
                        care = input(). lower()    
                        if care == "yes":
                            print("The creatures seem very appreciative. You decide to go to the local sage, Cye, to find more information about the creatures.")
                            print("Cye tells you the creatures are called pyrys. They are very calm creatures usually, consume only meat, and like people! When provoked, they may grow anywhere from 7 to 26 feet taller. They're often only 10 inches tall, 20 inches long, and usually weigh 8 to 12 pounds for a healthy adult. He says it's a good thing you took care of both pyrys, because they could have taken out their anger on the village. He suggests you name the two of them. ")
                            print("You return home and decide to name both pyrys and make collars for them.")
                            print("What do you name the first pyrys?")
                            name_1 = input(). lower()
                            print("What do you name the second pyrys?")
                            Name_2 = input(). lower()
                            print(f"What color collar do you make for {name_1}? ")
                            color_1 = input(). lower()
                            print(f"What color collar do you make for {Name_2}? ")
                            color_2 = input(). lower()
                            print(f"When you give {name_1} their {color_1} collar and {Name_2} their {color_2} collar, they seem very greatful.")
                            print(f"{name_1} seems like they want to play. What do you give them? ")
                            print(f"After searching through your home, you find a ball of old yarn, a dice, and a feather wand. Which do you use to play with {name_1}?")
                            play = input(). lower()
                            if play == "old yarn":
                                print(f"{name_1} plays with the old yarn for at most 5 minutes, then the yarn ball ends up completely shredded. Now you can't crochet a blanket like you planned.")
                                if play == "a dice":
                                    print(f"{name_1} bats at the dice, then ignores it.")
                                    if play == "a feather wand":
                                        print(f"{name_1} is very happy to play with you and the feather wand. They play with you for hours, eventually they curl up on the pillows you set out for {name_1} and {Name_2} and nap.")
                                        print(f"{name_1} and {Name_2} seem very hungry. What do you feed them? Your options are some turp (a fish), some grass, or a snack you found that you don't know the age of.")
                                        food = input(). lower()
                                        if food == "turp":
                                            print("Amazing choice! the pyrys eat it all, and they seem very happy.")
                                        if food == "grass":
                                            print("WHAT IS WRONG WITH YOU??? Cye told you that pyrys are carnivorous, eating grass will make them very sick. They reject the grass. ")
                                            print("What do you feed the pyrys? Turp or the old snack?")
                                            food_2 = input(). lower()
                                            if food_2 == "turp":
                                                print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                            if food_2 == "old snack":
                                                print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it.")
                                                sure_1 = input(). lower()
                                                if sure_1 == "yes":
                                                    print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                                    if sure_1 == "no":
                                                        print("Good choice. Feed the pyrys something else.")
                                                        print("You feed the pyrys turp. They eat it all, and seem much happier with you!")
                                        if food == "old snack":
                                            print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it.")
                                            sure = input(). lower()
                                            if sure == "yes":
                                                print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                            if sure == "no":
                                                print("Good choice. Feed the pyrys something else.")
                                                print(f"What do you feed {name_1} and {Name_2}? Turp or grass?")
                                                food_3 = input(). lower()
                                                if food_3 == "turp":
                                                    print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                                if food_3 == "grass":
                                                    print("Dude. You had ONE job. TRY AGAIN.")
                                                    print("You FINALLY feed these poor pyrys turp. They eat all of it, and seem happier with you.")
                                                    print(f"Finally, it's time for you to go to bed. {name_1} and {Name_2} curl up in bed with you, despite having the option of the pillows you set out for them.")
                                                    print("Congrats! You finished this adventure.")    
start_adventure()
def end_credits():
    print("Here are the credits!")
    print("Code Creator: Will Rizk")
    print("Director: Will Rizk")
    print("Whimsy Director: Will Rizk")
    print("Creative Assistant: Will Rizk")
    print("Only Writer: Will Rizk")
    print("Executive Producer: Will Rizk")
    print("Game Testers: Will Rizk and Christian T")
def fun_fact():
    print("Would you like to hear some fun facts about the world, characters, and creation of the universe?")
    first = input(). lower()
    if first == "yes":
        print("The first fun fact is that Will created the world of PASTELSPACE 3 years ago, back in 2023 because he was bored.")
        print("Would you like to hear another fun fact?")
        second = input(). lower()
        if second == "yes":
            print("The character Cye is going to be in another of Will's games! Will plans to make another game (as well as a book) inside this universe. Cye is a sage and scientist in the universe of PASTELSPACE, and they will be one of the main characters for the book and game!")
            print("Would you like to hear a third and final fun fact?")
            third = input(). lower()
            if third == "yes":
                print("In the universe of PASTELSPACE, there is a children's poem throughout the series that most citizens know. It goes: One for sorrow, two for mirth, three for a wedding, and four for a birth. five for silver, six for gold, and seven for a secret never to be told. It is very important to the story! It isn't featured here because that's a lot of extra work, but it will be used in the other parts of the universe!")
end_credits()
fun_fact()