# HL Decomposition Step 4

# To do
# Set up number of guesses
# Keep track of number of guesses
# if user runs out of guesses, print a losing message
# if user guesses secret number within number of guesses, print winning message

SECRET = 9
GUESSES_ALLOWED = 4

# initialise variables
guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

# Start game
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))   # replace with function call later
    guesses_left -= 1

    # If user has guesses left
    if guesses_left >= 1:
        if guess > SECRET:
                print("Too high, try a lower number. Guesses left: {}".format(guesses_left))

        elif guess < SECRET:
                print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

    # if user is out of guesses
    else:
        if guess > SECRET:
            print("Too high")
        elif guess < SECRET:
            print("Too low")

if guess == SECRET:
    if guesses_left == GUESSES_ALLOWED - 1:
        print("Good job! You got the secret number in one guess :)")
    else:
        print("Well done, you guessed the secret number")
    num_won += 1
