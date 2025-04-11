import random

def choose_word():
    try:
        with open("words.txt", "r") as file:
            words = [line.strip() for line in file if line.strip()]
        return random.choice(words)
    except FileNotFoundError:
        print("Error: 'words.txt' file not found. Please make sure the file exists.")
        exit()

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Welcome to the Hangman Game!")
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            print("Wrong guess!")
            attempts -= 1

    if attempts == 0:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()