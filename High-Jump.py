import random # To use "random.randint". 
attempts = 1
max_height = 0
L = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30] # List of the available heights. 
print("The following heights are available.")
print(L) 
height = int(input("Your chosen height: "))
while height not in L: # If the entered number not in the list, it will print "Invalid Number". 
    print("This is an invalid number.")
    height = int(input("Your chosen height: "))
while height in L: # If the entered number is in the list, it will continue. 
    roll = input("Enter \"roll\" to roll all 5 dice: ")
    if roll == "roll":
        # Program chooses random number for the dice roll. 
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        d4 = random.randint(1,6)
        d5 = random.randint(1,6)
        # This prints the dice that first dice is equal to. 
        if d1 == 1:
            print(u"\u2680")
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
        # Prints the euqal dice for 2nd dice. 
        if d2 == 1:
            print(u"\u2680")
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
        # Prints the equal dice for 3th dice.     
        if d3 == 1:
            print(u"\u2680")
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
        # Prints the equal dice for 4th dice. 
        if d4 == 1:
            print(u"\u2680")
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
        # Prints the equal dice for 5th dice. 
        if d5 == 1:
            print(u"\u2680")
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
    sum = d1 + d2 + d3 + d4 + d5 # This will sum up the random dice numbers.
    while attempts < 3:
        if sum >= height: # Summed up the numbers so the code can compare it to the entered number by the player. 
            max_height = height
            print("You managed to scored higher than your chosen height.")
            print("Your current highest score is",max_height,)
            attempts = 1
            height = int(input("Your next chosen height: "))
            roll = input("Enter \"roll\" to roll all 5 dice: ")
        elif sum < height:
            print("Your total was not higher than your chosen height.")
            attempts += 1
            change = input("If you want to change your chosen height, enter \"0\" if not enter \"pass\": ")
            # This asks the user if they want to change their choice after an unsuccessful attempt. 
            if change == "0":
                attempts = 1
                height = int(input("Your next chosen height: "))
                roll = input("Enter \"roll\" to roll all 5 dice: ")
            elif change == "pass":
                roll = input("Enter \"roll\" to roll all 5 dice: ")
    while attempts == 3:
        # This removes the number you were trying to achieve when you hit 3 attempts. 
        if height == 10:
            # While you are playing to achieve height 10, if after all 3 attempts it's still not achieved, it will remove it from list.
            # Same for every other height. 
            print("You can't use this height anymore.")
            print("You used all 3 attempts. ")
            L.remove(10)
            print("The following are the heights that are left.")
            print(L)
            attempts = 1
            height = int(input("Your next chosen height: "))
        elif height == 12:
            print("You can't use this height anymore.")
            print("You used all 3 attempts. ")
            L.remove(12) # Removes the height the user was trying to achive after 3 attempts. 
            print("The following are the heights that are left.")
            print(L)
            attempts = 1
            height = int(input("Your next chosen height: "))
        elif height == 14:
            print("You can't use this height anymore.")
            print("You used all 3 attempts. ")
            L.remove(14)
            print("The following are the heights that are left.")
            print(L)
            attempts = 1
            height = int(input("Your next chosen height: "))
        elif height == 16:
            print("You can't use this height anymore.")
            print("You used all 3 attempts. ")
            L.remove(16)
            print("The following are the heights that are left.")
            print(L)
            attempts = 1
            height = int(input("Your next chosen height: "))
        elif height == 18:
            print("You can't use this height anymore.")
            print("You used all 3 attempts. ")
            L.remove(18)
            print("The following are the heights that are left.")
            print(L)
            attempts = 1
            height = int(input("Your next chosen height: "))
        elif height == 20:
            print("You can't use this height anymore.")
            print("You used all 3 attempts. ")
            L.remove(20)
            print("The following are the heights that are left.")
            print(L)
            attempts = 1
            height = int(input("Your next chosen height: "))
        elif height == 22:
            print("You can't use this height anymore.")
            print("You used all 3 attempts. ")
            L.remove(22)
            print("The following are the heights that are left.")
            print(L)
            attempts = 1
            height = int(input("Your next chosen height: "))
        elif height == 24:
            print("You can't use this height anymore.")
            print("You used all 3 attempts. ")
            L.remove(24)
            print("The following are the heights that are left.")
            print(L)
            attempts = 1
            height = int(input("Your next chosen height: "))
        elif height == 26:
            print("You can't use this height anymore.")
            print("You used all 3 attempts. ")
            L.remove(26)
            print("The following are the heights that are left.")
            print(L)
            attempts = 1
            height = int(input("Your next chosen height: "))
        elif height == 28:
            print("You can't use this height anymore.")
            print("You used all 3 attempts. ")
            L.remove(28)
            print("The following are the heights that are left.")
            print(L)
            attempts = 1
            height = int(input("Your next chosen height: "))
        elif height == 30:
            print("You can't use this height anymore.")
            print("You used all 3 attempts. ")
            L.remove(30)
            print("The following are the heights that are left.")
            print(L)
            attempts = 1
            height = int(input("Your next chosen height: "))
while max_height == 30:
    print("You WON!") 
    print("You scored the highest possible height in the game.")
    # If the highest achievable height is achieved, it ends the game and prints that the user won. 
    break
