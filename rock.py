import random

def get_user_choice():
    """Get a valid user choice."""
    while True:
        user_action = input("Enter a choice (rock, paper, scissors): ").strip().lower()
        if user_action in ["rock", "paper", "scissors"]:
            return user_action
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(user_action, computer_action):
    """Determine the winner of the game."""
    if user_action == computer_action:
        return "It's a tie!"
    elif (user_action == "rock" and computer_action == "scissors") or \
         (user_action == "paper" and computer_action == "rock") or \
         (user_action == "scissors" and computer_action == "paper"):
        return "You win!"
    else:
        return "You lose."

def main():
    possible_actions = ["rock", "paper", "scissors"]
    user_action = get_user_choice()
    computer_action = random.choice(possible_actions)
    
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    
    print(determine_winner(user_action, computer_action))

if __name__== "__main__":
    main()