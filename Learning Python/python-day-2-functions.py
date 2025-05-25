#You can set a default or preassigned value to the argument "to" such as to : "world"
def hello(to):
    print("hello,", to)

name = input("What's your name?")
name = name.strip()
name = name.title()
hello(name)




