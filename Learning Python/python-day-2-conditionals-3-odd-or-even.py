def main():
    x = int(input("What is x?"))
    #if x % 2 == 0:
    if is_even(x):
        print("Even")
    else:
        print("Odd")
            
            
#Keep in mind you created a function instead of just writing a conditional as such you must now define it:
def is_even(n):
    #You can just say return n % 2 == 0
    return True if n % 2 == 0 else False
#Above can be done on one line or separately

main()