import re

email = input("Email:").strip().lower()

'''
if "@" in email and "." in email: #Looks for @sign and dot in inputed email
    print("Valid")
else:
    print("Invalid")
'''

#When you know the input you are expecting

'''
username, domain = email.split()

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")
'''

#To be more specific with how email should end

'''
username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
'''

#Regular expressions are patterns you can define for a purpose

#We start with a very simple regular expression
'''
if re.search("@", email):
    print("valid")
else:
    print("invalid")
'''

#RE.SEARCH can take in more symbols

'''
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    #^ matches at start
    #$ matches at end
    #first [^@] any character except an @ sign
    #second [^@] also means any character except an @ sign
    #There is an official standard for how an email can be written(characters)
    #similarly first[a-zA-Z0-9_] specifies which characters and numeric values you want to allow at start
    #similarly first[a-zA-Z0-9_] specifies which characters and numeric values you want to allow at end
    #But \w at start and end represents a word character
    #(com|net|org|co.za) specifies which domains to allow 
    #re.search can pass in flags: re.IGNORECASE,re.MULTILINE,re.DOTALL
    #re.search(r"^\w+@+(\w+\.)?\w+\.edu$", email):
    #You can use libraries to validate emails
    print("valid")
else:
    print("invalid")
'''
