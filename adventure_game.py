import random

def intro():
    print("Welcome to the Jungle Adventure!")
    print("You find yourself in a dense forest with two distinct paths.")
    print("The left path leads to a river, while the right path takes you to the mountains.")

def river_path():
    print("You have chosen the path towards the river.")
    print("You reach the riverbank. The water looks inviting and calm.")
    print("Do you want to 'swim' across the river or 'explore' the riverbank?")

def mountain_path():
    print("You have chosen the path towards the mountains.")
    print("The trail is rocky and steep. You feel a sense of adventure.")
    print("Do you want to 'climb' higher up the mountain or 'rest' at a nearby campsite?")

def swim_decision():
    if random.choice([True, False]):
        print("You swim across the river and discover a hidden cave filled with treasure!")
    else:
        print("The current is stronger than expected. You struggle but manage to reach the shore safely.")

def explore_decision():
    if random.choice([True, False]):
        print("While exploring the riverbank, you find a beautiful waterfall and a peaceful place to relax.")
    else:
        print("You wander for hours but find nothing interesting. You start to feel exhausted and decide to head back.")

def climb_decision():
    if random.choice([True, False]):
        print("You climb further and reach the summit, enjoying a breathtaking view of the valley below.")
    else:
        print("The path becomes treacherous. You slip but manage to find a secure ledge to catch your breath.")

def rest_decision():
    if random.choice([True, False]):
        print("You rest at the campsite and enjoy a warm meal. A friendly hiker shares fascinating stories with you.")
    else:
        print("While resting, you hear unsettling noises from the woods. You decide to pack up and move on.")

def adventure_game():
    intro()
    
    choice1 = input("Do you choose the 'left' path or the 'right' path? ").lower()
    
    if choice1 == "left":
        river_path()
        choice2 = input("Do you want to 'swim' across the river or 'explore' the riverbank? ").lower()
        if choice2 == "swim":
            swim_decision()
        elif choice2 == "explore":
            explore_decision()
        else:
            print("That's not a valid option. The adventure ends here.")
    
    elif choice1 == "right":
        mountain_path()
        choice2 = input("Do you want to 'climb' higher up the mountain or 'rest' at a nearby campsite? ").lower()
        if choice2 == "climb":
            climb_decision()
        elif choice2 == "rest":
            rest_decision()
        else:
            print("That's not a valid option. The adventure ends here.")
    
    else:
        print("That's not a valid option. The adventure ends here.")

    print("Thank you for playing the Adventure Game!")

adventure_game()
