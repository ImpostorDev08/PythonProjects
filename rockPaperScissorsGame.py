import random
options = ("rock", "paper", "scissors")
playing = True
while playing:
    player = input("Choose rock, paper, scissors: ").lower()
    computer = random.choice(options)
    print(f"Player:{player}")
    print(f"Computer:{computer}")
    if player not in options:
        playing = False
    if ((player == "rock") and (computer == "scissors")) or ((player == "scissors") and (computer == "paper")) or ((player == "paper") and (computer == "rock")):
        print("You win")
    elif player == computer:
        print("Its a tie")
    else:
        print("You lose")
    if input("Do you wish to continue? y/n: ").lower() == "n":
        playing = False