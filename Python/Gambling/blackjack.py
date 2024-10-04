import random

def intro(bal):
  print('''
----------------------------------------------------------------------------
      ''')
  print("Yo, welcome to Blackjack!")
  print("Beat the dealer and win big!")
  print(f"Your balance is: {bal}")

def wager(bal):
  while True:
    try:
      wager = int(input("Throw down your wager: "))
      if wager < 100:
        print("Gotta bet at least 100, man.")
        continue
      if wager > bal:
        print("Not enough cash, my friend.")
        continue
      return wager
    except ValueError:
      print("C'mon, gimme a number, not gibberish")

def deal_cards():
  cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

  hand = [random.choice(cards) for _ in range(2)]
  numeric_hand = [card_value(card) for card in hand]

  return hand, numeric_hand
  
def card_value(card):
  if card in ["J", "Q", "K"]:
    return 10
  elif card == "A":
    return 11
  else:
    return card

def decision(hand, numeric_hand):
  if sum(numeric_hand) == 21:
    return "stand", sum(numeric_hand)

  while True:
    choice = input("Would you like to \"hit\" or \"stand\"? ")
    if choice == "hit":
      new_card = 
      print(f"You got a {new_card}")
      n_c_numeric = card_value(new_card)
      numeric_hand.append(n_c_numeric)

    
  
def play(hand, dealer_hand, bal, wager, h_numeric, d_h_numeric):  
  print(f"You got a {hand[0]} and a {hand[1]}.")
  print(f"Your total is {sum(h_numeric)}")
  print(f"The dealer's face-up card is {dealer_hand[0]}.")
  
  

def blackjack(bal):
  intro(bal)

  while bal > 0:
    w = wager(bal)
    h, h_numeric = deal_cards()
    d_h, d_h_numeric = deal_cards()
    
  