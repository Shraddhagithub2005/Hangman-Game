import random

def hangman():
    words = ["python", "interface", "designer", "application", "sketching", "digital", "mongo"]
    word_to_guess = random.choice(words).lower()
    guessed_word = ["_" for _ in word_to_guess]
    guessed_letters = set()
    max_attempts = 7
    attempts_left = max_attempts

    print("Welcome to Hangman!")
    print("Try to guess the word letter by letter.")
    print("You have", max_attempts, "incorrect guesses allowed.")

    while attempts_left > 0 and "_" in guessed_word:
        print("\nWord to guess:", " ".join(guessed_word))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print(f"Attempts left: {attempts_left}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good guess!")
            for idx, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[idx] = guess
        else:
            print("Wrong guess.")
            attempts_left -= 1

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word_to_guess)
    else:
        print("\nGame over! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
