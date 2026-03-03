import random


class NumberGuessingGame:
    def __init__(self):
        # Tuple for difficulty levels (immutable data structure)
        self.difficulty_levels = (
            ("Easy", 10, 5),      # (Level Name, Max Number, Attempts)
            ("Medium", 50, 7),
            ("Hard", 100, 10)
        )

        # Dictionary to store score
        self.score = {
            "wins": 0,
            "losses": 0
        }

        # List to store game history
        self.game_history = []

    def select_difficulty(self):
        print("\nSelect Difficulty Level:")
        for index, level in enumerate(self.difficulty_levels, start=1):
            print(f"{index}. {level[0]} (1 to {level[1]}, Attempts: {level[2]})")

        while True:
            try:
                choice = int(input("Enter choice (1-3): "))
                if 1 <= choice <= len(self.difficulty_levels):
                    return self.difficulty_levels[choice - 1]
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")

    def play_game(self):
        level_name, max_number, attempts = self.select_difficulty()
        secret_number = random.randint(1, max_number)

        print(f"\nYou selected {level_name} level!")
        print(f"I have selected a number between 1 and {max_number}.")
        print(f"You have {attempts} attempts.\n")

        for attempt in range(1, attempts + 1):
            try:
                guess = int(input(f"Attempt {attempt}: Enter your guess: "))

                # print(f"Your Guess: {guess}")
                # print(f"System Number: {secret_number}")

                if guess == secret_number:
                    print("🎉 Congratulations! You guessed it correctly!")
                    self.score["wins"] += 1
                    self.game_history.append((level_name, "Win"))
                    return
                elif guess < secret_number:
                    print("Too Low!")
                else:
                    print("Too High!")

            except ValueError:
                print("Invalid input! Please enter a number.")

        print(f"\n😢 You lost! The correct number was {secret_number}.")
        self.score["losses"] += 1
        self.game_history.append((level_name, "Loss"))

    def show_score(self):
        print("\n📊 Score Board")
        print(f"Wins: {self.score['wins']}")
        print(f"Losses: {self.score['losses']}")

        print("\nGame History:")
        for game in self.game_history:
            print(f"Level: {game[0]} - Result: {game[1]}")

    def play_again(self):
        while True:
            choice = input("\nDo you want to play again? (y/n): ").lower()
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            else:
                print("Invalid input! Enter 'y' or 'n'.")


# Main Program
if __name__ == "__main__":
    game = NumberGuessingGame()

    print("🎯 Welcome to the Number Guessing Game!")

    while True:
        game.play_game()
        game.show_score()

        if not game.play_again():
            print("\nThanks for playing! Goodbye 👋")
            break