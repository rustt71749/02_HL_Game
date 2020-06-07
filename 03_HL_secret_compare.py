# HL Decomposition Step 3
# compare user guess with the secret number

SECRET = 9

guess = ""

while guess != SECRET:

    guess = int(input("Guess: "))   # replace with call function in final game

    if guess > SECRET:
        print("Too high, try a lower number")
    elif guess < SECRET:
        print("Too low, try a higher number")
    else:
        print("Congratulations! You guessed the secret number")
