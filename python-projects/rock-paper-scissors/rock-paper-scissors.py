import random

options = ["rock", "paper", "scissors"]

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Choose Rock,Paper or scissor or q to Quit:").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_num = random.randint(0, 2)
    #rock: 0, paper: 1, scissors:2
    computer_choice = options[random_num]
    print("Computer chose", computer_choice + ".")

    if user_input == "rock" and computer_choice == "scissors":
        print("You win!")
        user_wins += 1
        continue

    if user_input == "paper" and computer_choice == "rock":
        print("You win!")
        user_wins += 1
        continue

    if user_input == "scissors" and computer_choice == "paper":
        print("You win!")
        user_wins += 1
        continue

    else:
        print("You lose")
        computer_wins +=1
        
print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print("Goodbye")
