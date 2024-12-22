import random

# defining range for the game 

#try catch block for correct input by user 
def user_input_check(llim, ulim):
    while True:
        try:
            user_guess = int(
                input(f"\nEnter number between {llim} to {ulim}: ")
            )
            while user_guess > ulim or user_guess < llim:
                if user_guess > ulim:
                    user_guess = int(
                        input(
                            f"\nYour guess exceeds the upper range. Lower your guess and try again.\nEnter number between {llim} to {ulim}: "
                        )
                    )
                if user_guess < llim:
                    user_guess = int(
                        input(
                            f"\nYour guess exceeds the lower range. Increase your guess and try again.\nEnter number between {llim} to {ulim}: "
                        )
                    )
            return user_guess
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# function to handle checking user input against random number and upper/lower bounds
def guess(num, user_guess, num_of_guesses):
    upper_limit = 10
    lower_limit = 1
    while num != user_guess:
        if num > user_guess:
            print(f"\nNumber is higher than {user_guess}")
            lower_limit = user_guess
            user_guess = user_input_check(lower_limit + 1, upper_limit)
            num_of_guesses = num_of_guesses + 1
        elif num < user_guess:
            print(f"\nNumber is lower than {user_guess}")
            upper_limit = user_guess
            user_guess = user_input_check(lower_limit, upper_limit - 1)
            num_of_guesses = num_of_guesses + 1
        else:
            print()
    print(f"\nCongrats! You've guessed the correct number! It was {num}.\n")
    print(f"\nYou have tried {num_of_guesses+1} times to find the number.\n")


#start and asking the user to play
while True:
    play_y_n = input(
        "Welcome to INT Guesser GAME.\nIf you'd like to play: \npress 'Y' \nor \npress 'X' if you want to exit: "
    )
    if play_y_n.lower() == "y":
        ulim= int(
                input("\nEnter number for upper limit of range: ")
            )
        llim= int(
                input("\nEnter number for lower limit of range: ")
            )
        num_of_guesses = 0
        num = random.randint(llim, ulim)
        user_guess = user_input_check(llim, ulim)
        guess(num, user_guess, num_of_guesses)
    else:
        print("Thanks for playing!")
        break