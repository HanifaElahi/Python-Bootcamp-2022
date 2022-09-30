import random
from game_data import data
from art import logo, vs
#from replit import clear

# Add art.
#print(logo)


# Generate a random account from the game data.
def get_random_account():
    """Get data from random account"""
    return random.choice(data)


# Format account data into printable format.
def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


# Check if user is correct.
def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right.Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


## If Statement
# Make game repeatable.
# Make B become the next A.


def game():
    print(logo)
    score = 0
    game_should_continue = True
    # Generate a random account from the game data.
    account_a = get_random_account()
    account_b = get_random_account()

    # Make game repeatable
    while game_should_continue:

        # Making account at position B become the next account at position A
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        # Format account data into printable format.
        print(f"\nCompare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask user for a guess.
        guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        ## Get follower count.
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        # Check if user is correct.
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        #clear()
        print(logo)

        # Give User Feedback
        # Score Keeping
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
