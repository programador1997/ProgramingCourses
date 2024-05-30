t_prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    order_cost = 0
    while True:
        try:
            order = str(input("Item:"))
            if order in t_prices:
                order_cost = order_cost + t_prices[order]
                #print(f"adeded {order} + ${t_prices[order]} = {order_cost} ")
            else:
                print("please input a valid item")              

        except ValueError:
            print("please input a valid item")              
            ...
        except EOFError:
            print(f"Total: ${order_cost}")
            break
    


main()