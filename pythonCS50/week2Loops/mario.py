"""
for _ in range(3):
    print("#")

def printColum(height):
    for _ in range(height):
        print("#")

def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

"""
def main():
    print_sqr(3)

def print_sqr(size):
    for i in range(size):
        for j in range(size):
            print("#", end=" ")

        print()

main()