#Ask user for their name
name = input("What's your name?")

name = name.strip()
#Removes whitespace from string

name = name.capitalize()
#Capitalize user's name

name = name.title()
#Capitalises first letter of each word

name = name.strip().title()
#Removes whitespace from string
#Capitalises first letter of each word

first, last = name.split(" ")
#Split user's name into first name and last name


name = input("What's your name?").strip().title()
#You can add thecode to initial line instead of separating the code


#Say hello to user
print(f"Hello, {name}")
#The f before the quotations fornmats within the string meaning name is now the variable and not just a part of the string within the quotations





