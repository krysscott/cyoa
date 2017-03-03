
print "You have just been shipwrecked! You wake up washed up on the beach of a deserted island alone. You look around at the lush island in aw. It is beautiful, but what dangers are there?? Survive and get off the Island!!"
shelter = raw_input("First you need to build shelter. It is about noon judging by your shadow and compass. You need to consider your shelter options. Which do you choose? 'treehouse' (in the jungle) or 'tent' (on the beach)?   ")
if shelter == "treehouse":
    sleep_or_food = raw_input("You walk into the jungle and start working on your shelter. You work all day, finding wood, collecting palm fronds, and creating rope out of discarded coconut husks. Your shelter is still not finished after you've expended all your energy. It is getting too dark and you still need to find food. You are hungry, but the dangers of the jungle are unknown...sleep or food?   ")
    if sleep_or_food == "sleep":
        print "You go to sleep in your unfinished shelter. You just managed to sleep after killing several mosquitos when suddenly, in the middle of the night, a cougar finds its way into your shelter.. By the time your eyes open, the cougar is starting to devour you alive!"
        survive = raw_input("You can still live if you make very very specific moves!! Quickly make a choice: Do you act dead or fight?  ")
        if survive == "act" or survive == "ACT" or survive == "Act" or survive == "act dead" or survive == "Act dead":
            print "Bad choice! The cougar is already starting to eat you! Does it matter is you're dead or not to the cougar?? You die a slow death while the cougar tears at your skin"
        elif survive == "fight" or survive == "FIGHT" or survive == "Fight":
            method = raw_input("You have to think carefully on this one. This might be crazy, but you might have a knife in your pocket from earlier, but you are not sure. Do you risk it and try to grab the knife that is maybe not there, or do you start punching the cougar in the nose? print 'grab' or 'punch'   ")
            if method == "grab" or method == "Grab":
                print "good job, trust your intincts."
                print "Ruh Ro, your knife is not there :) I guess the cougar will just eat you. Say your last words!!"
            elif method == "punch" or method == "Punch":
                print "Cougars are not like sharks! They do not get disoriented if you punch them there!! The cougar gets angrier and devours you faster. Toodles Sailor! :))"
            else:
                print "Based on your indecisiveness, I sense your will to live is not strong. A massive tropical storm sweeps you away into Davvy Jones' Locker!!"

if sleep_or_food == "food" or sleep_or_food == "Food" or sleep_or_food == "FOOD":
    number = raw_input("You go out to find food and come across some nice bananas hanging low. Lucky you! You prepare to make off with them but a monkey crosses your path! This monkey is particularly smart and persistent.. Be careful! Choose a number between (1-5) to make away with your food  ")
        num = "3"
        while number != num:
            if number == "5":
                print "The Monkey takes your food and you die of starvation"
                break
            else:
                print "Wrong, guess again!"
                number = raw_input("What's your next guess? ")

    if number == num:
        water = raw_input("Good job, you evaded the monkey and get to eat your bananas. Now you have to get water. Do you get it from the pond or the stream?  ")
            if water == "pond" or water == "the pond" or water == "Pond" or water == "POND" or water == "The pond":
                print "You contract a digusting bacterial disease... You die the next day."
        if water == "stream" or water == "Stream" or water == "the stream" or water == "The stream" or water == "STREAM":
            print "Congratulations, you are well hydrated and take supply for the next coming days."
                materials = raw_input("You survived until the next morning. Time to build your raft to get out of here... Do you build out of tree bark and palms or bamboo and palms? Type 'bark' or 'bamboo':  ")
                if materials == "bark" or materials == "Bark" or materials == "BARK":
                    print "You go out onto the water after tirelessly working on your raft and start to drift away... You realize that the tree bark was rotten on the inside and you drown in the middle of the ocean!!"
            if materials == "bamboo" or materials == "Bamboo" or materials == "BAMBOO":
                print "CONGRATULATIONS!! You have survived the island and have successfully gotten off of it. A rescue boat finds you floating dreamily, eating bananas and coconuts in the crystal blue waters the next day."




