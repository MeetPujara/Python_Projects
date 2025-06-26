name_input = input("Enter Your Name: ").strip()
print(f"\nWelcome {name_input} to This Adventure!")

while True:
    print("\nYou are on a dirt road. It has come to an end and you can go left or right.")
    answer = input("Which way would you like to go? (left/right): ").strip().lower()

    if answer == "left":
        answer = input(
            "You come to a river. Do you want to walk around or swim across? (walk/swim): "
        ).strip().lower()

        if answer == "swim":
            print("You swam across and were eaten by an alligator.")
            user_lost = input("You lost. Want to try again? (Y/N): ").strip().lower()
            if user_lost == 'y':
                continue
            else:
                print("Game Over. Thanks for playing!")
                break

        elif answer == "walk":
            print("You walked for miles, ran out of water, and lost the game.")

        else:
            print("Not a valid option. You lose.")

    elif answer == "right":
        answer = input(
            "You come to a wobbly bridge. Do you want to cross it or go back? (cross/back): "
        ).strip().lower()

        if answer == "back":
            print("You go back and lose.")
        elif answer == "cross":
            answer = input(
                "You cross the bridge and meet a stranger. Do you talk to them? (yes/no): "
            ).strip().lower()

            if answer == "yes":
                print("The stranger gives you gold. You WIN!")
            elif answer == "no":
                print("You ignore the stranger. They get offended and you lose.")
            else:
                print("Not a valid option. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

    print(f"\nThank you for trying, {name_input}!")
    play_again = input("Do you want to play again? (Y/N): ").strip().lower()
    if play_again != 'y':
        print("Goodbye!")
        break
