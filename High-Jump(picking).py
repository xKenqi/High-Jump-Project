print("\033[1;34;10m  \n") # Adds colour to text. 
print("Welcome to Long Jump.")
print("You have 3 attempts at each height to achive your desired height. If you use all 3 attempts at one height without scoring it, the game ends.")
print("Enter \"0\" to quit the game with your current high score.")
print("\033[1;37;10m  \n")
import random # To use the "random.randint" function to make to code choose random number for dice roll. 
attempts = 0 # To count how many attempts the user is using. 
a_height = 0 # Maximum height achieved. 
L = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30] # List of heights available.
dicelist = []
print("The following heights are available to choose from.")
print(L)
height = int(input("Your selected height: "))
while height == 0: # If the user enters "0", the game ends and prints your high score. 
    print("\033[1;34;10m  \n")
    print("You chose to quit.")
    print("Your highest score was",a_height,)
    print("\033[1;37;10m  \n")
    break
while height not in L and height >= 1: # If the number is not in the list, it prints out "invalid number". 
    print("\033[1;33;10m  \n")
    print("This is an invalid number, please choose another.")
    height = int(input("Your VALID selected height: "))
    print("\033[1;37;10m  \n")
while height in L and attempts < 3: # This loop only runs when the attempts are under 3 and entered number is in the list.
    roll = input("Enter \"y\" to roll the dice: ")
    if roll == "y":
        d1 = random.randint(1,6) # Chooses random number from 1-6 for the dice roll. 
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        d4 = random.randint(1,6)
        d5 = random.randint(1,6)
        if d1 == 1:
            dicelist.append(u"\u2680")
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
        print(dicelist)
        print("Sum of all the dice you rolled is",sum)
        if sum >= height:
            if height > a_height: # Only if the selected height is bigger than the one already achived. 
                a_height = height # If the sum is higher or equal to the choosen height, your choosen height becomes your "Highest height achieved."
            print("\033[1;32;10m  \n")
            print("You managed to score heigher than your selected height.")
            print("Your current highest scored height is",a_height,)
            print("\033[1;37;10m  \n")
            dicelist = []
            attempts = 0
            height = int(input("Your next selected height: "))
        elif sum < height: # If the sum is not equal or higher than the choosen height. It prints that you did not achieve it and asks you to roll again. 
            attempts += 1
            print("\033[1;31;10m  \n")
            print("You did not score higher than your selected height.")
            print("\033[1;37;10m  \n")
            dicelist = []
        if height == 0: # If the user enters "0", the game ends and prints your current high score. 
            print("\033[1;34;10m  \n")
            print("You chose to quit.")
            print("Your highest score was",a_height,)
            print("\033[1;37;10m  \n")
            break
        elif height not in L:
            print("\033[1;33;10m  \n")
            print("This is an invalid number.")
            height = int(input("Your next VALID selected height: "))
            print("\033[1;37;10m  \n") 
while height in L and attempts == 3: # When trying to achieve a high score, if the user fails to get the higher score within 3 attempts, game is over. 
    print("\033[1;31;10m  \n")
    print("You failed to score higher than your selected and used all 3 attempts.")
    print("Gamer over!")
    print("Your highest score was",a_height,) # While trying to achieve a height, If the user uses all 3 attempts. It prints your highest achieved height and ends a game.
    print("\033[1;37;10m  \n")
    break
