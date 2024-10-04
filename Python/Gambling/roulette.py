import random
import math

def intro(bal):
  print('''
----------------------------------------------------------------------------
      ''')
  print("Yo, welcome to Roulette!")
  print("Place your bet and try your luck!")
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

def bet_type():
  while True:
    bet_type = input("Yo, what's your bet type (number/even/odd): ").lower()
    if bet_type in ["number", "even", "odd"]:
      return bet_type
    else:
      print("Bro, you didn't even choose a valid choice.")

def user_num():
  while True:
    try:
      user_num = int(input("What number you bettin' on (0 to 36)? "))
      if 0 <= user_num <= 36:
        return user_num
      else:
        print("Hold up, that ain't valid.")
    except ValueError:
      print("Bruh, that ain't even a number.")

def play(bal, wager, bet_type, user_num):
  win_num = random.randint(0, 36)
  print(f"The winning number is {win_num}.")

  if bet_type == "number" and user_num == win_num:
    bal += wager * 3
    print(f"Boom! You win {wager * 3}!")
  elif (bet_type == "even" and win_num % 2 == 0) or (bet_type == "odd" and win_num % 2 != 0):
    bal += math.floor(wager * 0.05)
    print(f"Boom! You win {math.floor(wager * 0.05)}!")
  else:
    bal -= wager
    print("Tough! Better luck next time.")

  return bal

def replay():
  replay = input("Wanna go again (y/n)? ").lower()
  while replay not in ["y", "n"]:
    print("Select 'y' or 'n'.")
    replay = input("Wanna go again (y/n)? ").lower()
  return replay
  
def roulette(bal):
  intro(bal)

# w = wager, b_t = bet_type, u_n = user_num
  while bal > 0:
    w = wager(bal)
    b_t = bet_type()
    u_n = user_num() if b_t == "number" else None
    
    bal = play(bal, w, b_t, u_n)
    
    r = replay()
    if r == "n":
      break
    
    print(f"Your new balance is {bal}.")

  return bal
