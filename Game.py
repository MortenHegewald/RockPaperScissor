import random

PcMoves = ("rock", "paper", "scissor")
PcChance = random.randrange(0,3)
PcChoice = PcMoves[PcChance]

choice = input("Hi, please choose a move")

if choice == "rock" and PcChoice == "rock":
    print("Both chose " + choice + ", and therefore it's a tie.")

if choice == "rock" and PcChoice == "paper":
    print("The PC chose " + PcChoice + ", and therefore you lose!")

if choice == "rock" and PcChoice == "scissor":
    print("The PC chose " + PcChoice + ", and therefore you win! ")

if choice == "paper" and PcChoice == "paper":
    print("Both chose " + choice + ", and therefore it's a tie.")

if choice == "paper" and PcChoice == "scissor":
    print("The PC chose " + PcChoice + ", and therefore you lose!")

if choice == "paper" and PcChoice == "rock":
    print("The PC chose " + PcChoice + ", and therefore you win! ")

if choice == "scissor" and PcChoice == "scissor":
    print("Both chose " + choice + ", and therefore it's a tie.")

if choice == "scissor" and PcChoice == "rock":
    print("The PC chose " + PcChoice + ", and therefore you lose!")

if choice == "scissor" and PcChoice == "paper":
    print("The PC chose " + PcChoice + ", and therefore you win! ")
if choice != "scissor" and choice != "rock" and choice != "paper":
    print("Sorry, that's not a valid move.")
