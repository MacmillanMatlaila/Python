#creating a calculator



#x = input("What's x?")#
#You can nest int(input("What's x?"))
#You can also nest as floats ---float(input("What's x?"))
#y = input("What's y?")#
#You can nest also nest as floats ---floats(input("What's y?"))
#x = float(input("What's x?"))
#z = int(x) + int(y)#
#You can also parse as floats z = float(x) + float(y)
#If nested then z = x + y will return answer to calculation instead of concatenating the string
#To round off we can say z = round(x + y)

#print(z)#
#If nested you could even just say print(x+y)
#to turn z into an f string , to format it - print(f"(z:.2f}"}



def main():
        x = int(input("What's x?"))
        print("x squared is", square(x))

#square has to be defined
def square(n):
    return n * n #n**2 or pow(n,2) can also be used to raise an number to the power 
#Don't forget to call the "main" function at the end or else it won't run
main()

