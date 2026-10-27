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
            care = input(print("Do you let the creatures stay with you in your home, or do you release them?" ))                
            if care == "yes":
                print("The creatures seem very appreciative. You decide to go to the local sage, Cye, to find more information about the creatures.")
                research = input(print("Do you a, draw a picture of the creatures, b, write down everything you've seen of them, or c, try and remember everything yourself? "))
                if research == "A":
                    print("Cye tells you the creatures are called pyrys. They are very calm creatures usually, consume only meat, and like people! When provoked, they may grow anywhere from 7 to 26 feet taller. They're often only 10 inches tall, 20 inches long, and usually weigh 8 to 12 pounds for a healthy adult. He says it's a good thing you took care of both pyrys, because they could have taken out their anger on the village. He suggests you name the two of them. ")
                    print("You return home and decide to name both pyrys and make collars for them.")
                    name_1 = input(print("What do you name the first pyrys?"))
                    Name_2 = input(print("What do you name the second pyrys?"))
                    color_1 = input(print(f"What color collar do you make for {name_1}? "))
                    color_2 = input(print(f"What color collar do you make for {Name_2}? "))
                    print(f"When you give {name_1} their {color_1} collar and {Name_2} their {color_2} collar, they seem very greatful.")
                    print(f"{name_1} seems like they want to play. What do you give them? ")
                    play = input(print(f"After searching through your home, you find a ball of old yarn, a dice, and a feather wand. Which do you use to play with {name_1}?"))
                    if play == "old yarn":
                        print(f"{name_1} plays with the old yarn for at most 5 minutes, then the yarn ball ends up completely shredded. Now you can't crochet a blanket like you planned.")
                    if play == "a dice":
                        print(f"{name_1} bats at the dice, then ignores it.")
                    if play == "a feather wand":
                        print(f"{name_1} is very happy to play with you and the feather wand. They play with you for hours, eventually they curl up on the pillows you set out for {name_1} and {Name_2} and nap.")
                        food = input(print(f"{name_1} and {Name_2} seem very hungry. What do you feed them? Your options are some turp (a fish), some grass, or a snack you found that you don't know the age of."))
                        if food == "turp":
                            print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                        if food == "grass":
                            print("WHAT IS WRONG WITH YOU??? Cye told you that pyrys are carnivorous, eating grass will make them very sick. They reject the grass. ")
                            food_2 = input(print("What do you feed the pyrys? Turp or the old snack?"))
                            if food_2 == "turp":
                                print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                            if food_2 == "old snack":
                                sure_1 = input(print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it."))
                                if sure_1 == "yes":
                                    print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                if sure_1 == "no":
                                    print("Good choice. Feed the pyrys something else.")
                                    print("You feed the pyrys turp. They eat it all, and seem much happier with you!")
                        if food == "old snack":
                           sure = input(print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it."))
                           if sure == "yes":
                               print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                           if sure == "no":
                                print("Good choice. Feed the pyrys something else.")
                                food_3 = input(print(f"What do you feed {name_1} and {Name_2}? Turp or grass?"))
                                if food_3 == "turp":
                                    print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                if food_3 == "grass":
                                    print("Dude. You had ONE job. TRY AGAIN.")
                                    print("You FINALLY feed these poor pyrys turp. They eat all of it, and seem happier with you.")
                                    print(f"Finally, it's time for you to go to bed. {name_1} and {Name_2} curl up in bed with you, despite having the option of the pillows you set out for them.")
                                    print("Congrats! You finished this adventure.")    
    else:
        if follow == "yes":
            print("You follow the creature. You can hear it's tiny paws padding on the wet grass, the sound of the rain, and your own small footsteps. You don't notice that you have followed the creature into the Awakened Forest. Suddenly, the creature stops. You see a slightly larger creature, the same as the one you've been following. It's belly is swollen, but it otherwise looks thin and weak. ")
            print("The creature looks at you pleadingly with its many eyes, and makes a small whimpering noise. Do you help the creature, or abandon it? ")
            help = input().lower()
            if help == "help":
                print("You decide to help the creature. You take them back to your cottage.")
                care = input(print("Do you let the creatures stay with you in your home, or do you release them?" ))                
                if care == "yes":
                    print("The creatures seem very appreciative. You decide to go to the local sage, Cye, to find more information about the creatures.")
                    research = input(print("Do you a, draw a picture of the creatures, b, write down everything you've seen of them, or c, try and remember everything yourself? "))
                    if research == "A":
                        print("Cye tells you the creatures are called pyrys. They are very calm creatures usually, consume only meat, and like people! When provoked, they may grow anywhere from 7 to 26 feet taller. They're often only 10 inches tall, 20 inches long, and usually weigh 8 to 12 pounds for a healthy adult. He says it's a good thing you took care of both pyrys, because they could have taken out their anger on the village. He suggests you name the two of them. ")
                        print("You return home and decide to name both pyrys and make collars for them.")
                        name_1 = input(print("What do you name the first pyrys?"))
                        Name_2 = input(print("What do you name the second pyrys?"))
                        color_1 = input(print(f"What color collar do you make for {name_1}? "))
                        color_2 = input(print(f"What color collar do you make for {Name_2}? "))
                        print(f"When you give {name_1} their {color_1} collar and {Name_2} their {color_2} collar, they seem very greatful.")
                        print(f"{name_1} seems like they want to play. What do you give them? ")
                        play = input(print(f"After searching through your home, you find a ball of old yarn, a dice, and a feather wand. Which do you use to play with {name_1}?"))
                        if play == "old yarn":
                            print(f"{name_1} plays with the old yarn for at most 5 minutes, then the yarn ball ends up completely shredded. Now you can't crochet a blanket like you planned.")
                        if play == "a dice":
                            print(f"{name_1} bats at the dice, then ignores it.")
                        if play == "a feather wand":
                            print(f"{name_1} is very happy to play with you and the feather wand. They play with you for hours, eventually they curl up on the pillows you set out for {name_1} and {Name_2} and nap.")
                            food = input(print(f"{name_1} and {Name_2} seem very hungry. What do you feed them? Your options are some turp (a fish), some grass, or a snack you found that you don't know the age of."))
                            if food == "turp":
                                print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                            if food == "grass":
                                print("WHAT IS WRONG WITH YOU??? Cye told you that pyrys are carnivorous, eating grass will make them very sick. They reject the grass. ")
                                food_2 = input(print("What do you feed the pyrys? Turp or the old snack?"))
                                if food_2 == "turp":
                                    print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                if food_2 == "old snack":
                                    sure_1 = input(print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it."))
                                    if sure_1 == "yes":
                                        print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                    if sure_1 == "no":
                                        print("Good choice. Feed the pyrys something else.")
                                        print("You feed the pyrys turp. They eat it all, and seem much happier with you!")
                            if food == "old snack":
                               sure = input(print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it."))
                               if sure == "yes":
                                   print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                               if sure == "no":
                                    print("Good choice. Feed the pyrys something else.")
                                    food_3 = input(print(f"What do you feed {name_1} and {Name_2}? Turp or grass?"))
                                    if food_3 == "turp":
                                        print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                    if food_3 == "grass":
                                        print("Dude. You had ONE job. TRY AGAIN.")
                                        print("You FINALLY feed these poor pyrys turp. They eat all of it, and seem happier with you.")
                                        print(f"Finally, it's time for you to go to bed. {name_1} and {Name_2} curl up in bed with you, despite having the option of the pillows you set out for them.")
                                        print("Congrats! You finished this adventure.")    
            else:
                print("You decide to abandon the creature. As you walk away, you hear its whimpering fade into the distance. You suddenly feel your heart race, and the forest grows darker. You see the creature you first saw, but this time much larger, with red eyes, claws, and very sharp teeth. It seems to want revenge for not saving it's friend. ")
                sorry = input(print("Do you apologize and go help it's friend?" ))
                if sorry == "yes":
                    print("The creature calms down, and decreases in size. You pet the small creature. It's fur is very soft, like a warm blanket. You return to the other creature, feed it, and tend to it's wounds. You realize that this creature you've just helped is likely pregnant. " )
                    care = input(print("Do you let the creatures stay with you in your home, or do you release them?" ))
                    if care == "yes":
                        print("The creatures seem very appreciative. You decide to go to the local sage, Cye, to find more information about the creatures.")
                        research = input(print("Do you a, draw a picture of the creatures, b, write down everything you've seen of them, or c, try and remember everything yourself? "))
                        if research == "A":
                            print("Cye tells you the creatures are called pyrys. They are very calm creatures usually, consume only meat, and like people! When provoked, they may grow anywhere from 7 to 26 feet taller. They're often only 10 inches tall, 20 inches long, and usually weigh 8 to 12 pounds for a healthy adult. He says it's a good thing you took care of both pyrys, because they could have taken out their anger on the village. He suggests you name the two of them. ")
                            print("You return home and decide to name both pyrys and make collars for them.")
                            name_1 = input(print("What do you name the first pyrys?"))
                            Name_2 = input(print("What do you name the second pyrys?"))
                            color_1 = input(print(f"What color collar do you make for {name_1}? "))
                            color_2 = input(print(f"What color collar do you make for {Name_2}? "))
                            print(f"When you give {name_1} their {color_1} collar and {Name_2} their {color_2} collar, they seem very greatful.")
                            print(f"{name_1} seems like they want to play. What do you give them? ")
                            play = input(print(f"After searching through your home, you find a ball of old yarn, a dice, and a feather wand. Which do you use to play with {name_1}?"))
                            if play == "old yarn":
                                print(f"{name_1} plays with the old yarn for at most 5 minutes, then the yarn ball ends up completely shredded. Now you can't crochet a blanket like you planned.")
                            if play == "a dice":
                                print(f"{name_1} bats at the dice, then ignores it.")
                            if play == "a feather wand":
                                print(f"{name_1} is very happy to play with you and the feather wand. They play with you for hours, eventually they curl up on the pillows you set out for {name_1} and {Name_2} and nap.")
                                food = input(print(f"{name_1} and {Name_2} seem very hungry. What do you feed them? Your options are some turp (a fish), some grass, or a snack you found that you don't know the age of."))
                                if food == "turp":
                                    print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                if food == "grass":
                                    print("WHAT IS WRONG WITH YOU??? Cye told you that pyrys are carnivorous, eating grass will make them very sick. They reject the grass. ")
                                    food_2 = input(print("What do you feed the pyrys? Turp or the old snack?"))
                                    if food_2 == "turp":
                                        print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                    if food_2 == "old snack":
                                        sure_1 = input(print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it."))
                                        if sure_1 == "yes":
                                            print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                        if sure_1 == "no":
                                            print("Good choice. Feed the pyrys something else.")
                                            print("You feed the pyrys turp. They eat it all, and seem much happier with you!")
                                if food == "old snack":
                                    sure = input(print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it."))
                                    if sure == "yes":
                                        print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                    if sure == "no":
                                        print("Good choice. Feed the pyrys something else.")
                                        food_3 = input(print(f"What do you feed {name_1} and {Name_2}? Turp or grass?"))
                                        if food_3 == "turp":
                                            print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                        if food_3 == "grass":
                                            print("Dude. You had ONE job. TRY AGAIN.")
                                            print("You FINALLY feed these poor pyrys turp. They eat all of it, and seem happier with you.")
                                            print(f"Finally, it's time for you to go to bed. {name_1} and {Name_2} curl up in bed with you, despite having the option of the pillows you set out for them.")
                                            print("Congrats! You finished this adventure.")
                    else:
                        print("The creatures seem sad. They leave you be though.")
                        care = input(print("Do you let the creatures stay with you in your home, or do you release them?" ))
                        if care == "Yes":
                            print("The creatures seem very appreciative. You decide to go to the local sage, Cye, to find more information about the creatures.")
                            research = input(print("Do you a, draw a picture of the creatures, b, write down everything you've seen of them, or c, try and remember everything yourself? "))
                            if research == "A":
                                print("Cye tells you the creatures are called pyrys. They are very calm creatures usually, consume only meat, and like people! When provoked, they may grow anywhere from 7 to 26 feet taller. They're often only 10 inches tall, 20 inches long, and usually weigh 8 to 12 pounds for a healthy adult. He says it's a good thing you took care of both pyrys, because they could have taken out their anger on the village. He suggests you name the two of them. ")
                                print("You return home and decide to name both pyrys and make collars for them.")
                                name_1 = input(print("What do you name the first pyrys?"))
                                Name_2 = input(print("What do you name the second pyrys?"))
                                color_1 = input(print(f"What color collar do you make for {name_1}? "))
                                color_2 = input(print(f"What color collar do you make for {Name_2}? "))
                                print(f"When you give {name_1} their {color_1} collar and {Name_2} their {color_2} collar, they seem very greatful.")
                                print(f"{name_1} seems like they want to play. What do you give them? ")
                                play = input(print(f"After searching through your home, you find a ball of old yarn, a dice, and a feather wand. Which do you use to play with {name_1}?"))
                                if play == "old yarn":
                                    print(f"{name_1} plays with the old yarn for at most 5 minutes, then the yarn ball ends up completely shredded. Now you can't crochet a blanket like you planned.")
                                if play == "a dice":
                                    print(f"{name_1} bats at the dice, then ignores it.")
                                if play == "a feather wand":
                                    print(f"{name_1} is very happy to play with you and the feather wand. They play with you for hours, eventually they curl up on the pillows you set out for {name_1} and {Name_2} and nap.")
                                    food = input(print(f"{name_1} and {Name_2} seem very hungry. What do you feed them? Your options are some turp (a fish), some grass, or a snack you found that you don't know the age of."))
                                    if food == "turp":
                                        print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                    if food == "grass":
                                        print("WHAT IS WRONG WITH YOU??? Cye told you that pyrys are carnivorous, eating grass will make them very sick. They reject the grass. ")
                                        food_2 = input(print("What do you feed the pyrys? Turp or the old snack?"))
                                        if food_2 == "turp":
                                            print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                        if food_2 == "old snack":
                                            sure_1 = input(print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it."))
                                            if sure_1 == "yes":
                                                print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                            if sure_1 == "no":
                                                print("Good choice. Feed the pyrys something else.")
                                                print("You feed the pyrys turp. They eat it all, and seem much happier with you!")
                                    if food == "old snack":
                                        sure = input(print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it."))
                                        if sure == "yes":
                                            print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                            if sure == "no":
                                                print("Good choice. Feed the pyrys something else.")
                                                food_3 = input(print(f"What do you feed {name_1} and {Name_2}? Turp or grass?"))
                                                if food_3 == "turp":
                                                    print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                                if food_3 == "grass":
                                                    print("Dude. You had ONE job. TRY AGAIN.")
                                                    print("You FINALLY feed these poor pyrys turp. They eat all of it, and seem happier with you.")
                                                    print(f"Finally, it's time for you to go to bed. {name_1} and {Name_2} curl up in bed with you, despite having the option of the pillows you set out for them.")
                                                    print("Congrats! You finished this adventure.")
                            else:
                                print("Much time passes. You fail to properly care for the creatures, and they consume you to survive.")
                                research = input(print("Do you a, draw a picture of the creatures, b, write down everything you've seen of them, or c, try and remember everything yourself? "))
                                if research == "A":
                                    print("Cye tells you the creatures are called pyrys. They are very calm creatures usually, consume only meat, and like people! When provoked, they may grow anywhere from 7 to 26 feet taller. They're often only 10 inches tall, 20 inches long, and usually weigh 8 to 12 pounds for a healthy adult. He says it's a good thing you took care of both pyrys, because they could have taken out their anger on the village. He suggests you name the two of them. ")
                                    print("You return home and decide to name both pyrys and make collars for them.")
                                    name_1 = input(print("What do you name the first pyrys?"))
                                    Name_2 = input(print("What do you name the second pyrys?"))
                                    color_1 = input(print(f"What color collar do you make for {name_1}? "))
                                    color_2 = input(print(f"What color collar do you make for {Name_2}? "))
                                    print(f"When you give {name_1} their {color_1} collar and {Name_2} their {color_2} collar, they seem very greatful.")
                                    print(f"{name_1} seems like they want to play. What do you give them? ")
                                    play = input(print(f"After searching through your home, you find a ball of old yarn, a dice, and a feather wand. Which do you use to play with {name_1}?"))
                                    if play == "old yarn":
                                        print(f"{name_1} plays with the old yarn for at most 5 minutes, then the yarn ball ends up completely shredded. Now you can't crochet a blanket like you planned.")
                                    if play == "a dice":
                                        print(f"{name_1} bats at the dice, then ignores it.")
                                    if play == "a feather wand":
                                        print(f"{name_1} is very happy to play with you and the feather wand. They play with you for hours, eventually they curl up on the pillows you set out for {name_1} and {Name_2} and nap.")
                                        food = input(print(f"{name_1} and {Name_2} seem very hungry. What do you feed them? Your options are some turp (a fish), some grass, or a snack you found that you don't know the age of."))
                                        if food == "turp":
                                            print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                        if food == "grass":
                                            print("WHAT IS WRONG WITH YOU??? Cye told you that pyrys are carnivorous, eating grass will make them very sick. They reject the grass. ")
                                            food_2 = input(print("What do you feed the pyrys? Turp or the old snack?"))
                                            if food_2 == "turp":
                                                print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                            if food_2 == "old snack":
                                                sure_1 = input(print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it."))
                                                if sure_1 == "yes":
                                                    print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                                if sure_1 == "no":
                                                    print("Good choice. Feed the pyrys something else.")
                                                    print("You feed the pyrys turp. They eat it all, and seem much happier with you!")
                                        if food == "old snack":
                                            sure = input(print("Uhhhh... are you sure? This... thing looks inedible. It's discolored and has a strange stench to it."))
                                            if sure == "yes":
                                                print(f"{name_1} and {Name_2} immediately run to the opposite side of your cottage. They seem disgusted. Frankly, so are you.")
                                            if sure == "no":
                                                print("Good choice. Feed the pyrys something else.")
                                                food_3 = input(print(f"What do you feed {name_1} and {Name_2}? Turp or grass?"))
                                                if food_3 == "turp":
                                                    print("Amazing choice! The pyrys eat it all, and they seem very happy.")
                                                if food_3 == "grass":
                                                    print("Dude. You had ONE job. TRY AGAIN.")
                                                    print("You FINALLY feed these poor pyrys turp. They eat all of it, and seem happier with you.")
                                                    print(f"Finally, it's time for you to go to bed. {name_1} and {Name_2} curl up in bed with you, despite having the option of the pillows you set out for them.")
                                                    print("Congrats! You finished this adventure.")                       
start_adventure()