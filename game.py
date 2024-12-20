import random  # For selecting a random word from the list
import os  # For clearing the screen
from colorama import Fore, Style  # For colored text in the terminal

def display_word(word, guessed_letters):
    # Create a string representing the current state of the guessed word.
    # Letters that have been guessed are displayed; others are shown as underscores.
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    # List of words to choose from
    words = ["python", "programming", "hangman", "challenge", "object", "function"]
    word_to_guess = random.choice(words)  # Randomly select a word from the list
    guessed_letters = set()  # Keep track of guessed letters
    attempts_remaining = 6  # Player starts with 6 attempts

    # Clear the screen and display the game title
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "Welcome to Hangman!" + Style.RESET_ALL)
    print("Try to guess the word, one letter at a time.")

    # Main game loop
    while attempts_remaining > 0:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen at the start of each turn
        
        # Display the current state of the word and other game info
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        print(f"Attempts remaining: {Fore.YELLOW}{attempts_remaining}{Style.RESET_ALL}")
        print("Guessed letters:", Fore.GREEN + ' '.join(sorted(guessed_letters)) + Style.RESET_ALL)

        # Prompt the player to guess a letter
        guess = input("Enter a letter: ").lower()

        # Check if the input is valid (a single alphabetical character)
        if len(guess) != 1 or not guess.isalpha():
            print(Fore.RED + "Please enter a single valid letter." + Style.RESET_ALL)
            input("Press Enter to continue...")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(Fore.RED + "You've already guessed that letter." + Style.RESET_ALL)
            input("Press Enter to continue...")
            continue

        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print(Fore.GREEN + f"Good job! '{guess}' is in the word." + Style.RESET_ALL)
            # Check if the player has guessed all the letters in the word
            if all(letter in guessed_letters for letter in word_to_guess):
                print(Fore.CYAN + "\nCongratulations! You guessed the word:" + Style.RESET_ALL, word_to_guess)
                input("Press Enter to return to the menu...")
                return  # Exit the game loop
        else:
            print(Fore.RED + f"Sorry, '{guess}' is not in the word." + Style.RESET_ALL)
            attempts_remaining -= 1  # Decrement attempts remaining

        input("Press Enter to continue...")

    # If the player runs out of attempts, reveal the word
    print(Fore.RED + "\nGame over! The word was:" + Style.RESET_ALL, word_to_guess)
    input("Press Enter to return to the menu...")

def show_menu():
    # Main menu loop
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        
        # Display the menu options
        print(Fore.MAGENTA + "\n--- Hangman Game Menu ---" + Style.RESET_ALL)
        print("1. Play Hangman")
        print("2. Exit")

        # Get the player's menu choice
        choice = input("Enter your choice: ")
        if choice == '1':
            hangman()  # Start a new game
        elif choice == '2':
            print(Fore.CYAN + "Thank you for playing! Goodbye!" + Style.RESET_ALL)
            break  # Exit the menu loop
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
            input("Press Enter to continue...")

# Start the program by displaying the menu
if __name__ == "__main__":
    show_menu()
