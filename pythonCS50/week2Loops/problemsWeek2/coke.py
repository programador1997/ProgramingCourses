"""
Coke Machine
CS50 Coke Bottle
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user
of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that 
the user will only input integers, and ignore any integer that isn’t an accepted denomination.

usser input money
check if the input money is 25 or 10 or 5
    if it true add the money to de bank and check if the bank is equial to 50
        if true give the coke
        if false show the amount of money left yo pay the 50 cents
    if false show mesalle sorry i only accept 25 cents, 10 cents, and 5 cents. and print the money left to pay the 50 cents

"""

def main():
    bank = 0
    price = 50
    due = 0
    int(bank)
    while bank <= price:
        due = price-bank
        print(f"Amount Due:  {due}")
        amount = int(input("Insert Coin: "))
        if amount == 25 or amount == 50 or amount == 5:
            bank = bank + amount
            if price <= bank:
                print("COKE")
                if price < bank:
                    change = bank - price
                    print(f"Change: {change} ")
        else:
            print("sorry i only accept 25 cents, 10 cents, and 5 cens")

main()