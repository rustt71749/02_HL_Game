# Higher Lower
# Program should work but will need to be usability tested
import random

# Number checking function:
def int_check(question, low=None, high=None):

    # error messages
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} " \
                "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or " \
                "equal to {}".format(high)

    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))

            # Checks response is not low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                    print(error)
                    continue

            return response

        except ValueError:
            print(error)
            continue

# Main routine

lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)
guess = int_check("Guess: ", lowest, highest)

# Generate secret number between low and high
LOW = lowest
HIGH = highest

for item in range(LOW, HIGH):
    secret = random.randint(LOW, HIGH)

# Compare users guess with secret number
SECRET = secret
GUESSES_ALLOWED = guess

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

# Start game
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))   # replace this with function call later

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("You have already guessed that number. Please try again. "
              "You still have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guess > SECRET:
        print("Too high, try a lower number. Guesses left: {}".format(guesses_left))
    elif guess < SECRET:
        print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

if guess == SECRET:
    if guesses_left == GUESSES_ALLOWED - 1:
        print("Good job! You got the secret number in one guess :)")
    else:
        print("Congratulations, you got it in {} guesses".format(len(already_guessed)))
    num_won += 1
else:
    print("Sorry, you lost this round because you have run out of guesses :(")
