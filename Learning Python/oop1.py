def main():

    '''
    name = input("Name:").strip()
    house = input("House:")
    print("{name} from {house}")
    '''

    '''
    name = get_name()
    house = get_house()
    print("{name} from {house}")
    '''
    
    '''
    name, house = get_student()
    print(f"{name} from {house}")
    '''
    
    #Using a Tuple when inputed data should not change:
    student = get_student()
    
    '''
    if student[0] == "Macmillan":
        student[1] = "Mont Acres 27"
    print(f"{student[0]} from {student[1]}")
    '''
    if student["name"] == "Macmillan":
        student["house"] = "Mont Acres 27"
    print(f"{student['name']} from {student['house']}")


'''
def get_name():
    name=input("Name:").strip()
    return name

def get_house():
    house =input("House:").strip()
    return house
'''

def get_student():
    '''
    name=input("Name:").strip()
    house =input("House:").strip()
    return [name, house]
    '''
'''   
#using a ditionary:
    student = {}
    student["name"] = input("name:")
    student["house"] = input("house:")
    return student
'''

    #Tightening the code:
    name = input("Name:")
    house = input("House")
    return{"name": name, "house": house}

if __name__== "__main__":
    main()
    
    