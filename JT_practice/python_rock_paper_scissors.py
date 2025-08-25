import random

options = ("rock", "paper", "scissors")
playing = True

while playing:

  player = None
  computer = random.choice(options)

  while player not in options:
    player = input("Enter rock, paper, or scissors: ").lower() 

  print(f'Player: {player}')
  print(f'Computer: {computer}')

  if player == computer:
    print("It's a tie!")
  elif (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
    print("Player wins!")
  else:
    print("Computer wins!")

  if input("Do you want to play again? (yes/no): ").lower() != 'yes':
    playing = False

print("Thanks for playing!")