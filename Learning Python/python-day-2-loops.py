#A way to help you understand loops:
'''
-To help with understanding loops picture you have 3 fingers up
-Each time you say hello , one finger goes down
-Each time a finger goes down you ask are there any fingers still up
-If there are fingers still up you continue saying hello until there are no fingers up
'''

#The basic:

'''
print("meow" * 3)

#print("meow\n" * 3) #\n new line

#print("meow\n" * 3, end = "") #overwrites the ending being \n to what you want 
'''

#Initial loop
'''
i = 3 #Sets the number of times to loop like above where you had 3 fingers up
while i != 0: #while i does not equal 0, that finger question..REMEMBER!!! 
   print("boomshakalaka") #What to loop
   i = i - 1 #Remeber i = 3, therefore code should loop 3 times. to avoid an infinite loop you decrement(i-1) each time its called therefore it loops once(i = 3-1) then asks if it loop again (i = 2-1) and again(i = 1-1) until it hits 0
   #This is basically putting a finger down after each loop
'''

#ALTERNATIVELY:
'''
i = 1
while i <= 3: #So wile there are still less/equal fingers up than 3
    print("boom boom pow")
    i = i + 1 #Therefore instead of decrementing you increment
'''

#ALTERNATIVELY set the range but write it out:
'''
for i in [0,1,2]: #functionaly the same as i = 3 0r i < = 3
    print("Tshepo bothata keng")
'''

#BUT WHAT IF IT'S A MILLION TIMES, THE EXTREME CASE:
#Use the range function
'''
for i in range (3): #sets range to 3 times instead of typing out each number within the range 0,1,2 which are the ranges to 3
    print("Johnny ooo johnny ooo")
'''

'''
while True:
    n = int(input("What's n?"))
    if n < 0:
        continue
    else:
        break
'''

'''
while True:
    n = int(input("What's n?"))
    if n > 0: #Greater than 0 sets an infinite loop
        break #Forgtting to break will give a syntax error response
    
for _ in range(n):
        print("rambakchuas lol")
'''

'''
def main():
    palmer(3)
    
def palmer(n):
    for _ in range(n):
        print("palmer")
        
main()
'''

def main():
    number = get_number()
    palmer(number)
    
def get_number(): #Remember to define funtions you have created
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
    
def palmer(n):
    for _ in range(n):
        print("palmer")
        
main()




    
    

    
    