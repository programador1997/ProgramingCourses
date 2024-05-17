"""
                    while loop
i = 3
while i != 0:
    print("nya")
    i -= 1
"""

"""
                    list(array) and for loop
for i in [0, 1, 2]:
    print("nya")

by ussing the funtion range u don have to make the list for the for loop    
for _ in range(3):
    print("nya")

    in python u name "_" the variable that is no gona to be use in the code 

anothe way of doing thos is that can print and multiply 
print("nya\n" * 3, end="")

while True:
    n= int(input("What's n?"))
    if n > 0:
        break

for _ in range(n):
    print("nya")

"""

def main():
    number = get_number()
    nya(3)

def get_number():
    while True:
        n = int(input("What's n ?"))
        if  n > 0:
            break
    return n
    
def nya(n):
    for _ in range(n):
        print("nya")