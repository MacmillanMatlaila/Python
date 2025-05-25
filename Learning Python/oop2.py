#Creating datatytpes and giving them names, classes:
#Everytime you use classes you create objects from classes
class Student:
    ## dotted lines are just an allowed placeholder in python
    '''
    ...
    '''
    #init is the initialisation method
    def __init__(self, name, house): #The parameters are self, name, house. self gives you access to the current object which was created
        self.name = name
        self.house = house
    
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    '''
    student = Student()
    student.name = input("name:") #A created object from Student class
    student.house = input("house:") #A created object from Student class
    return student
    '''
    
    
    name = input("name:") 
    house = input("house:")
    student = Student(name, house)
    return student
    
if __name__ == "__main__":
    main()
    