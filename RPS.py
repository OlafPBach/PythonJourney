import random
import time

You_Points = 0 #Everyone starts at 0 points
Ai_Points = 0
Options = ["r","p","s"] #Key: 0: Rock, 1: Paper, 2: Scissors
Words = ["Rock","Paper","Scissors"]

try: #Defining the Number of Rounds
    Num_Rounds = int(input("How many rounds do you want to play? "))
    if Num_Rounds < 1:
        Num_Rounds = int("Error")
except Exception:
    print("Invalid input for number of rounds, must be a positive integer")
    Num_Rounds = 0

for rr in range(Num_Rounds): #Start a Round
    print("\nYou: " + str(You_Points) + "  Ai: " + str(Ai_Points) + "  rounds left: " + str(Num_Rounds - rr))

    AiChoice = random.randint(0,2) #Ai Choice

    YouChoice = 4 #Start with an unnexceptable value
    while not (YouChoice in range(3)): #Is Player Choice Valid?
        try: #Define Player Choice
            YouChoice = Options.index(input("What are you playing? (r,p,s): ").lower())
        except Exception: #Player Choice is Invalid
            print("Unsupported Choice, the choices are r,p,s")
        finally: #Regardless, sleep for a tenth of a second
            time.sleep(0.1)

    print("You Chose " + Words[YouChoice])
    time.sleep(0.5)
    print("The computer chose " + Words[AiChoice])
    time.sleep(0.5)

    Result = (YouChoice - AiChoice) % 3 #Modulus 3
    if Result == 1:
        print("You Win!")
        You_Points += 1
    elif Result == 2:
        print("You Lose..")
        Ai_Points += 1
    else: #Result == 0:
        print("It's a Draw.")
    time.sleep(0.7)

    #If Game is Unwinnable, and it's not the last turn, then end the game
    if max([You_Points,Ai_Points]) > Num_Rounds/2 and (rr != Num_Rounds-1):
        if You_Points > Ai_Points:
            print("Game is Unlossable")
        else: #The Opposite Case
            print("Game is Unwinnable")
        break

if Num_Rounds > 0: #Print Results
    print("\nFinal Results\nYou: " + str(You_Points) + "  Ai: " + str(Ai_Points))
    time.sleep(0.1)
    if You_Points > Ai_Points:
        print("You Won The Game!")
    elif You_Points < Ai_Points:
        print("You Lost The Game..")
    else:
        print("In the End, It's a Draw.")