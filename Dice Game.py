import random

while True:
    choice = input("Roll the dice: (y/n) ")
    if choice.upper() == "Y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')

    elif choice.upper() == "N":
        print("Thanks for playing!")
        break
    else:
        print("Invalid Choice")