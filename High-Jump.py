import random # To use the "random.randint" function to make to code choose random number for dice roll. 
attempts = 0 # To count how many attempts the user is using. 
a_height = 0 # Maximum height achieved. 
L = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30] # List of heights available. 
print("The following heights are available to choose from.")
print(L)
height = int(input("Your selected height: "))
while height not in L: # If the number is not in the list, it prints out "invalid number". 
    print("This is an invalid number, please choose another.")
    height = int(input("Your VALID selected height: "))
while height in L and attempts < 3: # This loop only runs when the attempts are under 3 and entered number is in the list.
    roll = input("Enter \"y\" to roll the dice: ")
    if roll == "y":
        d1 = random.randint(1,6) # Chooses random number from 1-6 for the dice roll. 
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        d4 = random.randint(1,6)
        d5 = random.randint(1,6)
        if d1 == 1:
            print(u"\u2680") # This prints a dice related to the number the computer chose for die 1. 
        elif d1 == 2:
            print(u"\u2681")
        elif d1 == 3:
            print(u"\u2682")
        elif d1 == 4:
            print(u"\u2683")
        elif d1 == 5:
            print(u"\u2684")
        elif d1 == 6:
            print(u"\u2685")
        if d2 == 1:
            print(u"\u2680") # This prints a dice related to the number the computer chose for die 2.
        elif d2 == 2:
            print(u"\u2681")
        elif d2 == 3:
            print(u"\u2682")
        elif d2 == 4:
            print(u"\u2683")
        elif d2 == 5:
            print(u"\u2684")
        elif d2 == 6:
            print(u"\u2685")
        if d3 == 1:
            print(u"\u2680") # This prints a dice related to the number the computer chose for die 3.
        elif d3 == 2:
            print(u"\u2681")
        elif d3 == 3:
            print(u"\u2682")
        elif d3 == 4:
            print(u"\u2683")
        elif d3 == 5:
            print(u"\u2684")
        elif d3 == 6:
            print(u"\u2685")
        if d4 == 1:
            print(u"\u2680") # This prints a dice related to the number the computer chose for die 4.
        elif d4 == 2:
            print(u"\u2681")
        elif d4 == 3:
            print(u"\u2682")
        elif d4 == 4:
            print(u"\u2683")
        elif d4 == 5:
            print(u"\u2684")
        elif d4 == 6:
            print(u"\u2685")
        if d5 == 1:
            print(u"\u2680") # This prints a dice related to the number the computer chose for die 5.
        elif d5 == 2:
            print(u"\u2681")
        elif d5 == 3:
            print(u"\u2682")
        elif d5 == 4:
            print(u"\u2683")
        elif d5 == 5:
            print(u"\u2684")
        elif d5 == 6:
            print(u"\u2685")
        sum = d1 + d2 + d3 + d4 + d5 # Sums up all the die. 
        if sum >= height:
            a_height = height # If the sum is higher or equal to the choosen height, your choosen height becomes your "Highest height achieved."
            print("You managed to score heigher than your selected height.")
            print("Your current highest scored height is",a_height,)
            attempts = 0
            height = int(input("Your next selected height: "))
        elif sum < height: # If the sum is not equal or higher than the choosen height. It prints that you did not achieve it and asks you to roll again. 
            attempts += 1
            print("You did not score higher than your selected height.")
        if height not in L:
            print("This is an invalid number.")
            height = int(input("Your next VALID selected height: "))
while height in L and attempts == 3: # When trying to achieve a high score, if the user fails to get the higher score within 3 attempts, game is over. 
    print("You failed to score higher than your selected and used all 3 attempts.")
    print("Gamer over!")
    print("Your highest score was",a_height,) # While trying to achieve a height, If the user uses all 3 attempts. It prints your highest achieved height and ends a game.
    break
