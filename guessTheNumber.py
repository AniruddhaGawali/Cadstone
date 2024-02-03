import random 
import math

# Taking inputs from the user
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# generating random number between the lower and upper
x = random.randint(lower, upper)

print("\n\t You've only",round(math.log(upper - lower + 1,2)),"chances to guess the integer!\n")

count = 0

while count < math.log(upper - lower +1,2):
    count += 1

    # Taking guessing number as input
    guess = int(input("Guess a number: "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in", count, "try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

# If Guessing is more than required guesses, shows this output.
        if( count >= math.log(upper-lower+1,2)):
            print("\nThe number is %d"%x)
            print("\tBetter Luck Next time!")
