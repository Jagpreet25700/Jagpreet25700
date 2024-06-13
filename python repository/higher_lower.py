from data_higher_lower import data
import random as ram
import Higher_lower_logo as h
from replit import clear

def format_data(account):
    """Takes the account data and converts it into a printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name},{account_description},{account_country}"

def check_answer(guess,a_followers,b_followers):
    """Takes the user counts and check whether the user's guess is correct or not."""
    if a_followers > b_followers and guess == "a":
        return guess == "a"
    else:
        return guess == "b"  

# display art
print(h.logo)
score = 0
account_b = ram.choice(data)
#generate a random account
game_continue = True
while game_continue: 


    account_a = account_b
    account_b = ram.choice(data)
    while account_a == account_b:
        account_b = ram.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(h.vs)
    print(f"Compare B: {format_data(account_b)}.")  

    #make a guess

    guess = input("Who has more followers? Type A or B: ").lower()
    #get follower count
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    clear()
    # give user the feedback
    if is_correct:
        score +=1
        print(f"You are right. Your score is {score}")
    else:
        game_continue = False
        print(f"You are wrong.Your score is {score}")

# make the game repeatable        