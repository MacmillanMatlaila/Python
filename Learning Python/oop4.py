class Student:
    def __init__(self, name, house, course):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Mont Acres", "Lotus Gardens", "Roodeplaat", "Zebediela"]:
            raise ValueError["Invalid house"]
        self.name = name
        self.house = house
        self.course = course
        
    def __str__(self):
        '''
        return "a student"
        '''
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.course:
            case "computer science":
                return "pc"
            case "humanities":
                return "hr"
            case "environmental sciences":
                return "soil"
            case "geopolitics":
                return "geo"
        
        
def main():
    student = get_student()
    print(student)
    print(student.charm)
    
    
def get_student():
    name = input("name:") 
    house = input("house:")
    course = input("course:")
    return Student(name, house, clan)

if __name__ == "__main__":
    main()
    