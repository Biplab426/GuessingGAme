import random
jackpot = random.randint(1,100)
guess = int(input("Guess an number"))
while guess!= jackpot:
    if guess<jackpot:
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input("Guess an number"))
   
   

print("Correct")

            