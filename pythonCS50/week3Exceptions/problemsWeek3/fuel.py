def main():
    x = get_()
    print(f"{x}")


def get_():
    while True:
        fraction = (input("Fraction: "))
        try:
            x , y = fraction.split("/")
            x = int(x)    
            y = int(y)
            cap = x/y
        except ValueError:
            print("please input a valid fraction x/y")              
        except ZeroDivisionError:
            print("error divicion by zero x/0")                          
        else:
            if x > y :
                print("please enter a valid fraction x < y")
            break
    

    cap = cap * 100
    cap = str(int(cap)) + "%"

    if x == 0:
        cap = "E"
    elif x == y:
        cap = "F"
    return cap


main()
