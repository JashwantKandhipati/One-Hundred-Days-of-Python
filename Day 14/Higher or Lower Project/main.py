import random
from game_data import data
import art

# function to format the account data
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

# function to check if guess is correct
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# display art
print(art.logo)

score = 0
game_continue = True
accountB = random.choice(data)

while game_continue:
    # generate random account from game_data
    accountA = accountB     # making the account at position B to go to position A
    accountB = random.choice(data)

    if accountB == accountA:
        accountB = random.choice(data)

    # Print account data
    print(f"Compare A: {format_data(accountA)}")
    print(art.vs)
    print(f"Against B: {format_data(accountB)}")

    # ask the user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # clear the screen & reprint logo
    print("\n" * 15)
    print(art.logo)

    ## get follower count of each account
    followersA = accountA["follower_count"]
    followersB = accountB["follower_count"]

    # check if user guess is correct
    is_correct = check_answer(guess, followersA, followersB)

    ## use if statement to check if user guess is correct
    if is_correct:
        score += 1          # score keeping
        print("Your guess is correct! Current Score:", score)   # Give user feedback on their guess
    else:
        print("Your guess is wrong! Final Score:", score)       # Give user feedback on their guess
        game_continue = False

