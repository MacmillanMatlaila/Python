import csv

'''
name = input("name?")
print(f"hello, {name}")
'''

#Alternatively

'''
names = []
'''

'''
for _ in range(3):
     name = input("name?")
     names.append(name)
print(f"hello, {name}")
'''

#Alternatively

'''
for _ in range(3):
     names.append(input("name?"))

for name in sorted(names):
    print(f"hello, {name}")
'''

#What if it's a large progra with many names

'''
name = input("Name:")

#Instead of just printing out the input lets store it to a file:

file = open("names.txt", "w") #cretes text file
file.write(name) #write the name
file.close()#close the file
'''

#To save multiple inputs to a file

name = input("Name:")

'''
file = open("names2.txt", "a") #cretes text file
file.write(name) #write the name
file.close()#close the file
'''

#To save names in one file on new line each

'''
file = open("names2.txt", "a") 
file.write(f"{name}\n")
file.close()
'''

#Alternative way to file.(close)

'''
with open("names2.txt", "a") as file: 
    file.write(f"{name}\n")

'''
#########
'''
with open("names3.txt", "r") as file:
    lines = file.readLines()

for line in lines:
    print("hello,", line.rstrip())
'''

'''
with open("names3.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
'''

'''
names = []

with open("names4.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

'''

#Storing names and addresses: names.txt becomes names.csv

'''
with open("names.csv") as file:
    for line in file:
        line.rstrip().split(",") #columns and rows
        print(f"{row(0)} is in {row(1)}")

'''

#Alternatively:

'''
with open("names.csv") as file:
    for line in file:
    name, house = line.rstrip().split(",") #columns and rows
        print(f"{name(0)} is in {house(1)}") # renamed to name and column

'''

#Sort per name in csv:

names = []

'''
with open(names2.csv) as file:
    for line infile:
        name, house = line.rstrip().split()
        names.append(f"{name} is in {house}")

for name in sorted(names):
    print(name)
'''

#Remember Python supports dictioneries which are a way to associate keys

'''
with open(names2.csv) as file:
    for line infile:
        name, house = line.rstrip().split(",")
        name = {} #empty curly braces creates empty dictionary
        name["name"] = name
        name["house"] = house
        students.append(name)

    for name in names:
        print(f"name['name'] is in {name['house']}")

''''

#Alternatively: sorting a dictionary with 2 keys names and house

'''
with open(names2.csv) as file:
    for line in file:
        name, house = line.rstrip().split(",")
        name = {"name" = name, "house" = house
        students.append(name)

def get_name(name): #A function gets the name
    return name["name"]

for name in sorted(names, key = get_name):
        print(f"name['name'] is in {name['house']}")

#or      
                   
for name in sorted(names, key = lambda name: name["name"]):
        print(f"name['name'] is in {name['house']}")

'''

#many values , more than 2 in csv file we import csv at top.

'''
with open(names2.csv) as file:
    reader = csv.reader(file)
    for row inrader:
        names.append({"name": row[], "home": row[1]})
    

def get_name(name): #A function gets the name
    return name["name"]

for name in sorted(names, key = get_name):
        print(f"name['name'] is in {name['house']}")
'''
        
#Taking input to write:

'''
name = inpout("name?")
house = input("house?")

with open("names.csv", "a"):
    writer = csv.writer(file)
    writer.writerow([name, home])
'''

