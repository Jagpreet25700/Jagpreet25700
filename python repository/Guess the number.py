import random as ram
import itertools as tools
from Guess_the_number_logo import logo

print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_guess(guess,answer,turns):
    """Check answer against guess and return the number"""    
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it.The answer is {answer}")         

def set_difficulty():
    level = input("Please choose the level you would like to select. Type 'Easy' or 'Hard': ")
    if level == "Easy" or level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS    


def game():
    turns = set_difficulty()
    number = list(tools.islice(tools.count(1),100))
    print("Welcome to Number Guessing Game!\nI am thinking of a number bewteen 1 and 100")
    answer = ram.choice(number)
    print(f"You have {turns} left")
    guess= 0
    while guess != answer:
        print(f"You have {turns} attempts left")
        guess= int(input("Please choice a number: "))
        turns = check_guess(guess,answer,turns)
        if turns == 0:
            print(f"You run out guess. You lose!! The answer is {answer}")
            return
game()        