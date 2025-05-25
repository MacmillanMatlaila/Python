import re
#Reformatting inputed data into the desired format

name = input("Name:").strip()
'''
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"Hello, {name}")
'''

'''
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")
'''

'''
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.groups(1)
    first = matches.groups(2)
    name = f"{first} {last}"
print(f"hello, {name}")
'''

#Further tightening of code:

'''
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
'''