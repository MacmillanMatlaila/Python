name = input("Type your name:")
print("Welcome", name, "to this adventure")

answer = input(
                "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?"
                ).lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross. Type walk to walk around or swim to swim across: ").lower()
    
    if answer == "swim":
        print("You swam aross and were eaten by an alligator.")
    
    elif answer == "walk":
        print("You walked for any kilometers, ran out of water and you lost the game.")
    
    else:
        print("Not a valid choice. You Lose!")
    

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly do you want to cross it or head back (cross/back)" ).lower()
    
    if answer == "back":
        print("You go back to the road. you lose!")
    
    elif answer == "cross":
        print("You cross the bridge and meet a stranger. Do you talk to them(Yes/No)?")
        
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You Win!")
            
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose")
            
        else:
            print("Not a valid choice. You Lose!")
    
    
else:
    print("Not a valid choice. You Lose!")
    
print("thank you for trying", name,"!")