import random
from game_data import data
import art


# format the account data
def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

# Check if guess is correct
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a" # if guess is A then True, if B then False
    else:
        return user_guess == "b"

# display art
print(art.logo)

score = 0
game_should_continue = True
accountB = random.choice(data)

while game_should_continue:     # Make the game repeatable

    # generate random account from game_data
    # making the account at position B to go to position A
    accountA = accountB
    accountB = random.choice(data)


    if accountA == accountB:
        accountB = random.choice(data)

    # Print account data
    print(f"Compare A: {format_data(accountA)}")
    print(art.vs)
    print(f"Against B: {format_data(accountB)}")

    # ask the user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # clear the screen & reprint logo
    print("\n" * 20)
    print(art.logo)

    # check if user guess is correct
    ## get follower count of each account
    followersA = accountA["follower_count"]
    followersB = accountB["follower_count"]

    ## use if statement to check if user guess is correct
    is_correct = check_answer(guess, followersA, followersB)

    # score keeping


    # Give user feedback on their guess
    if is_correct:
        score += 1
        print("You are correct! Correct score:", score)
    else:
        print("You are wrong! Final score:", score)
        game_should_continue = False
