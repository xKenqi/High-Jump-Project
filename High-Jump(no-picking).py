print("\033[1;34;10m  \n") # Adds colour to text.  
print("Welcome to Long Jump.")
print("You have 3 attempts at each height to achive your desired height. If you use all 3 attempts at one height without scoring it, the game ends.")
print("--------------------------------------------------------------------------------")
import random # To use the "random.randint" function to make to code choose random number for dice roll. 
attempts = 0 # To count how many attempts the user is using. 
a_height = 0 # Maximum height achieved. 
L = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30] # List of heights available.
dicelist = []
start = 10
print("The following heights are available to choose from.")
print(L)
print("--------------------------------------------------------------------------------")
print("You start from 10 and work your way right until you reach 30.")
print("Enter \"Yes\" in the following question to quit the game at any given time.")
height = input("Would you like to end the game?: ")
if height == "Yes": # If the user enters "0", the game ends and prints your high score. 
    print("\033[1;31;10m  \n")
    print("You chose to quit.")
    print("Your highest score was",a_height,)
    print("\033[1;37;10m  \n")
else:
    while attempts < 3: # This loop only runs when the attempts are under 3 and entered number is in the list.
        roll = input("Enter \"y\" to roll the dice: ")
        if roll == "y":
            d1 = random.randint(1,6) # Chooses random number from 1-6 for the dice roll. 
            d2 = random.randint(1,6)
            d3 = random.randint(1,6)
            d4 = random.randint(1,6)
            d5 = random.randint(1,6)
            if d1 == 1:
                dicelist.append(u"\u2680") # Adds the dice symbol into the list so it can print in a horizontal line. 
            elif d1 == 2:
                dicelist.append(u"\u2681")
            elif d1 == 3:
                dicelist.append(u"\u2682")
            elif d1 == 4:
                dicelist.append(u"\u2683")
            elif d1 == 5:
                dicelist.append(u"\u2684")
            elif d1 == 6:
                dicelist.append(u"\u2685")
            if d2 == 1:
                dicelist.append(u"\u2680")
            elif d2 == 2:
                dicelist.append(u"\u2681")
            elif d2 == 3:
                dicelist.append(u"\u2682")
            elif d2 == 4:
                dicelist.append(u"\u2683")
            elif d2 == 5:
                dicelist.append(u"\u2684")
            elif d2 == 6:
                dicelist.append(u"\u2685")
            if d3 == 1:
                dicelist.append(u"\u2680")
            elif d3 == 2:
                dicelist.append(u"\u2681")
            elif d3 == 3:
                dicelist.append(u"\u2682")
            elif d3 == 4:
                dicelist.append(u"\u2683")
            elif d3 == 5:
                dicelist.append(u"\u2684")
            elif d3 == 6:
                dicelist.append(u"\u2685")
            if d4 == 1:
                dicelist.append(u"\u2680")
            elif d4 == 2:
                dicelist.append(u"\u2681")
            elif d4 == 3:
                dicelist.append(u"\u2682")
            elif d4 == 4:
                dicelist.append(u"\u2683")
            elif d4 == 5:
                dicelist.append(u"\u2684")
            elif d4 == 6:
                dicelist.append(u"\u2685")
            if d5 == 1:
                dicelist.append(u"\u2680")
            elif d5 == 2:
                dicelist.append(u"\u2681")
            elif d5 == 3:
                dicelist.append(u"\u2682")
            elif d5 == 4:
                dicelist.append(u"\u2683")
            elif d5 == 5:
                dicelist.append(u"\u2684")
            elif d5 == 6:
                dicelist.append(u"\u2685")
            sum = d1 + d2 + d3 + d4 + d5 # Sums up all the die.
            print(dicelist) # Prints all the dice that the user rolled in a horizontal line. 
            print("Sum of all the dice you rolled is",sum)
            if sum >= start:
                    a_height = start # If the sum is higher or equal to the choosen height, your choosen height becomes your "Highest height achieved."
                    print("\033[1;32;10m  \n")
                    print("You managed to score heigher than your selected height.")
                    print("Your current highest scored height is",a_height,)
                    print("\033[1;37;10m  \n")
                    print("\033[1;35;10m  \n")
                    print("Next height is",a_height+2)
                    print("\033[1;37;10m  \n")
                    start += 2
                    dicelist = []
                    attempts = 0
                    if a_height == 30:
                        print("Congratulations you achieved the highest height possible.")
                        break
                    height = input("Would you like to end the game? Type \"Yes\" if so: ")
                    if height == "Yes": # If the user enters "Yes", the game ends and prints your high score. 
                        print("\033[1;31;10m  \n")
                        print("You chose to quit.")
                        print("Your highest score was",a_height,)
                        print("\033[1;37;10m  \n")
                        break
                    skip = input("Would you like to skip this heigth and go on to the next one? Type \"Yes\" if so: ")
                    if skip == "Yes": # If the user wants to skip the height, user can by typing "Yes".
                        start += 2
                        print("\033[1;35;10m  \n")
                        print("You skipped this height, next height is",start)
                        print("\033[1;37;10m  \n")
            elif sum < start: # If the sum is not equal or higher than the choosen height. It prints that you did not achieve it and asks you to roll again. 
                    attempts += 1
                    print("\033[1;31;10m  \n")
                    print("You did not score higher than your selected height.")
                    print("\033[1;37;10m  \n")
                    dicelist = []
while attempts == 3: # When trying to achieve a high score, if the user fails to get the higher score within 3 attempts, game is over. 
    print("\033[1;31;10m  \n")
    print("You failed to score higher than your selected and used all 3 attempts.")
    print("Gamer over!")
    print("Your highest score was",a_height,) # While trying to achieve a height, If the user uses all 3 attempts. It prints your highest achieved height and ends a game.
    print("\033[1;37;10m  \n")
    break
