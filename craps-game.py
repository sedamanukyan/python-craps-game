import random


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    return dice1, dice2, dice_sum


def play_craps():
    instant_wins = [7, 11]
    instant_losses = [2, 3, 12]

    print("\n=== New Game of Craps ===")
    input("Press Enter to roll the dice...")

    # First Roll
    dice1, dice2, first_sum = roll_dice()
    print(f"First Roll: You rolled {dice1} and {dice2}. Total sum = {first_sum}")

    # Check outcomes
    if first_sum in instant_wins:
        print("Congratulations! You rolled 7 or 11 on the first try. YOU WIN!")
        return
    elif first_sum in instant_losses:
        print("Craps! You rolled 2, 3, or 12 on the first try. THE CASINO WINS!")
        return
    else:
        # Set Goal and Loop
        goal = first_sum
        print(f"Your goal number is now: {goal}")
        print("Keep rolling! You win if you hit your goal again, but lose if you roll a 7.")

        game_over = False

        while not game_over:
            input("\nPress Enter to roll again...")
            dice1, dice2, current_sum = roll_dice()
            print(f"You rolled {dice1} and {dice2}. Total sum = {current_sum}")

            if current_sum == goal:
                print(f"Awesome! You hit your goal number ({goal})! YOU WIN!")
                game_over = True
            elif current_sum == 7:
                print("Oh no! You rolled a 7 before reaching your goal. THE CASINO WINS!")
                game_over = True
            else:
                print(f"No match yet. Goal is still {goal}. Roll again!")


# Main function
def main():
    keep_playing = True

    while keep_playing:
        play_craps()

        # Asking user if they want to play again
        user_choice = input("\nDo you wanna play again? (yes/no): ").strip().lower()

        if not user_choice.startswith('y'):
            keep_playing = False
            print("Thanks for playing! Goodbye!")


main()
