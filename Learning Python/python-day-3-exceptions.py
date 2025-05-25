'''
try:
    x = int(input("What's x?"))
    
except ValueError:
    print("x is not an integer")#Tells python what to do in exceptional cases where user doesn't key in an integer

else :
    print(f"x is {x}") #Using else deals with errors
'''

#You can loop until user gives correct data type
'''
while True:
    try:
        x = int(input("What's x?"))
        
    except ValueError:
        print("x is not an integer")

    else :
        break
        
print(f"x is {x}")

'''

'''
def main():
    x = get_int()
    print(f"x is {x}")
    
def get_int():
    while True:
        try:
            x = int(input("What's x?"))
            
        except ValueError:
            print("x is not an integer")

        else :
            return(x)

main()
'''

#Using pass instead of an error message incase of wrong data type inputed

'''
def main():
    x = get_int()
    print(f"x is {x}")
    
def get_int():
    while True:
        try:
            x = int(input("What's x?"))
            
        except ValueError:
            pass #Instead of an error message python has pass

        else :
            return(x)
main()
'''

#Alternatively:

'''
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
    
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            
        except ValueError:
            pass 

main()

'''