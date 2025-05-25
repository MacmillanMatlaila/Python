name = input("What's your name? ")

'''if name == "Tshepo":
    print("Mont Acres")
elif name == "Thato":
    print("Mont Acres")
elif name == "Pretty":
    print("Mont Acres")
elif name == "Evidence":
    print("Moletlane")
else:
    print("I don't know")
'''


'''
name = name.strip().title()
match name:
    case "Tshepo":
        print("Mont Acres")
    case "Thato":
        print("Mont Acres")
    case "Pretty":
        print("Mont Acres")
    case "Evidence":
        print("Moletlane")
    #The syntax for the else function in python:    
    case _:
        print("Address not in register")
'''

#You can condense the code
name = name.strip().title()
match name:
    case "Tshepo" | "Thato" | "Pretty":
        print("Mont Acres")
    case "Evidence":
        print("Moletlane")
    #The syntax for the else function in python:    
    case _:
        print("Address not in register")

