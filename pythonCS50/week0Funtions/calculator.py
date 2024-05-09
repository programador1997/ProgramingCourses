
"""
x = input("Whats's x? ")
y = input("Whats's y? ")
#convert str to int
z = int(x) + int(y)
print(z)
"""
"""
x = int(input("Whats's x? "))
y = int(input("Whats's y? "))
print(x+y)
"""
"""
dont over complicate dont nest to much
print(int(input("Whats's x? "))+int(input("Whats's y? ")))
"""
"""
round numbers
x = float(input("Whats's x? "))
y = float(input("Whats's y? "))
print(round(x+y))
"""
"""

x = float(input("Whats's x? "))
y = float(input("Whats's y? "))
z = (round(x + y))
add format to numbers add a coma
print(f"{z:,}")
"""

def main():
    x = int(input("What's x ?"))
    print("x square is: ", square(x))

def square(n):
    return pow(n,2)

main()