import random


number = random.randint(1, 100)
while True:
    guess = input("Guess the number between 1 and 100: ")
    if guess.isdigit():
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the number!", number)
            break
        elif guess > number:
            print("Too high try again")
        elif guess < number:
            print("Too low try again")
    else:
        print("Please enter a valid number")