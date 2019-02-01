import random
word_bank = ["bank", "teller", "jukebox", "yeah", "don't", "yes", "ban", "okay", "minecraft", "roblox"]

word = random.choice(word_bank)
guesses_left = 8
guessed_letters = ["'", ]

while guesses_left > 0:
    # Show the hidden word
    word_hidden = []
    for letter in word:
        if letter in guessed_letters:
            word_hidden.append(letter)
        else:
            word_hidden.append("*")
    print(word_hidden)

    # Take in a guess
    user_guess = input("Guess a letter")
    guessed_letters.append(user_guess)
    guesses_left -= 1
