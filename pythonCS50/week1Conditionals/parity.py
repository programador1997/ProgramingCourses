def main():
    x = int(input("What's x ?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(x):
    return x % 2 == 0
"""
    if x % 2 == 0:
        return True
    else:
        return False
u can in paython make this in one line
"""

main()