import random

matches = {
    ('heads', 'tails'): False,
        ('Heads', 'Tails'): False,
            ('Tails', 'Heads'): False,
            ('tails', 'heads'): False,
            ('heads', 'heads'): True,
            ('tails', 'tails'): True,
            ('Heads', 'Heads'): True,
            ('Tails', 'Tails'): True,
            ('tails', 'Heads'): False,
            ('Heads', 'tails'): False,
            ('Tails', 'heads'): False,
            ('heads', 'Tails'): False,
            ('heads', 'Heads'): True,
            ('Heads', 'heads'): True,
            ('Tails', 'tails'): True,
            ('tails', 'Tails'): True
}
def get_results(play1, play2):
    """
        Return True if play1 beats play2, or False if not. Returns None if the
        plays tie.
        """
    
    if play1 == play2:
        return None
    
    return matches[(play1, play2)]

def get_randomdice():
    """
        Flip a coin to pick a random play.
        """
    return random.choice(['heads', 'tails', 'Heads', 'Tails'])


matchups = {
    ('rock', 'paper'): False,
    ('paper', 'rock'): True,
    ('rock', 'scissors'): True,
    ('scissors', 'rock'): False,
    ('paper', 'scissors'): False,
    ('scissors', 'paper'): True,
}

def get_result(play1, play2):
    """
        Return True if play1 beats play2, or False if not. Returns None if the
        plays tie.
        """
    
    if play1 == play2:
        return None
    
    return matchups[(play1, play2)]

def get_random():
    """
        Rolls a 3-way dice to pick a random play.
        """
    return random.choice(['rock', 'paper', 'scissors'])

