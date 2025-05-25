import re 

email = input("Email").strip()

if re.search(r"`[`@]+@[`@]+\.edu$", email): #use square brackets and put a charater to specifically search for
    print("Valid")
else:
    print("Invalid")