import sys

'''
print("Hello, my name is", sys.argv[1])
'''
#With an error message:

'''
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
'''

#With conditionals:

'''
if len(sys.argv) < 2:
    print("Too few arguments")
    
elif len(sys.argv) > 2:
    print("Too many arguments")

else:
    print("Hello, my name is", sys.argv[1])
'''

#Alternatively:

'''
#check for errors on top
if len(sys.argv) < 2:
    print("Too few arguments")
    
elif len(sys.argv) > 2:
    print("Too many arguments")

#Print name tags
print("Hello, my name is", sys.argv[1])

'''

#sys.exit exits the program earlier than we may have otherwise given wrong input

'''
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
    
elif len(sys.argv) > 2:
    print("Too many arguments")

else:
    print("Hello, my name is", sys.argv[1])
    
'''

'''
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is", arg)

'''


if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)


