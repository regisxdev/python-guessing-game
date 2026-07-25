import random

def play():
    print("====================================")
    print("Welcome to the Guessing Game!")
    print("====================================")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess what it is!\n")

    # The computer chooses a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Asks the player to type a number
            guess_str = input("What is your guess? ")
            guess = int(guess_str)
            attempts += 1

            # Checks the game conditions
            if guess < 1 or guess > 100:
                print("Please, choose a number between 1 and 100 only!\n")
                continue

            if guess < secret_number:
                print("Too low! Try a higher number.\n")
            elif guess > secret_number:
                print("Too high! Try a lower number.\n")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break # Ends the loop and the game when the player guesses correctly

        except ValueError:
            # Handles the error if the user types letters or symbols instead of numbers
            print("Invalid input! Please type an integer number.\n")

    print("Game over. Thanks for playing!")

# Starts the game
if __name__ == "__main__":
    play()
