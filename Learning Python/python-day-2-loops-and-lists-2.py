population = [
    {"name" : "Tshepo", "house" : "Mont Acres", "race" : "Black"},
    {"name" : "Thato", "house" : "Mont Acres", "race" : "Black"},
    {"name" : "Pretty", "house" : "Mont Acres", "race" : "Black"},
    {"name" : "Evidence", "house" : "Mont Acres", "race" : "White"},
]

'''
for person in population:
    print(person["name"])
    #Prints out only the name
'''

for person in population:
    print(person["name"], person["house"], person["race"], sep = ",")
    #Prints out both the name and address and race and adds a separator