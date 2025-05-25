import random

top_range = input("Type in a number: ")
#isdigit() ensures input is a digit/number
if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please type in a number greater than zero")
        quit()

else:
    print("Please type a number")
    quit()

guesses = 0
     
#randrange(start, stop)
random_num = random.randint(0, top_range)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    #isdigit() ensures input is a digit/number
    if user_guess.isdigit():
        user_guess = int(user_guess)


    else:
        print("Please type a number")
        continue#this takes us back to the top of the loop

    if user_guess == random_num:
        print("You got it right the random number is: ",random_num)
        break
    else:
        print("You got it wrong...Try again")

print("You got it in", guesses, "guesses")
