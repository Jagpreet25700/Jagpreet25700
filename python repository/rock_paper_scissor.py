#rock paper scissor

import random as ram

select = int(input ("Welcome to the game of Rock,Paper,Scisssor. Please type 0 for Rock,  1 for Paper and  2 for Scissor: "))

ramdom = ram.randint(0,2)
print(f"The computer selected {ramdom}")

if select == 0 and ramdom == 0:
    print("Draw")
elif select == 0 and ramdom == 1:
    print("You selected Rock and computer Paper. You lose")
elif select == 0 and ramdom == 2:
    print("You have selected Rock and computer Scissor. You win.")
elif select == 1 and ramdom == 0:
    print("You have selected paper and computer selected rock. You win")
elif select == 1 and ramdom == 1:
    print("Draw")
elif select == 1 and ramdom == 2:
    print("You have selected paper and computer Scissor. You loss.")    
elif select == 2 and ramdom == 0:
    print("You selected scissor and computer Rock. You loss")
elif select == 2 and ramdom == 1:
    print("You selected scissor and computer paper. You win")
elif select == 2 and ramdom == 2:
    print("Draw")