import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid choice. Please choose rock, paper, or scissors.")

def determine_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    rounds = int(input("How many rounds would you like to play? "))
    player_score = 0
    computer_score = 0

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)

        if winner == "player":
            print("You win this round!")
            player_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("This round is a draw!")

    print("\nFinal Results:")
    print(f"Your score: {player_score}")
    print(f"Computer's score: {computer_score}")

    if player_score > computer_score:
        print("Congratulations, you are the overall winner!")
    elif player_score < computer_score:
        print("The computer is the overall winner. Better luck next time!")
    else:
        print("The game ends in a draw!")

if __name__ == "__main__":
    play_game()