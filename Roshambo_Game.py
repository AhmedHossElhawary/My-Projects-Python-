import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("Welcome to Rock , Paper, Scissors Game!")
Rule = input("Press Enter to continue or type 'Help' for the rules of the game: ").lower()
while True:
    if Rule == "help":
        print("""The rules of the game are as follows:
1. Rock beats Scissors
2. Scissors beats Paper
3. Paper beats Rock
4. If both players choose the same option, it's a tie""")
        break
    elif Rule == "":
        break
    else:   
        Rule = input("Invalid input. Please press Enter to continue or type 'Help' for the rules of the game: ").lower()
while True:
    chose = input("Please choose Rock 'R', Paper 'P', or Scissors 'S': ").lower()
    options = ["rock", "paper", "scissors"]
    options_short = ["r", "p", "s"]
    while chose not in options and chose not in options_short:
        chose = input("Invalid choice. Please choose Rock 'R', Paper 'P', or Scissors 'S': ").lower()
    computer_choice = random.choice(options)
    if chose == "r":
        chose = "rock"
    elif chose == "p":
        chose = "paper"
    elif chose == "s":
        chose = "scissors"
    print(f"You chose: {chose}")
    if chose == "rock" or chose == "r":
        print(rock)
    elif chose == "paper" or chose == "p":
        print(paper)
    elif chose == "scissors" or chose == "s":
        print(scissors)
    print(f"Computer chose: {computer_choice}")
    if computer_choice == "rock":
        print(rock)
    elif computer_choice == "paper":
        print(paper)
    elif computer_choice == "scissors":
        print(scissors)
    if chose == computer_choice:
        print("It's a tie!")
    elif (chose == "rock" and computer_choice == "scissors") or \
         (chose == "scissors" and computer_choice == "paper") or \
         (chose == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("Computer wins!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    while True:
        if play_again == "no" or play_again == "n":
            print("Thanks for playing! Goodbye!") 
            break
        elif play_again != "yes" and play_again != "y":
            play_again = input("Invalid input. Do you want to play again? (yes/no): ").lower()
        else:
            break
    if play_again == "no" or play_again == "n":
        break