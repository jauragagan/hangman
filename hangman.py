import random

# List of words to choose from
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grapefruit", "honeydew"]

# ASCII art images for hangman stages
hangman_images = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

def choose_word():
    # Choose a random word from the list
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with guessed letters filled in
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts = len(hangman_images) - 1

    while attempts > 0:
        print(hangman_images[len(hangman_images) - attempts - 1])
        print(display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            if display_word(word, guessed_letters) == word:
                print("Congratulations, you won!")
                break
        else:
            print("Wrong guess!")
            attempts -= 1

    if attempts == 0:
        print(hangman_images[len(hangman_images) - attempts - 1])
        print(f"Sorry, you lost! The word was '{word}'.")

play_hangman()
