import random  # Importing the random module to generate random choices for the computer

def get_user_choice():
    while True:
        # Get the player's choice and convert it to uppercase to handle case-insensitive input
        choice = input("Rock, Paper, or Scissors? (r/p/s): ").upper()
        # If the player's choice is not 'R', 'P', or 'S', it is invalid, so we ask again
        if choice not in ["R", "P", "S"]:
            print("Invalid choice!")
            continue  # Go back to the start of the loop to ask for a valid input
        else:
            return  choice

while True:  # Start of the game loop, runs indefinitely until the player decides to quit
    choice = get_user_choice()
    # Display the player's choice
    if choice == "R":
        print("You chose Rock")
    elif choice == "P":
        print("You chose Paper")
    elif choice == "S":
        print("You chose Scissors")

    # Generate a random choice for the computer (1 for Rock, 2 for Paper, 3 for Scissors)
    computer_choice = random.randint(1, 3)

    # Map the random number to the computer's choice and display it
    if computer_choice == 1:
        computer = "R"
        print("Computer Chose Rock")
    elif computer_choice == 2:
        computer = "P"
        print("Computer Chose Paper")
    elif computer_choice == 3:
        computer = "S"
        print("Computer Chose Scissors")

    # Check if it's a tie (both player and computer chose the same)
    if choice == computer:
        print("Tie game")
    # Check if the player wins (Rock beats Scissors, Paper beats Rock, Scissors beat Paper)
    elif (choice == "R" and computer == "S") or (choice == "P" and computer == "R") or (choice == "S" and computer == "P"):
        print("You win")
    # If it's not a tie and the player doesn't win, the computer wins
    elif (computer == "R" and choice == "S") or (computer == "P" and choice == "R") or (computer == "S" and choice == "P"):
        print("Computer Wins")

    # Ask if the player wants to play again and convert input to uppercase
    play_again = input("Do you want to play again? (y/n): ").upper()

    # If the player doesn't enter 'Y', thank them and break the loop to end the game
    if play_again != "Y":
        print("Thanks For Playing!")
        break  # Exit the loop and end the game
