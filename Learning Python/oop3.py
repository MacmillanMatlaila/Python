class Student:
    def __init__(self, name, house):
        if not name:
            '''
            print("Missing name")#simply prints out missing name
            sys.exit("Missing name")#exits program and prints out Missing name as reason, don't forget to import sys at the top if you use this .
            '''
            raise ValueError("Missing name") #better way to handle exceptions in this case
        if house not in ["Mont Acres", "Lotus Gardens", "Roodeplaat", "Zebediela"]:#Specifies/limits acceptable input 
            raise ValueError["Invalid house"]
        self.name = name
        self.house = house
    
def main():
        student = get_student()
        print(f"{student.name} from {student.house}")

def get_student():
    name = input("name:") 
    house = input("house:")
    student = Student(name, house)
    return student
    
if __name__ == "__main__":
            main()
    