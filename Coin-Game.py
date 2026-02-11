import random
ans = input("""Welcome to the Coin Flip Game!
In this game, you will guess the outcome of a coin flip.
Choose a method to toss the coin:
1. Using random.random()
2. Using random.randint()
Enter your choice (1 or 2): """)
if ans not in ['1', '2']:
    print("Invalid choice. Please restart the game and choose 1 or 2.")
    exit()
elif ans == '1':
    toss = input("You chose random.random(). Guess the outcome (heads/tails): ").lower()
    if toss not in ['heads', 'tails']:
        print("Invalid guess. Please restart the game and choose heads or tails.")
        exit()
    flip = 'heads' if random.random() < 0.5 else 'tails'
    print(f"The coin landed on {flip}.")
else:
    toss = input("You chose random.randint(). Guess the outcome (heads/tails): ").lower()
    if toss not in ['heads', 'tails']:
        print("Invalid guess. Please restart the game and choose heads or tails.")
        exit()
    flip = 'heads' if random.randint(0, 1) == 0 else 'tails'
    print(f"The coin landed on {flip}.")
if toss == flip:
    print("Congratulations! You guessed correctly.")
    print("You win!")
    