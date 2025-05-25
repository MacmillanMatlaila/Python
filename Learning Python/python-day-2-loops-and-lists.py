students = ["Thato", "Pretty", "Tshepo"]

'''
print(students[0])
print(students[1])
print(students[2])
'''

'''
for student in students:
    print(student)
'''

'''
for i in range(len(students)):
    print(i + 1, students[i])
'''

'''
students = ["Tshepo", "Thato", "Pretty", "Evidence"]
houses = ["Mont Acres", "Mont Acres", "Moletlane"]
'''

#OR
'''
students = {
    "Tshepo": "Mont Acres",
    "Thato" : "Mont Acres",
    "Pretty": "Mont Acres",
    "Evidence": "Moletlane",
}

print(students["Tshepo"]) # Prints out address 
'''

#OR
'''
students = {
    "Tshepo": "Mont Acres",
    "Thato" : "Mont Acres",
    "Pretty": "Mont Acres",
    "Evidence": "Moletlane",
}

for student in students:
    print(student) #This will only print out the names which are keys for the location
'''

#OR

population = {
    "Tshepo": "Mont Acres",
    "Thato" : "Mont Acres",
    "Pretty": "Mont Acres",
    "Evidence": "Moletlane",
}

for person in population:
    print(person, population[person]) #This prints out everything

#
  
