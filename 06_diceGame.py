import random

def roll_dice():
    print("Rolling the dice...")
    num = random.randint(1, 6)
    print(f"You rolled a {num}")
    return num

def play_game():
    score = 0

    start = input("Do you want to start the game? (yes/no): ").strip().lower()
    if start != "yes":
        print("Maybe next time! 👋")
        return

    while True:
        random_num = roll_dice()
        if random_num == 1:
            print("You rolled a 1! Game over.")
            print(f"Your final score is: {score}")
            break

        score += random_num
        print(f"Your current score is: {score}")

        if score >= 50:
            print("🎉 Congratulations! You've reached a score of 50!")
            break

        play = input("Do you want to roll again? (yes/no): ").strip().lower()
        if play != 'yes':
            print("Thanks for playing!")
            print(f"Your final score is: {score}")
            break

if __name__ == "__main__":
    print("🎲 Welcome to the Dice Game!")
    play_game()
