import random

# Predefined list of 5 words
word_list = ["apple", "chair", "piano", "tiger", "snake"]

# Choose a random word from the list
secret_word = random.choice(word_list)

# To keep track of guessed letters and incorrect tries
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Create a display version of the word using underscores
display_word = ["_" for _ in secret_word]

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Main game loop
while incorrect_guesses < max_attempts and "_" in display_word:
    print("Word:", " ".join(display_word))
    print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        # Reveal the guessed letter in display_word
        for index, letter in enumerate(secret_word):
            if letter == guess:
                display_word[index] = guess
        print("Good guess!\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess!\n")

# Game result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Sorry, you've been hanged. The word was:", secret_word)
