import pyfiglet
from slot import slots
from roulette import roulette


bal = 5000

print(pyfiglet.figlet_format("Le Gamblin Den"))

while True:
  print("----------------------------------------------------------------------------")
  print('''
Here are the games that we have:

  1. Slots
  2. Roulette
  3. Blackjack
''')

  choice = 0
  while choice not in [1, 2, 3]:
    try:
      choice = int(input("Enter your choice: "))
      if choice not in [1, 2, 3]:
        print("Please enter a valid choice.")
    except ValueError:
      print("Please enter a number.")


  while True:
    if choice == 1:
      bal = slots(bal)
      print(f"Your new balance is {bal}.")
    elif choice == 2:
      bal = roulette(bal)
      print(f"Your new balance is {bal}.")
    elif choice == 3:
      print("Work in progess")
    
    print('''
----------------------------------------------------------------------------
      ''')

    if bal <= 0:
      print("You're broke, man. Better luck next time.")
      exit()
    
    replay = input("Do you want to play another game (y/n)? ").lower()
    while replay not in ["y", "n"]:
      print("Please select 'y' or 'n'.")
      replay = input("Do you want to play another game (y/n)? ").lower()
      
    if replay == "n":
      print("Come again!")
      exit()

    break