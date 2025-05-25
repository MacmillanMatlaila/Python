import rc


email = input("Email:").strip()

'''
if "@" in email:
    print("Valid")
else:
    print("Invalid")
'''

'''
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
'''

'''
username, domain = email.split("@"):
if usernam and "." in domain:
    print("Valid")
else:
    print("Invalid")
'''

#Setting a ".com" limitation
'''
username, domain.endswith(".com"):
if username and "." in domain:
    print("Valid")
else:
    print("Invalid")

'''

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")



