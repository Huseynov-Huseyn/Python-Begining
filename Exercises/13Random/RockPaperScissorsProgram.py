import random

options = ("rock", "paper", "scissors")
is_running = True
health = 3

while is_running:
    if health == 0:
        is_running = False
    else:
        player = None
        computer = random.choice(options)
        while player not in options:
            player = input("Enter a choice (rock,paper OR scissors): ").lower()

        print(f"Player choice : {player}")
        print(f"Computer choice : {computer}")

        if computer == player:
            print("Tie!")
        elif computer == "rock" and player == "paper":
            print("Player win!")
        elif computer == "paper" and player == "scissors":
            print("Player win!")
        elif computer == "scissors" and player == "rock":
            print("Player win!")
        else:
            print("Computer win!")
            health -= 1
            print(f"Your current health: {health}")

print("You lose the game!")
