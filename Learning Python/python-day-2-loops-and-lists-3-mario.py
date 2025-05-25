def main():
    print_square(3)
    #print_row(4)
    
'''    
    print_column(3)


def print_column(height):
    #for _ in range(height):
    print("#\n" * height, end = "")
'''

'''
def print_row(width):
    print("?" * width)
'''

'''
#Keep in mind we are stacking bricks of width 3 and height 3 to create a small square or a wall
def print_square(size):#For each row in square or small wall
    for i in range(size):
        for j in range(size):#For each brick in row of briks to create square or small wall
            print("#", end="")#Print the bricks to create a small 3x3 square or small wall built with with bricks
        print()
'''

#ALTERNATIVELY:


def print_square(size):
    for i in range(size):
        print("#" * size, end="")


main()