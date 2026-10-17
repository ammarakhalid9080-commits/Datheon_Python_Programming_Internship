
import random

words = ["python", "java", "computer"]
secret_word = random.choice(words)

guessed_letters = set()
remaining_attempts = 6

while remaining_attempts > 0:

    # Display the hidden word
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()

    # Check if the word is complete
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter one letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct!")
    else:
        remaining_attempts -= 1
        print("Wrong! Attempts left:", remaining_attempts)

if not all(letter in guessed_letters for letter in secret_word):
    print("Game over! The word was:", secret_word)


