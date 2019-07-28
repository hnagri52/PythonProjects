import random
from datetime import datetime as dt

computer = ["rock", "paper", "scissors"]
playgame = 'yes'
cwins = 0
pwins = 0


while playgame == "yes" or playgame == "y":
    try:
        ans = input("You are now playing rock paper scissors against a computer! Enter your choice: ")
        comp = str(random.choice(computer))

        if comp.lower() == "rock" and ans.lower() == "rock":
            print(f"Tie game! The computer was a {comp} and you were a {ans}")
            cwins = cwins +1
            pwins = pwins +1
            playgame = input("Would you like to play again? ")
        elif comp.lower() == "rock" and ans.lower() == "paper":
            print(f"You won the game! The computer was a {comp} and you were a {ans}")
            playgame = input("Would you like to play again? ")
            pwins = pwins +1
        elif comp.lower() == "rock" and ans.lower() == "scissors":
            print(f"You lost the game! The computer was a {comp} and you were a {ans}")
            playgame = input("Would you like to play again? ")
            cwins = cwins + 1
        elif comp.lower() == "paper" and ans.lower() == "paper":
            print(f"Tie game! The computer was a {comp} and you were a {ans}")
            playgame = input("Would you like to play again? ")
            cwins = cwins + 1
            pwins = pwins + 1
        elif comp.lower() == "paper" and ans.lower() == "scissors":
            print(f"You won the game! The computer was a {comp} and you were a {ans}")
            playgame = input("Would you like to play again? ")
            pwins = pwins + 1
        elif comp.lower() == "paper" and ans.lower() == "rock":
            print(f"You lost the game! The computer was a {comp} and you were a {ans}")
            playgame = input("Would you like to play again? ")
            cwins = cwins + 1
        elif comp.lower() == "scissors" and ans.lower() == "scissors":
            print(f"You tied the game! The computer was a {comp} and you were a {ans}")
            playgame = input("Would you like to play again? ")
            cwins = cwins + 1
            pwins = pwins + 1
        elif comp.lower() == "scissors" and ans.lower() == "paper":
            print(f"You lost the game! The computer was a {comp} and you were a {ans}")
            playgame = input("Would you like to play again? ")
            cwins = cwins + 1
        elif comp.lower() == "scissors" and ans.lower() == "rock":
            print(f"You won the game! The computer was a {comp} and you were a {ans}")
            playgame = input("Would you like to play again? ")
            pwins = pwins + 1
    except Exception as e:
        print(e)
if cwins > pwins:
    print(f"The computer won {cwins} times and you won {pwins} times. Computer wins ")
elif cwins < pwins:
    print(f"The computer won {cwins} times and you won {pwins} times. You won! ")
if cwins == pwins:
    print(f"The computer won {cwins} times and you won {pwins} times. Tie Game ")
