import random
from Balance import update_balance, balance

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

min_wager = 100
max_wager = 1000

dealer_min_score = 17


def get_wager(balance):
    while True:
        try:
            wager = int(
                input(
                    f"How much do you want to bet (Min: ${min_wager}, Max: ${max_wager})?\n> $ "
                )
            )
            if wager not in range(min_wager, max_wager + 1) or wager > balance:
                print(f"You can't bet ${wager}. Please input a valid bet.")
            else:
                return wager
        except ValueError:
            print("Please enter a valid integer.")


def deal_cards():
    hand = [random.choice(cards) for _ in range(2)]
    numeric_hand = [convert_card_value(card) for card in hand]
    return hand, numeric_hand


def convert_card_value(card):
    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        return 11
    else:
        return card


def user_decision(numeric_hand):
    if sum(numeric_hand) == 21:
        return "stand", sum(numeric_hand)

    while True:
        choice = input('Would you like to "hit" or "stand"? ')
        if choice == "hit":
            new_card = random.choice(cards)
            print(f"You got a {new_card}.")
            numeric_new_card = convert_card_value(new_card)
            numeric_hand.append(numeric_new_card)
            user_total = sum(numeric_hand)
            print(f"Your total is {user_total}.\n")
            if user_total > 21:
                print("You busted! Better luck next time.")
                return "bust", user_total
        elif choice == "stand":
            user_total = sum(numeric_hand)
            return "stand", user_total
        else:
            print("Please enter a valid option.")


def dealer_turn(dealer_numeric_hand):
    dealer_total = sum(dealer_numeric_hand)
    print(f"\nThe dealer's other card was {dealer_numeric_hand[1]}")
    print(f"The dealer's total is {dealer_total}")

    while dealer_total < dealer_min_score:
        print("The dealer chooses to hit.")
        new_card = random.choice(cards)
        print(f"The dealer drew a {new_card}.")
        numeric_new_card = convert_card_value(new_card)
        dealer_total += numeric_new_card
        print(f"The dealer's total is {dealer_total}.\n")

    if dealer_total > 21:
        print("The dealer busted!")
    return dealer_total


def play_again():
    while True:
        replay = input("Would you like to play again (y/n)? ")
        if replay in ["y", "n"]:
            return replay
        else:
            print("Please enter a valid option.")


def play_hand(numeric_hand, balance, wager, dealer_numeric_hand):
    print(f"You get a {numeric_hand[0]} and a {numeric_hand[1]}.")
    print(f"Your total is {sum(numeric_hand)}")
    print(f"The dealer's face-up card is {dealer_numeric_hand[0]}.")
    decision, user_total = user_decision(numeric_hand)

    while decision == "hit":
        decision, user_total = user_decision(numeric_hand)

    if decision == "bust":
        print("You lost. Better luck next time.")
        balance -= wager
    else:
        dealer_total = dealer_turn(dealer_numeric_hand)
        if dealer_total > 21 or user_total > dealer_total:
            print("Congrats! You won!")
            balance += wager
        elif user_total == dealer_total:
            print("What a bummer. You tied.")
        else:
            print("You lost. Better luck next time.")
            balance -= wager
    return balance


def split_hand(numeric_hand, balance, wager, dealer_numeric_hand):
    if numeric_hand[0] != numeric_hand[1]:
        print("You can't split your hand.")
        return numeric_hand, balance

    print("You chose to split your hand!")
    balance -= wager
    hands = {
        "hand 1": [numeric_hand[0], random.choice(cards)],
        "hand 2": [numeric_hand[1], random.choice(cards)],
    }
    numeric_hands = {
        hand_name: [convert_card_value(card) for card in hand]
        for hand_name, hand in hands.items()
    }

    for hand_name, hand in hands.items():
        print(f"\nPlaying {hand_name}!")
        print(f"You get a {hand[0]} and a {hand[1]}.")
        print(f"Your total is {sum(numeric_hands[hand_name])}")
        print(f"The dealer's face-up card is {dealer_numeric_hand[0]}.")
        decision, user_total = user_decision(hand)

        while decision == "hit":
            decision, user_total = user_decision(hand)

        if decision == "bust":
            print("You lost. Better luck next time.")
            balance -= wager
        else:
            dealer_total = dealer_turn(dealer_numeric_hand)
            if dealer_total > 21 or user_total > dealer_total:
                print("Congrats! You won!")
                balance += wager
            elif user_total == dealer_total:
                print("What a bummer. You tied.")
            else:
                print("You lost. Better luck next time.")
                balance -= wager

    return hands, balance


def play_blackjack():
    print("Welcome to my Blackjack game!")
    print(f"Your balance is ${balance}.")

    while True:
        wager = get_wager(balance)
        hand, numeric_hand = deal_cards()
        dealer_hand, dealer_numeric_hand = deal_cards()

        if numeric_hand[0] == numeric_hand[1]:
            split_choice = input("Would you like to split your hand (y/n)? ")
            if split_choice.lower() not in ["y", "n"]:
                split_choice = input("Would you like to split your hand (y/n)? ")
            elif split_choice.lower() == "y":
                hands, balance = split_hand(
                    numeric_hand, balance, wager, dealer_numeric_hand
                )
        else:
            balance = play_hand(numeric_hand, balance, wager, dealer_numeric_hand)

        print(f"Your balance is now ${balance}.")

        if balance < 100:
            print("You don't have enough money!")
            break

        replay = play_again()
        if replay.lower() == "n":
            break

    print(f"Thanks for playing! Your final balance is ${balance}")


if __name__ == "__main__":
    play_blackjack()
