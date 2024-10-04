import random

# Function to get user's choice in own range or generating a random range
def get_user_choice():
    user_choice = None
    while user_choice not in [1, 2]:
        try:
            user_choice = int(
                input(
                    "\nChoose an option:\n1. Enter your own range\n2. Generate a random range\nEnter option number: "
                )
            )
        except ValueError:
            print("Please choose a valid option (1 or 2).")
    return user_choice


# Function to get user's own range of positive integers
def get_user_range():
    print("\nEnter a range of positive integers you would like to guess from.")
    while True:
        try:
            num_low = int(input("Enter lower range: "))
            num_high = int(input("Enter upper range: "))
            if num_low < 1 or num_high < 1:
                print("Please choose numbers greater than zero.")
            elif num_low > num_high:
                print("The lower range can't be greater than the upper range.")
            elif abs(num_low - num_high) < 10:
                print("Please choose numbers at least 10 values away.")
            else:
                return num_low, num_high
        except ValueError:
            print("Please choose a valid integer")


# Function to generate a random range of positive integers
def get_random_range():
    while True:
        num_low = random.randint(1, 50)
        num_high = random.randint(51, 100)

        if abs(num_low - num_high) >= 10:  # Ensure a valid range
            break

    print(f"\nThe range is from {num_low} to {num_high}.")
    return num_low, num_high


# Function to generate hints based on the secret number
def get_hints(num, num_low, num_high):
    hints = []
    prime_num = all(num % j != 0 for j in range(2, int(num ** 0.5) + 1))
    for i in range(3, 10):
        if num % i == 0:
            hints.append(f"The number is divisible by {i}")
    if num < ((num_high + num_low) // 2):
        hints.append(
            f"The number is between {num_low} and {(num_high + num_low) // 2}."
        )
    else:
        hints.append(
            f"The number is between {(num_high + num_low) // 2} and {num_high}."
        )
    hints.append("The number is even." if num % 2 == 0 else "The number is odd.")
    hints.append(
        "The number is a perfect square."
        if int(num ** 0.5) ** 2 == num
        else "The number is not a perfect square."
    )
    hints.append(
        "The number is a prime number."
        if prime_num and num > 1
        else "The number is not a prime number."
    )
    return hints


# Function to check if the user wants to allow hints
def hints_allowance():
    hints_allow = input("Do you want to allow hints (y/n)? ")
    while hints_allow.lower() not in ["y", "n"]:
        hints_allow = input("Invalid choice. Please enter 'y' or 'n'.")
    return hints_allow.lower() == "y"


# Function to start the game
def guess_number(num_low, num_high, num, hints_allow, hints):
    attempts = int((num_high - num_low + 1) ** 0.7)
    guesses = []
    while attempts > 0:
        print(f"\nYou have {attempts} attempt(s).")
        user_guess = input(
            f'Guess a number from {num_low} to {num_high} (type "q" to quit and "h" for a hint): '
        )
        if user_guess.lower() == "q":
            print("Here were your guesses: ", ", ".join(guesses))
            print("The secret number was: ", num)
            return False
        elif user_guess.lower() == "h":
            if hints_allow.lower() == "n":
                print("Sorry, hints are not allowed.")
            elif len(hints) != 0:
                if hints:
                    hint = random.choice(hints)
                    hints.remove(hint)
                    print(hint)
                else:
                    print("Sorry, you're out of hints.")
            else:
                print("Sorry, you're out of hints.")
        else:
            try:
                user_guess = int(user_guess)
                if user_guess > num_high or user_guess < num_low:
                    print("Please choose a number between your selected range.")
                elif user_guess == num:
                    print("You must be really good! You won!")
                    guesses.append(user_guess)
                    print("Here were your guesses: ", ", ".join(guesses))
                    return False
                else:
                    if abs(user_guess - num) <= 5:
                        if user_guess > num:
                            print(
                                f"{user_guess} is pretty close! It's just a little too high."
                            )
                        else:
                            print(
                                f"{user_guess} is pretty close! It's just a little too low."
                            )
                    else:
                        if user_guess > num:
                            print(f"{user_guess} is too low. Try again.")
                        else:
                            print(f"{user_guess} is too low. Try again.")
                    guesses.append(user_guess)
                    attempts -= 1
            except ValueError:
                print("Please choose a valid integer")

        if attempts == 0:
            print("You ran out of attempts!")
            print("Here were your guesses: ", ", ".join(guesses))
            print("The secret number was: ", num)
            return False


def start_game():
    print("Welcome to my Number Guessing Game")
    while True:
        user_choice = get_user_choice()
        if user_choice == 1:
            num_low, num_high = get_user_range()
        else:
            num_low, num_high = get_random_range()
        hints_allow = hints_allowance()
        num = random.randint(num_low, num_high)

        while True:
            replay = guess_number(
                num_low,
                num_high,
                num,
                str(hints_allow),
                get_hints(num, num_low, num_high),
            )
            if not replay:
                break

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    start_game()
