import random
from colorama import Fore, Style

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    words = ["python", "programming", "hangman", "challenge", "object", "function"]
    word_to_guess = random.choice(words)
    guessed_letters = set()
    attempts_remaining = 6

    print(Fore.CYAN + "Welcome to Hangman!" + Style.RESET_ALL)
    print("Try to guess the word, one letter at a time.")

    while attempts_remaining > 0:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        print(f"Attempts remaining: {Fore.YELLOW}{attempts_remaining}{Style.RESET_ALL}")
        print("Guessed letters:", Fore.GREEN + ' '.join(sorted(guessed_letters)) + Style.RESET_ALL)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(Fore.RED + "Please enter a single valid letter." + Style.RESET_ALL)
            continue

        if guess in guessed_letters:
            print(Fore.RED + "You've already guessed that letter." + Style.RESET_ALL)
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(Fore.GREEN + f"Good job! '{guess}' is in the word." + Style.RESET_ALL)
            if all(letter in guessed_letters for letter in word_to_guess):
                print(Fore.CYAN + "\nCongratulations! You guessed the word:" + Style.RESET_ALL, word_to_guess)
                return
        else:
            print(Fore.RED + f"Sorry, '{guess}' is not in the word." + Style.RESET_ALL)
            attempts_remaining -= 1

    print(Fore.RED + "\nGame over! The word was:" + Style.RESET_ALL, word_to_guess)

def show_menu():
    while True:
        print(Fore.MAGENTA + "\n--- Hangman Game Menu ---" + Style.RESET_ALL)
        print("1. Play Hangman")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            hangman()
        elif choice == '2':
            print(Fore.CYAN + "Thank you for playing! Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    show_menu()