if shelter == "tent" or shelter == "Tent":
    print "Good choice! You have enough daylight to find food and water- which do you find first?"
    choice = raw_input("Food or Water?")
    if choice == "food" or choice == "Food":
        print "Uh oh! You've stumbled upon a gorilla nest without knowing, but you're able to find a lot of food!"
        second_choice = raw_input("You begin to run, but which way do you turn first? Left or Right?")
        if second_choice == "left" or second_choice == "Left":
            print "You run into a gorilla and it kills you for taking its food."
        elif second_choice == "right" or second_choice == "Right":
            print "You're running and find an animal den- do you crawl inside?"
            #This is for the coin flip chance game!
            #picking from a couple options
            #kinda like the rock paper scissors
            #Mr. Smedberg's code was used and edited!
            print "Let's flip a coin!"
            
            user_play = raw_input("Type heads/tails or Heads/Tails: ")
            computer_play = get_randomdice()
            
            print "I chose %s!" % (computer_play,)
            
            result = get_results(user_play, computer_play)
            while result == None:
                print "It's a tie, play again!"
                user_play = raw_input("Type heads/tails or Heads/Tails: ")
                computer_play = get_randomdice()
                result = get_results(user_play, computer_play)
                print "I chose %s!" % (computer_play,)
            
            if result:
                print "You've won! You avoid the animal den and survive until the next morning, managing to also find water on your way back to your tent!"
                print "Morning arrives, and it's time to start building your raft!"
                raft = raw_input("What do you build it out of? (choose 'a, b, or c') \n a: Coconuts and Jungle Leaves \n b: Tree Bark and Flowers \n c: Bamboo and Banana Peels")
                if raft == 'a':
                    print "CONGRATULATIONS!! You've successfully made it off of the island and you are found by a rescue boat after sailing out in the sea for a day or two!"
                elif raft == 'b':
                    print "The tree bark was rotten and did not last long out in the water. You have a slow death by being eaten by a family of piranahs."
                elif raft == 'c':
                    print "Not the best choice, your raft lasts for a little bit but eventually starts sinking in the middle of the sea; you've drowned."
            else:
                print "You've lost and you've been eaten by a family of foxes, sorry."
    elif choice == "water" or choice == "Water":
        lala = raw_input("Do you choose to a: desalinate ocean water or b: find a stream?")
        if lala == "a" or lala == "desalinate" or lala == "desalinate ocean water" or lala == "A" or lala == "Desalinate" or lala == "Desalinate ocean water" or lala == "Desalinate Ocean Water" or lala == "desalinate water" or lala == "Desalinate Water" or lala == "Desalinate water":
            print "You now have enough time to find food, how are you going to get it?"
            print "Let's play rock-paper-scissors!"
            
            user_play = raw_input("Type rock/paper/scissors: ")
            computer_play = get_random()
            
            print "I chose %s!" % (computer_play,)
            result = get_result(user_play, computer_play)
            while result == None:
                print "It's a tie, play again!"
                user_play = raw_input("Type rock/paper/scissors: ")
                computer_play = get_random()
                result = get_result(user_play, computer_play)
                print "I chose %s!" % (computer_play,)
            if result == False:
                print "I win. You lose!! You die of starvation.. Mwahahahahah"
            if result == True:
                print "You win, and you've caught a nice fish to eat for dinner! You survive till the next day, and now it's time to build a raft!"
                raft = raw_input("What do you build it out of? (choose 'a, b, or c') \n a: Coconuts and Jungle Leaves \n b: Tree Bark and Flowers \n c: Bamboo and Banana Peels")
                if raft == 'a':
                    print "CONGRATULATIONS!! You've successfully made it off of the island and you are found by a rescue boat after sailing out in the sea for a day or two!"
                elif raft == 'b':
                    print "The tree bark was rotten and did not last long out in the water. You have a slow death by being eaten by a family of piranahs."
                elif raft == 'c':
                    print "Not the best choice, your raft lasts for a little bit but eventually starts sinking in the middle of the sea; you've drowned."
            else:
                print "You were going to pick some berries off of a bush, but decided to climb the trees to get some bananas, but a branch broke underneath you and you fell to your death."
        if lala == "b" or lala == "stream" or lala == "Stream" or lala == "B" or lala == "find a stream" or lala == "Find A Stream" or lala == "Find a Stream" or lala == "Find a stream" or lala == "a stream":
            print "Finding the stream takes you all day and you don't have time to get back to your tent or find food. What happens next?"
                bloop = raw_input("Pick a number between 1-5 to find out: ")
                if bloop == "1" or bloop == "one" or bloop == "One":
                    print "You manage to sleep where you are unharmed and survive till the next day, but you stop to grab some berries, only to die since you didn't realize they were Belladonnas."
            elif bloop == "2" or bloop == "two" or bloop == "Two":
                print "You find Belladonna berries and die from the poison."
                elif bloop == "3" or bloop == "three" or bloop == "Three":
                    print "You've stayed in one place for too long and get eaten by a random jaguar."
elif bloop == "4" or bloop == "Four" or bloop == "four":
    print "You're able to find food and return the tent safely! You've survived till the next morning, time to build your raft, what do you build it out of?"
        raft = raw_input("What do you build it out of? (choose 'a, b, or c') \n a: Coconuts and Jungle Leaves \n b: Tree Bark and Flowers \n c: Bamboo and Banana Peels")
            elif bloop == "5" or bloop == "Five" or bloop == "five":
                print "You run home safely! (But you get trampled by an elephant and die.)"
                else:
                    print "You've died from a jungle virus for not picking a number between 1-5!"
                    if raft == 'a':
                        print "CONGRATULATIONS!! You've successfully made it off of the island and you are found by a rescue boat after sailing out in the sea for a day or two!"
                elif raft == 'b':
                    print "The tree bark was rotten and did not last long out in the water. You have a slow death by being eaten by a family of piranahs."
                    elif raft == 'c':
                        print "Not the best choice, your raft lasts for a little bit but eventually starts sinking in the middle of the sea; you've drowned."
