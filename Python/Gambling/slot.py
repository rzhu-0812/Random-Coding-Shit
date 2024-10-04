import sys
import random
import time

def intro(bal):
  print('''
----------------------------------------------------------------------------
    ''')
  print("Yo, welcome to Slots!")
  print("Match three symbols in a row for the win!")
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

def spinning():
  sys.stdout.write("\033[F")
  sys.stdout.write("\033[K")

  symbols = ["💎 ", "🍒 ", "🪙 ", "💰 ", "⭐ "]
  spin = ""

  for _ in range(3):
    spin += random.choice(symbols)
  
  return spin

def play(bal, wager):
  spin_duration = 0.05
  for _ in range(10):
    spin = spinning()
    print(spin)
    time.sleep(spin_duration)
    spin_duration += 0.05

  if len(set(spin)) == 1:
    bal += wager * 3
    print(f"Boom! You win {wager * 3}!")
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

def slots(bal):
  intro(bal)

  while bal > 0:
    w = wager(bal)
    bal = play(bal, w)

    r = replay()
    if r == "n":
      break
      
    print(f"Your new balance is {bal}.")

  return bal

slots(500)