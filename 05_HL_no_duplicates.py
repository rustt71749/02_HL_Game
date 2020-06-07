# HL Decomposition Step 5
# Make sure user if user guesses a duplicate number that it is not counted
# Print already guessed message

# Prevents duplicate guesses

SECRET = 9
GUESSES_ALLOWED = 4

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

# Start game
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))   # replace this with function call in final game

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("You have already guessed that number. Please try again. "
              "You still have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    # if user has guesses left
    if guesses_left > 1:
        if guess > SECRET:
                print("Too high, try a lower number. Guesses left: {}".format(guesses_left))

        elif guess < SECRET:
                print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

    # if user has one guess left
    elif guesses_left == 1:
        if guess > SECRET:
            print("Too high, try a lower number. THIS IS YOUR FINAL GUESS!")

        elif guess < SECRET:
            print("Too high, try a lower number. THIS IS YOUR FINAL GUESS!")

if guess == SECRET:
    if guesses_left == GUESSES_ALLOWED - 1:
        print("Good job! You got the secret number in one guess :)")
    else:
        print("Congratulations, you got it in {} guesses".format(len(already_guessed)))
    num_won += 1
else:
    print("Sorry, you lost this round because you have run out of guesses :(")
