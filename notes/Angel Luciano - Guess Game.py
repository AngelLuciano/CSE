import random

guessesTaken = 0

playing = True

number = random.randint(1, 10)

while guessesTaken < 5:
    print("Guess the number")
    guess = input()
    guess = int(guess)

    guessesTaken += 1

    if guess < number:
        print("Your number guess is low")

    if guess > number:
        print("Your number is high.")

    if guess == number:
        print("Good job you guessed the right number")
        playing = False
