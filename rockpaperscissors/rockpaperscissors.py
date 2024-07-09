# This is a rock paper scissors game
import random

#ask the user to enter their name
name = input("Hello User! What is your name? ") 
print("Nice to meet you, " + name + "!")

#ask the user if they know how to play
print("\nThis is a very simple rock, paper, scissors game.")
ans = input("Are you familiar with the rules of the game? (type Y or N) ")

#if they do, no need to show the rules
if (ans == "Y"):
    print("\nOk cool, I won't delve into the rules then.")
    
#if they dont, show the rules of the game
elif (ans == "N"):
    print("\nThe rules are fairly simple to learn!")
    print("Basically, you will be playing against me (The CPU)")
    print("\nYou have to pick one of three options (Rock, Paper, or Scissors)")
    print("I will also pick one of the three")
    print("Based on what you pick, you will either win or lose.")
    
    print("\nIf you pick Paper and I pick Rock, you win and vice versa")
    print("If you pick Scissors and I pick Paper, you win and vice versa")
    print("If you pick Rock and I pick Scissors, you win and vice versa")
    
print("\nLet's get started!")

#define the three options
options = ["Rock", "Paper", "Scissors"]


while True:
    #have the computer pick between one of the options randomly (make sure random is imported)
    compOption = random.choice(options)

    #ask the user to choose one of the three options
    userOption = input("Choose Rock, Paper, or Scissors: ")
    
    if userOption not in options:
        print("\nThat is not a valid option, please try again")
        continue
    
    print(f"You chose {userOption} and I chose {compOption}")
        
    if (userOption == "Paper" and compOption == "Rock"):
        print("\nYou won!")
    elif (userOption == "Rock" and compOption == "Paper"):
        print("\nI win!")   
    elif (userOption == "Scissors" and compOption == "Paper"):
        print("\nYou won!")
    elif (userOption == "Paper" and compOption == "Scissors"): 
        print("\nI win!")   
    elif (userOption == "Rock" and compOption == "Scissors"):
        print("\nYou won!")
    elif(userOption == "Scissors" and compOption == "Rock"):
        print("\nI win!")
    elif (userOption == "Rock" and compOption == "Rock"):
        print("\nWe both chose Rock, it's a tie!")
    elif (userOption == "Paper" and compOption == "Paper"):
        print("\nWe both chose Paper, it's a tie!")
    elif (userOption == "Scissors" and compOption == "Scissors"):
        print("\nWe both chose Scissors, it's a tie!")
       
    restartOption = input("Do you want to play again? (type Y or N): ")
    
    if restartOption != "Y":
        break    

    