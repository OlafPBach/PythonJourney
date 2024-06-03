import random as rand
import math
RN = [
    rand.randint(1,10),rand.randint(1,10),
    rand.randint(1,10),
    rand.randint(1,5),
    rand.randint(1,10),rand.randint(1,10)
] #Generate some random numbers for the questions

questions = {#unsure how to store values temporarily to both sides of a dictionary
    "What is "+str(RN[0])+" + "+str(RN[1])+"? ": str(RN[0]+RN[1]),
    "What is the square root of "+str(RN[2]**2)+"? ": str(RN[2]),
    "What is "+str(RN[3])+"! ? ": str(math.factorial(RN[3])),
    "What is "+str(RN[4])+" mod "+str(RN[5])+"?": str(RN[4] % RN[5])
} #Generate the questions

try: #Defining the Number of Rounds
    Num_Rounds = int(input("How many rounds do you want to play? "))
    if Num_Rounds < 1:
        Num_Rounds = int("Error")
    elif Num_Rounds > len(questions):
        print("We don't have that many questions, setting to max")
        Num_Rounds = len(questions)
except Exception:
    print("Invalid input for number of rounds, must be a positive integer")
    Num_Rounds = 0

Score = 0 #Start with the score as 0
Order = list(range(0,len(questions)))
rand.shuffle(Order)
for qq in Order[0:Num_Rounds]:
    print("\nQuestion 1:\n"+list(questions.keys())[qq])
    Answer = input("Answer: ")
    if Answer == list(questions.values())[qq]:
        print("Correct!")
        Score += 1
        print("Score: "+str(Score))
    else:
        print("Incorrect!")
        print("Score: " + str(Score))

if Num_Rounds > 0:
    print("\nQuiz Completed!\nFinal Score: "+str(Score))